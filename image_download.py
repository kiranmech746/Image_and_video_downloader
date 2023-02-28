# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 14:26:03 2023

@author: Ravi
"""

from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keywords = ["MS Dhoni","Rohit Sharma","Yuvraj Singh"]

for kw in keywords:
    response().download(kw,300)