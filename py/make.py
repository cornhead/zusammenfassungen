# this script is to be invoked from the summary base-directory, not the py-directory

import sys
import os
from Zusammenfassung import SummaryType


# ------ configuration ------------
tex_image_path = os.path.join('img', 'tex')

exclude = [
	'README.md',
	'TOOLS.md' ,
	'STYLEGUIDE.md'
]


zusammenfassung = SummaryType(
	yml=[
		os.path.join('yml', 'metadata_defaults.yml'),
		os.path.join('yml', 'metadata_article.yml')
	],
	identifier='summary-type: (zusammenfassung|summary)',
	further_dependencies = [os.path.join('tex', 'summary.sty')]
)

formelsammlung = SummaryType(
	yml=[
		os.path.join('yml', 'metadata_defaults.yml'),
		os.path.join('yml', 'metadata_beamer.yml')
	],
	identifier='summary-type: (formelsammlung|formula_sheet)',
	pandoc_options=['-s', '-f', 'markdown', '-t', 'beamer']
)



# ------ functions ------------------

def make_all():
	SummaryType.make_all_images(tex_image_path)
	zusammenfassung.make_all(exclude=exclude)
	formelsammlung.make_all(exclude=exclude)
	
def make_clean():
	SummaryType.clean_all_images(tex_image_path)
	zusammenfassung.clean_all(exclude=exclude)
	formelsammlung.clean_all(exclude=exclude)



# ------- main -----------------------

if (len(sys.argv) > 2):
	print('expected at most 1 command line argument,', len(sys.argv)-1, 'given.')
	sys.exit(-1)

elif (len(sys.argv) == 1):
	make_all()
	
else:
	v = sys.argv[1]
	
	if   (v == 'all'): make_all()
	elif (v == 'clean'): make_clean()
	else:
		print('unknown command line argument \''+v+'\', expecting either \'all\' or \'clean\'.')
		sys.exit(-1)
	
sys.exit(0)
