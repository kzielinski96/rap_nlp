"""
A simple python script for simplification of the JSON files retrieved in the build_dataset script, they had a lot
of redundant data and point of this script is extracting only the meaninguf information from them
"""

import json
import os

keys = ['api_path', 'description', 'id', 'image_url', 'name', 'url']
song_keys = ['api_path', 'id', 'title', 'title_with_featured', 'release_date', 'lyrics']

def concat_json(data_trimmed, tmp_json, empty):
    empty.append(tmp_json)
    return {
        **data_trimmed,
        'songs': empty
    }


def clean_json(file):
    with open(file, 'r') as data_file:
        data = json.load(data_file)

    empty = []

    data_trimmed = {key: data[key] for key in keys}
    songs = data['songs']

    for dict in songs:
        data_trimmed = concat_json(data_trimmed, {key: dict[key] for key in song_keys}, empty)

    with open(os.path.join('dataset/', '%s.json' %data_trimmed['name']), 'w') as data_file:
        json.dump(data_trimmed, data_file)


for root, dirs, files in os.walk('dataset\original'):
    for file in files:
        if file.endswith('.json'):
            print('Working on ', file)
            clean_json(os.path.join(root, file))