# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 23:34:49 2020
indeed Job Search
using custom URLs

@author: Rizilip
"""
import webbrowser
from formatCity import formatCity

jobFile = open('E:\Programming\eclipseWorkspace\globeProject\globeProject.txt', encoding="utf8")
cities = jobFile.readlines()
jobFile.close()  

for city in cities:
    formatCity(city, "indeed")
    url = "https://www.indeed.com/jobs?q=IT+help+desk&l=" + formatCity(city, "indeed")
    webbrowser.open(url)
    
    
url = "https://keep.google.com/u/0/"
webbrowser.open(url)