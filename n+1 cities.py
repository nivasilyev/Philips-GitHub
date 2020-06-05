# -*- coding: utf-8 -*-
import webbrowser
from formatCity import formatCity
"""
Created on Tue Jun  2 11:46:18 2020

n+1 cities


@author: Rizilip
"""
## landmarks
# mansion tours


cityFile = open('E:\Programming\eclipseWorkspace\globeProject\globeProject.txt', encoding="utf8")
cities = cityFile.readlines()
cityFile.close()  

Y=0
print("type break to exit loop - ")
 
for city in cities:
    Y=Y+1
    currentCity = formatCity(city,1)
    cityURL = "https://www.apartments.com/" + currentCity + "/under-1300-pet-friendly-dog/?so=2"
    webbrowser.open_new_tab(cityURL)
    currentCity = formatCity(city,2)
    cityURL = "https://www.google.com/search?q=things+to+do+in+" + currentCity
    webbrowser.open_new_tab(cityURL)
    currentCity = formatCity(city,4)
    cityURL = "https://www.walkscore.com/" + currentCity
    webbrowser.open_new_tab(cityURL)
   
    
    comments = input("tell me about the things to do in this city: ")
    if comments == "":
            continue
    if comments == "break":
            break
    newCityFile = open('E:\Programming\eclipseWorkspace\globeProject\cityResults.txt', 'a')
    currentCity = formatCity(city,3)
    newCityFile.write(currentCity + "\t")
    newCityFile.write(comments + "\n")
    newCityFile.close()


    
    
GlobeProjectURL = "https://drive.google.com/drive/u/1/folders/0B5MHN_Nvv_AqfjAyVVpHMkpwSDdJMEhRQnhnQnBRQkFCVFBjbE5WamktLWN6eHR4cmNUR2M"
webbrowser.open(GlobeProjectURL, autoraise = False)
newCity = input("Please enter a New City : ")
newCityFile = open('E:\Programming\eclipseWorkspace\globeProject\globeProject.txt', 'a')
newCityFile.write(newCity + "\n")
newCityFile.close()



#with open(<filename>,'r') as contents:
#      save = contents.read()
#with open(<filename>,'w') as contents:
#      contents.write(< New Information >)
#with open(<filename>,'a') as contents:
#      contents.write(save)