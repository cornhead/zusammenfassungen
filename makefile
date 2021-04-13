md2pdf = pandoc -s -f markdown+yaml_metadata_block+tex_math_dollars+multiline_tables -t latex --metadata-file=metadata.yml

.PHONY: all
.PHONY: clean

all:\
	digides_zusammenfassung.pdf\
	risc_v_cheatsheet.pdf\
	depsys_zusammenfassung.pdf\
	hm_zusammenfassung.pdf

clean:
	rm -f ./*.pdf

%.pdf: %.md metadata.yml
	$(md2pdf) -o $@ $<
