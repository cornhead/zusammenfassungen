metadata_defaults  = ./yml/metadata_defaults.yml
metadata_article = ./yml/metadata_article.yml
metadata_beamer  = ./yml/metadata_beamer.yml

texPackages = ./tex/summary.sty

md2article = pandoc $(metadata_defaults) $(metadata_article)
md2beamer  = pandoc -s -f markdown+yaml_metadata_block+tex_math_dollars+multiline_tables -t beamer --slide-level=2 $(metadata_defaults) $(metadata_beamer)

summaryType = $(shell cat $< | ./sh/getSummaryType.sh)

md2pdf = $(if $(filter $(summaryType),formula_sheet), $(md2beamer), $(md2article) )


allPdfs = $(shell ls *.md | sed -e 's/.md/.pdf/g' -e 's/README.pdf//g' -e 's/TOOLS.pdf//g' -e 's/STYLEGUIDE.pdf//g') # TODO: find better method to exclude files from list

.PHONY: all
.PHONY: clean


all: $(allPdfs)

clean:
	rm -f $(allPdfs)

%.pdf: %.md $(metadata_defaults) $(metadata_article) $(metadata_beamer) $(texPackages)
	$(md2pdf) $< -o $@
	
