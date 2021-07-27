.PHONY: build update check-links install

all: check-links

update:
	${MAKE} -C publications/
	${MAKE} -C usersmap/

build: update
	bundle exec jekyll build

serve:
	bundle exec jekyll serve

install:
	bundle install --path=vendor

check-links: build
	bundle exec htmlproofer \
	       --empty-alt-ignore \
	       --typhoeus-config '{ "ssl_verifypeer": false }' \
	       --root-dir _site \
	       _site
