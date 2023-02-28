# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:43:34 2023

@author: Ravi
"""

from pytube import Playlist
from tqdm import tqdm
py = Playlist("https://www.youtube.com/playlist?list=PLZoTAELRMXVOSsBerFZKsdCaA4RYr4RGW")

print(f'Downloading : {py.title}')


for video in tqdm(py.videos):
    video.streams.first().download()
      
      
