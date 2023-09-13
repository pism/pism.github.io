#!/usr/bin/env python3

import json
import folium
from folium.plugins import MarkerCluster

def load_data(filename):
    "Load marker locations, names, etc from a JSON file"
    with open(filename, 'r') as f:
         return json.load(f)

def label(name, info):
    "Create a label for a marker"
    link = f"<a href=\'{info['url']}\' target=\'_blank\'>{info['url']}</a>"
    return f"{name} | {info['city']}, {info['country']} | {link}"

def create_map(data, output_filename):
    "Create a leaflet map using information about markers provided in `data`"
    Map = folium.Map(min_lon=-180, max_lon=180, max_bounds=True)

    clusters = {}
    for name, info in data.items():
        location = f"{info['city']}, {info['country']}"
        if location not in clusters.keys():
            clusters[location] = MarkerCluster(name=location).add_to(Map)

    for name, info in data.items():

        if "developer" in info.keys():
            icon = folium.map.Icon(color="green", icon="screwdriver-wrench", prefix="fa")
        else:
            icon = folium.map.Icon(color="blue")

        popup = folium.map.Popup(label(name, info), max_width=250)

        location = f"{info['city']}, {info['country']}"
        cluster = clusters[location]

        folium.Marker(location=(info["lat"], info["lon"]),
                      tooltip=name,
                      popup=popup,
                      icon=icon).add_to(cluster)

    Map.save(output_filename)

if __name__ == "__main__":
    import sys
    data = load_data(sys.argv[1])

    create_map(data, sys.argv[2])
