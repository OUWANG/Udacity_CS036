#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  2 14:08:43 2018

@author: Austin
Method overriding
"""
class Parent():
    def __init__(self, last_name, eye_color):
        print("parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last name - "+self.last_name)
        print("Eye color - "+self.eye_color)

class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("child constructor called")
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last name - "+self.last_name)
        print("Eye color - "+self.eye_color)
        print("Number of toys - "+str(self.eye_color))

billy_cyrus = Parent("Cyrus", "Blue")
miley_cyrus = Child("Cyrus", "Blue", 5)
miley_cyrus.show_info()      
#print (billy_cyrus.last_name)

# =============================================================================
# miley_cyrus = Child("Cyrus", "Blue", 5)
# print (miley_cyrus.last_name)
# print (miley_cyrus.number_of_toys)
# =============================================================================

