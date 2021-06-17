metadata_defaults  = ./yml/metadata_defaults.yml
metadata_article = ./yml/metadata_article.yml
metadata_beamer  = ./yml/metadata_beamer.yml

md2article = pandoc $(metadata_defaults) $(metadata_article)
md2beamer  = pandoc -s -f markdown+yaml_metadata_block+tex_math_dollars+multiline_tables -t beamer $(metadata_defaults) $(metadata_beamer)

articles = \
	digides_zusammenfassung\
	depsys_zusammenfassung\
	hm_zusammenfassung\
	rta_zusammenfassung\
    psv_zusammenfassung

beamers = \
	digides_formelsammlung\
	adm_formelsammlung
	

.PHONY: all
.PHONY: articles
.PHONY: beamers
.PHONY: clean


all: articles beamers	

clean:
	rm -f $(all)
	
	
articles:
	for article in $(articles); do \
		echo $(md2article) $${article}.md -o $${article}.pdf ;\
		     $(md2article) $${article}.md -o $${article}.pdf ; \
	done

beamers:
	for beamer in $(beamers); do \
		echo $(md2beamer) $${beamer}.md -o $${beamer}.pdf ;\
		     $(md2beamer) $${beamer}.md -o $${beamer}.pdf ; \
	done

%.pdf: %.md $(metadata_defaults) $(metadata_article) $(metadata_beamer)
	$(md2article) -o $@ $<
	
