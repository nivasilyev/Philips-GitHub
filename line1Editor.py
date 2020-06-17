import datetime, webbrowser
helloFile = open('E:\Programming\eclipseWorkspace\Planner\list1.txt', encoding="utf8")
Lines = helloFile.readlines()    
helloFile.close() 


responseLines = []
Y=0
print("0 and end are the only special functions")
for line in Lines:
    Y=Y+1
    lineInQuestion = line.strip()
    if lineInQuestion == "":
        continue
    print("Ln {}. {}".format(Y, lineInQuestion), end = "")
    reply = input()
    if reply == "":
        responseLines = responseLines + [lineInQuestion]
        continue
    if reply == "0" or reply == "del":
        continue
    if reply =="search":
        search_name = lineInQuestion
        search_name = search_name.replace(" ", "+") 
        complete_url = "google.com/search?q=" + search_name
        webbrowser.open_new_tab(complete_url)
        continue
    if reply == "end":
        break
    else:
        responseLines = responseLines + [reply]


filePath = "E:\Programming\eclipseWorkspace\Planner\list1beta" + datetime.date.today().isoformat() + ".txt"
try:
    replyFile = open(filePath, 'a')
    for linesHow in responseLines:
        replyFile.writelines(linesHow)
        replyFile.writelines("\n")
    replyFile.close()
except:
    print("you're going to have to do all that again, something went wrong")

