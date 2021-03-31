"""
A very simple python script for downloading the lyrics of the artists from the lists retrieved in download_rapper_list
notebook. The scripts uses the lyricsgenius client created by John W. Miller, that really helped in the simplification
of this task.
"""

import json
from lyricsgenius import Genius

genius = Genius()
genius.retries = 5

with open('../groups.json') as f:
    groups = json.load(f)

for group in groups:
    artist = genius.search_artist(group, max_songs=100)
    artist.save_lyrics(filename=group)

with open('../rappers.json') as f:
    rappers = json.load(f)

for rapper in rappers:
    artist = genius.search_artist(rapper, max_songs=100)
    artist.save_lyrics(filename=rapper)