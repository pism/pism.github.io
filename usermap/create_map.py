# # Leaflet cluster map of group locations
# 
# based on https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py
# (c) 2016-2017 R. Stuart Geiger, released under the MIT license
# 
# Run this from the usermap/ directory, which contains .md files of all your talks. This scrapes the location YAML field from each .md file, geolocates it with geopy/Nominatim, and uses the getorg library to output data, HTML, and Javascript for a standalone cluster map.
# 
# Requires: glob, getorg, geopy
#!pip install getorg python-frontmatter

import glob
import getorg
from geopy import Nominatim

g = glob.glob("_talks/*.md")

geocoder = Nominatim(user_agent="my-application")
location_dict = {}
location = ""
permalink = ""
title = ""
venue = ""
count=0

for file in g:
    with open(file, 'r') as f:
        lines = f.read()
        if lines.find('location: "') > 1:
            loc_start = lines.find('location: "') + 11
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            location = lines_trim[:loc_end]
        if lines.find('title: "') > 1:
            loc_start = lines.find('title: "') + 8
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            title = lines_trim[:loc_end]
        if lines.find('venue: "') > 1:
            loc_start = lines.find('venue: "') + 8
            lines_trim = lines[loc_start:]
            loc_end = lines_trim.find('"')
            venue = lines_trim[:loc_end]

        key = str(title + " | " + venue + ", " + location)

        location_dict[key] = geocoder.geocode(location)
        print(key, "\n", location_dict[key])
    count = count + 1

m = getorg.orgmap.create_map_obj()
getorg.orgmap.output_html_cluster_map(location_dict, folder_name="talkmap/", hashed_usernames=False)
