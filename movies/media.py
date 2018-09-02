#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  1 21:23:31 2018

@author: Austin
"""

"""
Notes:
    
The double underscore is python telling us that this function is reserved, a special function or method
class - a blue print with both data and methods
instance - (toy story, avatar)
constructor - the init function
self - the object being created
instance variables - (titile, storyline, etc)
instance method - functions within class
"""
import webbrowser

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
    def show_poster(self):
        webbrowser.open(self.poster_image_url)
