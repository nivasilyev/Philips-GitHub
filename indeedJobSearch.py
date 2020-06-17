# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:11:56 2020

@author: Rizilip
"""


import webbrowser, random
from formatString import formatString


cityFile = open('E:\Programming\globeProject.txt', encoding="utf8")
cities = cityFile.readlines()
cityFile.close()  

taskFile = open('E:\Programming\list0.txt', 'r')
tasks = taskFile.readlines()
taskFile.close()


reply = ""
Y= 0
for lines in cities:
    Y+=1
    url = ""
    searchTerm = tasks[random.randrange(20)]
    url = "https://www.indeed.com/jobs?q=" + formatString(searchTerm, "indeedTask") + "+$30,000&l=" + formatString(lines, "indeedCity")
    webbrowser.open(url)
    
    if Y%10 ==0:
        reply = input("hey press [br] to break early.\n")
        if reply == "br":
            
            break    
if reply != "br":
    url = "https://keep.google.com/u/0/"
    webbrowser.open(url)
