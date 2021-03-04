md2pdf = pandoc -s -f markdown+yaml_metadata_block+tex_math_dollars -t latex

.PHONY: all

all: digides_zusammenfassung.pdf

%.pdf: %.md
	$(md2pdf) -o $@ $<
