# # Leaflet cluster map of group locations
# 
# based on https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
# 
# Run this from the usermap/ directory, which contains the file pism_users.csv This scrapes the city of each group, geolocates it with geopy/Nominatim, and uses the getorg library to output data, HTML, and Javascript for a standalone cluster map.
# 
# Requires: getorg, geopy
#!pip install getorg python-frontmatter

import getorg
from geopy import Nominatim
import csv

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

#print(location_dict)
	
		
#for file in g:
#    with open(file, 'r') as f:
#        lines = f.read()
#        if lines.find('location: "') > 1:
#            loc_start = lines.find('location: "') + 11
#            lines_trim = lines[loc_start:]
#            loc_end = lines_trim.find('"')
#            location = lines_trim[:loc_end]
#        if lines.find('title: "') > 1:
#            loc_start = lines.find('title: "') + 8
#            lines_trim = lines[loc_start:]
#            loc_end = lines_trim.find('"')
#            title = lines_trim[:loc_end]
#        if lines.find('venue: "') > 1:
#            loc_start = lines.find('venue: "') + 8
#            lines_trim = lines[loc_start:]
#            loc_end = lines_trim.find('"')
#            venue = lines_trim[:loc_end]
#
#        key = str(title + " | " + venue + ", " + location)
#
#        location_dict[key] = geocoder.geocode(location)
#        print(key, "\n", location_dict[key])
#    count = count + 1

m = getorg.orgmap.create_map_obj()
# writes file org-locations.js
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="./", hashed_usernames=False)
