import re
import subprocess
import textwrap
import os

class SummaryType:
	
	_command_for_special_block = ['pandoc', '-f', 'markdown', '-t', 'latex']
	_command_for_bullet_list   = ['pandoc', '-f', 'markdown', '-t', 'latex']
	_command_for_tikz_images_latex = ['pdflatex', '-synctex=1', '-interaction=nonstopmode']
	_command_for_tikz_images_imagemagick = ['convert', '-density', '300', '-colorspace', 'rgb']
	
	encoding = 'UTF-8'
	
	'''
	@param: [optional] yml: path to a file with the yml-metadata or list of paths (internally, it will always be cast to a list)
	@param: [optional] pandoc_options: a string that is given to pandoc as options
	@param: [optional] encoding
	@param: [optional] identifier: a regex (given as string) that identifies files that are of this summary type
	@param: [optional] input_name_to_output_name: a function that takes the name of the input file and returns the desired output file name
	@param: [optional] further_dependencies: a list of strings representing paths that will be needed for make (so if a dependency changes, the target file needs to be remade)
	'''
	def __init__(self, yml=None, pandoc_options=None, encoding='UTF-8', identifier='.*', input_name_to_output_name=None, further_dependencies=[]):
		self.encoding = encoding
		
		self.yml = yml
		if (yml != None):
			if (type(yml) == str):
				self.yml = [yml]
		else: self.yml = []
		
		if (pandoc_options == None): pandoc_options = ['-s', '-f', 'markdown', '-t', 'latex']
		self.pandoc_command = ['pandoc']+ pandoc_options
		
		self.identifier = re.compile(identifier)
		
		
		def standard_input_name_to_output_name(input_name):
			basename, _ = os.path.splitext(input_name)
			output_name = basename+'.pdf'
			return output_name
		
		self.input_name_to_output_name = input_name_to_output_name
		if (self.input_name_to_output_name == None):
			self.input_name_to_output_name = standard_input_name_to_output_name
			
		self.dependencies = self.yml + further_dependencies
		
	'''
	@brief: takes a file and parses it such that it is ready to be given to pandoc
	@detail: the main tasks of the parsing are to
		-) include specified yml-files in the yml-header or create a yml-header
		-) parse markdown-commands for custom environments like `theorem` or `note`
	@param: file: the path to the file that is to be parsed
	@return: a string with the compiled file, ready for pandoc
	'''
	def parse(self, file):
		
		# this is gonna be the output string
		s = ""
		
		# this is a string for intermediate results (e.g. for extracting special blocks and compiling them separately)
		i = ""
		
		# basically, we are building an FSM. For the philosophy of state and next_state, see VHDL (yes, I'm a computer engineer)
		next_state={
			'found_non_blank_line': False,
			'in_yml_header': False,
			'found_yml_header': False,
			'entering_yml_header': False,
			'entering_bullet_list': False,
			'exiting_bullet_list': False,
			'in_bullet_list': False,
			'in_special_block': False,
			'entering_special_block': False,
			'exiting_special_block': False,
			'special_block_type' : "",
			'special_block_title': ""
		}
		state = next_state.copy()
		
		regex={
			'blank_line': re.compile('^\s*$'),
			'yml_start_end': re.compile('\s*---\s*'),
			'bullet_list_item': re.compile('^\s*(\*|#\.)\s'),
			'special_block_start' : re.compile('\s*:::(theorem|note|example|comment)(\s+([a-zA-Z].*)|\s*)'),
			'special_block_end' : re.compile('\s*:::(\n|$)')
		}
		
		with open(file, 'r') as f:
			
			
			for line in f:
				
				# ------ next state logic ---------------
				# ---------------------------------------
			
				# yml-headers
				next_state['entering_yml_header'] = False
				
				# if no yml-header exists, create one
				if (not regex['blank_line'].match(line)): next_state['found_non_blank_line'] = True
				if (state['found_non_blank_line'] and not state['found_yml_header']): next_state['found_yml_header'] = True
				
				if (not state['found_yml_header'] or state['in_yml_header']):
					if (regex['yml_start_end'].match(line)):
						next_state['found_yml_header'] = True
						next_state['in_yml_header'] = not state['in_yml_header']
						if (not state['in_yml_header']):
							next_state['entering_yml_header'] = True
			
				# bullet lists
				
				next_state['entering_bullet_list'] = False
				next_state['exiting_bullet_list'] = False
				next_state['in_bullet_list'] = False
				
				if (regex['bullet_list_item'].match(line)):
					next_state['in_bullet_list'] = True
					next_state['entering_bullet_list'] = not state['in_bullet_list']
				else:
					next_state['exiting_bullet_list'] = state['in_bullet_list']


			
				# special blocks
				
				next_state['entering_special_block'] = False
				next_state['exiting_special_block'] = False
					
				if (regex['special_block_start'].match(line)):
					next_state['in_special_block'] = True
					next_state['entering_special_block'] = True
					
					res = regex['special_block_start'].search(line)
					next_state['special_block_type'] = res.group(1)
					next_state['special_block_title'] = res.group(2).strip()
					
				if (regex['special_block_end'].match(line)):
					next_state['in_special_block'] = False
					next_state['exiting_special_block'] = True
					
					
					
				# ------ "output" logic -----------------
				# ---------------------------------------
				
				if (next_state['found_non_blank_line'] and not next_state['found_yml_header'] and len(self.yml) > 0):
					s += '---\n'
					
					for yml_file in self.yml:
						with open(yml_file, 'r') as yml:
							yml_content = yml.read()
						
						s += yml_content + '\n'
						
					s += '---\n' + line
				
				elif (state['entering_yml_header']):
				
					for yml_file in self.yml:
						with open(yml_file, 'r') as yml:
							yml_content = yml.read()
						
						s += yml_content + '\n'
						
					s += line
				
				
				
				elif (next_state['entering_bullet_list']):
					i = line
				elif (next_state['in_bullet_list']):
					i += line
					
				elif (next_state['exiting_bullet_list']):
					
					p = subprocess.Popen(self._command_for_bullet_list,
						stdout = subprocess.PIPE,
						stdin  = subprocess.PIPE
					)
					
					i = textwrap.dedent(i)
					
					p.stdin.write(i.encode(self.encoding))
					p.stdin.close()
					
					out = p.stdout.read().decode(self.encoding)
					
					s += out + line
									
				
				
				elif (next_state['entering_special_block']):
					pass # this leaves out the entering line
					
				elif (state['in_special_block']):					
					if (state['entering_special_block']):
						i = ''
					
					if (not next_state['exiting_special_block']): i += line
					
				elif (state['exiting_special_block']):
					if (state['special_block_type'] != 'comment'):
						p = subprocess.Popen(self._command_for_special_block,
							stdout = subprocess.PIPE,
							stdin  = subprocess.PIPE
						)
						
						i = textwrap.dedent(i)
						
						p.stdin.write(i.encode(self.encoding))
						p.stdin.close()
						
						out = p.stdout.read().decode(self.encoding)
						
						s += '\\begin{'+state['special_block_type']+'}{'+state['special_block_title']+'}\n' + out + '\\end{'+state['special_block_type']+'}\n' + line
					
					
				else:
					s += line
				
				# ------ updating state -----------------
				# ---------------------------------------
				
				state = next_state.copy()
				
		return s
		
	
	'''
	@brief: reads a file and decides wheter it is of the type described by this object
	'''
	def check_type_of(self, file):
		with open(file, 'r') as f:
			content = f.read()
			return self.identifier.search(content) != None
			
		return False
		
	'''
	@brief: takes a string representing a file and determins whether it needs to be made (GNU make)
	'''
	def shall_make(self, file):
		if not os.path.isfile(file): return False
		
		target = self.input_name_to_output_name(file)
		
		if (not os.path.isfile(target)): return True
		
		for dependency in self.dependencies + [file]:
			if (os.path.getmtime(dependency) > os.path.getmtime(target)): return True
			
		return False
	
	'''
	@brief: takes a string or list of string representing the paths to files that should be made according to this summary type, regardless of whether the type-identifyer is found!
	@param: [optional] verbose (standard is True)
	'''
	def make(self, files, verbose=True):
		if type(files) == str: files = [files]
		
		for file in files:
			target = self.input_name_to_output_name(file)
			
			if (verbose): print('making', target, '\t...\t', end='')
			
			if (not self.shall_make(file)):
				if (verbose): print('already up to date')
				continue
			
			parsed = self.parse(file)
			
			command = self.pandoc_command + ['-o', target]
			
			p = subprocess.Popen(command,
				stderr  = subprocess.PIPE,
				stdin  = subprocess.PIPE
			)
			
			p.stdin.write(parsed.encode(self.encoding))
			p.stdin.close()
			
			err = p.stderr.read().decode(self.encoding)
			
			if (len(err) > 0):
				print(err)
				return -1
			
			if (verbose): print('finished')
				
		return 0
	
	'''
	@brief: returns a list of all files that match this summary type
	@param: [optional] dir: the directory. If not specified './' is assumed.
	@param: [optional] exclude: a list with files to exclude
	'''
	def get_all_matching_files(self, dir=None, exclude=[]):
		if (dir == None): dir = './'
		
		if (not os.path.isdir(dir)): return []
		
		matches = []
		
		for entry in os.listdir(dir):
			if (entry in exclude): continue
			
			file = os.path.join(dir,entry)
						
			if (not os.path.isfile(file)): continue
			if (os.path.splitext(file)[1] != '.md'): continue
			if (not self.check_type_of(file)): continue
			
			matches += [file]
		
		return matches
			
	'''
	@brief: takes a string representing the path of a directory and makes all files within it that match the summary type
	@param: [optional] dir: the directory. If not specified './' is assumed.
	@param: [optional] exclude: a list with files to exclude
	'''
	def make_all(self, dir=None, exclude=[]):
		self.make(self.get_all_matching_files(dir, exclude))
	
	
	'''
	@brief: takes a string or a list of strings representing the paths of files of which the respective targets will be cleaned up (without checking the type of summary)
	'''
	def clean(self, files, verbose=True):
		if type(files) == str: files = [files]
		
		for file in files:
			target = self.input_name_to_output_name(file)
			
			if (verbose): print('cleaning up', target, '\t...\t', end='')
			
			if (not os.path.isfile(target)):
				if (verbose): print('nothing to clean up')
				continue
			
			os.remove(target)
			
			if (verbose): print('finished')
	
	'''
	@brief: takes the path to a directory and cleanes up all targets of this summary type
	'''	
	def clean_all(self, dir=None, exclude=[]):
		self.clean(self.get_all_matching_files(dir, exclude))
	
	'''
	@brief: takes a path to a tex-file with stand-alone tikz-images and returns a list with the names of the included targets
	@detail:
		This function scans the tex-file for a comment like '% output-name: my_awesome_name' and appends the given name as
		a suffix to the filename with png-extension for the next picture. So 'psv_images.tex' could create 'psv_images_my_awesome_name.png', for instance.
		If no such comment is given, the pictures will be numbered also counting the named ones so that naming a picture in retrospect does not
		affect the names of the subsequent pictures.
	@return: returns a list of targets or -1 if an error occured
	'''
	@staticmethod
	def get_targets_of_image(file):
		
		regex_standaloneenv = re.compile('standaloneenv{(.*)}\s*(%.*)?')
		regex_set_name = re.compile('\s*%+\s*output-name:\s*(.*)')
		regex_begin_picture = None # to be set during scanning
		regex_end_picture = None # to be set during scanning
		
		base_name, extension = os.path.splitext(file)
		
		targets = []
		name_buffer = ''
		ctr = 0
		standaloneenv = None
		
		with open(file, 'r') as f:
			for line in f:
				if (regex_standaloneenv.search(line)):
					standaloneenv = regex_standaloneenv.search(line).group(1)
					
					regex_begin_picture = re.compile('begin{'+standaloneenv+'}')
					regex_end_picture = re.compile('end{'+standaloneenv+'}\s*')
					
				if (regex_set_name.match(line)): name_buffer = regex_set_name.match(line).group(1)
				
				if (regex_begin_picture != None and regex_begin_picture.search(line)):					
					new_name = base_name + '_'
					if (len(name_buffer) > 0): new_name += name_buffer
					else: new_name += str(ctr)
					new_name += '.png'
					
					targets += [new_name]
					
				if (regex_end_picture != None and regex_end_picture.search(line)):
					name_buffer = ''
					ctr += 1
		
		if (standaloneenv == None): return -1 # check if standaloneenv-specification was found
		
		return targets
				
		
	
	'''
	@brief: Takes a path to a tex-file with stand-alone tikz-images and checks if all its targets are up date. Return, whether the file shall be recompiled
	@param: file: the path to the tex-file
	@return: returns whether the file shall be made or not, or -1 if an error occured
	'''
	@staticmethod
	def shall_make_image(file):
		if (not os.path.isfile(file)): return False
		
		targets = SummaryType.get_targets_of_image(file)
		
		if (type(targets) == int and targets < 0): return -1
		
		for target in targets:
			if (not os.path.isfile(target)): return True
			
			if (os.path.getmtime(file) > os.path.getmtime(target)): return True
		
		return False
		
		
	
	'''
	@brief: takes a string representing the path to a tex-file with stand-alone tikz-images and compiles it (if it is not up to date)
	@param: file: the path to the tex-file
	'''
	@staticmethod
	def make_image(file, verbose=True):
		if (not os.path.isfile(file)): return -1
		
		if (verbose): print('making', file, '\t...\t', end='')
		
		shall_make = SummaryType.shall_make_image(file)
		
		if (type(shall_make) == int and shall_make < 0):
			if (verbose): print('unable to find \standaloneenv{} command')
			return -1
		
		if (not shall_make):
			if (verbose): print('already up to date')
			return 0
		
		dir = os.path.dirname(file)
		
		command1 = SummaryType._command_for_tikz_images_latex + ['-jobname=tmp', '-output-directory='+dir, file] # pdflatex will write output in same directory as `file` and call it tmp.pdf
		
		p1 = subprocess.Popen(command1,
			stderr = subprocess.PIPE,
			stdout = subprocess.PIPE
		)
		
		err1 = p1.stderr.read().decode(SummaryType.encoding)
		out1 = p1.stdout.read().decode(SummaryType.encoding)
		
		if (len(err1) > 0):
			if (verbose):
				print('failed:')
			print(err1)
			return -1
		
		command2 = SummaryType._command_for_tikz_images_imagemagick + [os.path.join(dir, 'tmp.pdf'), os.path.join(dir, 'tmp_%d.png')]
		
		p2 = subprocess.Popen(command2,
			stderr = subprocess.PIPE,
			stdout = subprocess.PIPE
		)
		
		err2 = p2.stderr.read().decode(SummaryType.encoding)
		out2 = p2.stdout.read().decode(SummaryType.encoding)
		
		if (len(err2) > 0):
			if (verbose):
				print('failed:')
			print(err2)
			return -1
		
		targets = SummaryType.get_targets_of_image(file)
		
		for i, target in enumerate(targets):
			os.rename(os.path.join(dir,'tmp_'+str(i)+'.png'), target) # (target already includes directory path)
		
		for tmp_file in ['tmp.aux', 'tmp.log', 'tmp.pdf', 'tmp.synctex.gz']:
			os.remove(os.path.join(dir, tmp_file))
		
		if (verbose): print('finished')
		
		return 0
	
	
	@staticmethod
	def make_all_images(dir=None):
		if (dir == None): dir = './'
		
		if (not os.path.isdir(dir)): return False
		
		for entry in os.listdir(dir):
			
			file = os.path.join(dir, entry)
						
			if (not os.path.isfile(file)): continue
			if (os.path.splitext(file)[1] != '.tex'): continue
			
			SummaryType.make_image(file)
	
	@staticmethod
	def clean_all_images(dir=None, verbose=True):
		if (dir == None): dir = './'
		
		if (not os.path.isdir(dir)): return False
		
		for entry in os.listdir(dir):
			
			file = os.path.join(dir, entry)
						
			if (not os.path.isfile(file)): continue
			if (os.path.splitext(file)[1] != '.tex'): continue
			
			if (verbose): print('cleaning up', file, '\t...\t', end='')
			
			targets = SummaryType.get_targets_of_image(file)
			
			if (type(targets) == int and targets < 0):
				print('unable to find \standaloneenv{} command')
				continue
			
			for target in targets:
				if (os.path.isfile(target)): os.remove(target)
			
			print('finished')
