# # Leaflet cluster map of group locations
# 
# based on https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
# 
# Run this from the usermap/ directory, which contains the file pism_users.csv This scrapes the city of each group, geolocates it with geopy/Nominatim, and uses the getorg library to output data, HTML, and Javascript for a standalone cluster map.
# 
# Requires: getorg, geopy
#!pip install getorg python-frontmatter


#### creating PISM html usermap with Leaflet
# this python script builds a map of PISM users for the website based on 
# pism_users.csv   To get coordinates for the location given in the table,
# the python package getorg is used which automatically creates the html, js
# and css files to be included in the website. 
# As some manual changes in these files get overriden every time the python 
# script runs, there are a backup versions in the restore/ directory which 
# automatically get copied to the main repository.

# [mok 2021/06]: built python environment locally with  
#   mamba create -n pism_website python=3 geopy pip -c conda-forge
#   conda activate pism_website
#   pip install getorg

import getorg
from geopy import Nominatim
import csv
import shutil

input_file = 'pism_users.csv'

#geocoder = Nominatim(user_agent="my-application")
geocoder = Nominatim(user_agent='test')
location_dict = {}
location = ""


print()
with open(input_file, 'r') as f:
	csv_data = csv.DictReader(f, delimiter=',')
	for row in csv_data:
		#print(row)
		key = f'{row["name"]} | {row["city"]}, {row["country"]}'
		if row["website"] != '?':
			link = f'<a href=\'{row["website"]}\' target=\'_blank\'>{row["website"]}</a>'
			key += f' | {link}'
		location = f'{row["city"]}, {row["country"]}'
		location_dict[key] = geocoder.geocode(location)
		print(f'label:    {key}')
		print(f'location: {location}')
		print()


m = getorg.orgmap.create_map_obj()
# writes file org-locations.js, map.html, leaflet_dist/
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="./", hashed_usernames=False)


# some files include manual changes but are overwitten by getorg
# like map.html and leaflet_dist/screen.css
# thus a backup version is kept in restore/ and copied to replace the newly created ones
print()
print('copying files from restore/ directory')
shutil.copytree("./restore/","./", dirs_exist_ok=True)



