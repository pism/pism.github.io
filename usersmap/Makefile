org-locations.js: pism_users.csv
	python3 create_map.py

	# restore customized version of some files:
	cp -rf restore/* .

install: requirements.txt
	pip3 install --user -r $^
