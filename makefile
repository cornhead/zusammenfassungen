md2pdf = pandoc -s -f markdown+yaml_metadata_block+tex_math_dollars -t latex --metadata-file=metadata.yml

.PHONY: all

all: digides_zusammenfassung.pdf risc_v_cheatsheet.pdf

%.pdf: %.md metadata.yml
	$(md2pdf) -o $@ $<
