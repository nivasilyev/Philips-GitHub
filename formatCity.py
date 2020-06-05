# -*- coding: utf-8 -*-
import re
"""
Created on Tue Jun  2 11:46:18 2020

class format city


@author: Rizilip
"""
## landmarks
# mansion tours
def formatCity(f,m):
    currentCity = f.strip()
    name = ""
    method = m
    match = re.findall("[\w\s]+,\s\w+", currentCity)
    match = str(match)
    if method == 1:
        for character in match:
            if character.isalpha() :
                name += character
            if character == ", ":
                name += "-"
            if character == " ":
                name += "-"


    if method == 2:
        for character in match:
            if character.isalpha() :
                name += character
            if character == ", ":
#                name += "+"
                pass
            if character == " ":
                name += "+"

    if method == 3:      
        for character in match:
            if character.isalpha() :
                name += character
            if character == ",":
                name += ", "
            if character == " ":
                name += character
            name = "{:>20s}".format(name)
    if method == 4:      
        
        for character in match:
            if character.isalpha() or character == " ":
                name += character
        name = str(name)
        chunks = name.split()
        name = chunks[-1] + "/"
        name += chunks[0]
        if chunks[1] != chunks[-1]:
            name+="_" + chunks[1]
    if method == "indeed":
        for character in match:
            if character.isalpha() :
                name += character
            if character == ", ":
                name += "%2C+"
                pass
            if character == " ":
                name += "+"


#Sacramento%2C+CA
   
    return name
      