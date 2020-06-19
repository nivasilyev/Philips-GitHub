# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 19:11:56 2020

@author: Rizilip
"""


import random
from formatString import formatString


def generateURLS(num):
    
    cityFile = open('E:\Programming\Cities.txt', encoding="utf8")
    cities = cityFile.readlines()
    cityFile.close()  
    
    taskFile = open('E:\Programming\SearchTerms.txt', 'r')
    tasks = taskFile.readlines()
    taskFile.close()
    
    urls = []
    
    for i in range(num):
        url = ""
        task = random.choice(tasks)
        city = random.choice(cities)
        url = "https://www.indeed.com/jobs?q=" + formatString(task, "indeedTask") + "+$30,000&l=" + formatString(city, "indeedCity")
        urls.append(url)
        
    return urls