# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 15:21:31 2023

@author: Ravi
"""

from pytube import YouTube
from tqdm import tqdm

link ="https://www.youtube.com/watch?v=LVhWJhKQGhs"

youtube_1= YouTube(link)

print(youtube_1)

print(youtube_1.title)
print(youtube_1.thumbnail_url)

videos= youtube_1.streams.all()

for i in list(enumerate(videos)):
    print(i)
    print("############################")
    
    
qual = int(input("Enter which format to download"))
videos[qual].download()

print("successfully")