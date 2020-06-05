# -*- coding: utf-8 -*-
"""
Personal Organiser
Created on Thu Jun  4 18:32:32 2020

@author: Rizilip
"""


import calendar, datetime, logging,  webbrowser
logger = logging.Logger('catch_all')


my_date = datetime.date.today()

switch = {
        0: calendar.day_name[0],
        1: calendar.day_name[1],
        2: calendar.day_name[2],
        3: calendar.day_name[3],
        4: calendar.day_name[4],
        5: calendar.day_name[5],
        6: calendar.day_name[6]
    }
print(switch.get(my_date.weekday(), "Date Error") + ", " + my_date.isoformat())

todaysObservations = input("How are you and Riz feeling today?\n")
todaysObservations += input("Is there anything missing from your life?\n\n")

if todaysObservations.isspace() != True:
    todaysObservations = my_date.isoformat() + "\n" + todaysObservations
    helloFile = open('E:\Programming\eclipseWorkspace\Planner\diary.txt', 'a')
    helloFile.write(todaysObservations)
    helloFile.close()  


print(switch.get(my_date.weekday(), "Date Error") + ", " + my_date.isoformat())
switch2 = {
        0: "washing the windows and microwave",
        1: "change bedding, vacuum a room, and clean out fridge",
        2: "clean hallway closet, scrub toilet, wash mirrors, and organise your pants",
        3: "dusting, washing the windows and microwave",
        4: "decluttering, organizing, cleaning the bathroom, and mopping the kitchen floor",
        5: "organize books, wash a fridge shelf, and wash tables",
        6: "clean living room"
    }

print("chores for the day are " + switch2.get(my_date.weekday()))    



if my_date.weekday()%2 == 0:
    pass

plantFile = open('E:\Programming\eclipseWorkspace\Planner\plants.txt', 'r')
plantLine = plantFile.readline()
plantFile.close()


if str(plantLine) == str(my_date):
    plantResponse = input("Have you watered the plants today?\n").upper()
    if plantResponse == "YES" or "YE" or "Y":
        plantFile = open('E:\Programming\eclipseWorkspace\Planner\plants.txt', 'w')
        plantFile.write(str(my_date))
plantFile.close()  
    

plants = ["Ruby", "Red", "Kiwi", "Spike", "Aloe"]
for plant in plants:

    plantFeelings = input("how would you say " + plant + " is doing?\n")


    diaryFile = open('E:\Programming\eclipseWorkspace\Planner\plantLog.txt', 'a')
    diaryFile.write(plantFeelings)
    diaryFile.close()  
    

successfulLoad = True
skipLines = ""

