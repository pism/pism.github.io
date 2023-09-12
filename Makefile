BUNDLE=bundle
DESTDIR=_site
.PHONY: all build update serve check-links check-external-links install

all: check-links

img/pism_publications.png: publications/plot_references.py publications/applications.bib
	python3 $^ $@

update: img/pism_publications.png
	${MAKE} -C publications/
	${MAKE} -C usersmap/

build: update
	${BUNDLE} exec jekyll build -d ${DESTDIR}

serve: update
	${BUNDLE} exec jekyll serve

install:
	${BUNDLE} install --path=vendor

check-links: build
	${BUNDLE} exec htmlproofer \
	       --empty-alt-ignore \
	       --disable-external \
	       --root-dir ${DESTDIR} \
	       ${DESTDIR}

check-external-links: build
	${BUNDLE} exec htmlproofer \
	       --empty-alt-ignore \
	       --typhoeus-config '{ "ssl_verifypeer": false, "connecttimeout": 300, "timeout": 300, "headers" : {"User-Agent": "Mozilla/5.0 (compatible; htmlproofer)"}}' \
	       --root-dir ${DESTDIR} \
	       ${DESTDIR}
