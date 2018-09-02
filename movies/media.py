#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:23:31 2018

@author: Austin
"""

"""
Notes:
    
The double underscore is python telling us that this function is reserved, a special function or method
class
instance
constructor
self - the object being created
"""
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube