import datetime, logging,  webbrowser
logger = logging.Logger('catch_all')


helloFile = open('E:\Programming\eclipseWorkspace\Planner\list1.txt', encoding="utf8")
# can it open an excel file next and the a database file?

Lines = helloFile.readlines()
helloFile.close()  

# How Are You feeling?
# day of the week cleaning


saveStateFile = open('E:\Programming\eclipseWorkspace\Planner\saveState.txt', encoding="utf8")
try:
    skipLines= int(saveStateFile.readline())
    saveStateFile.close()
    successfulLoad = False
except:
    print("couldn't open saveState.txt")
    skipLines=0
    
if skipLines==0:
    successfulLoad = True


responseLines = []
print("menu, skip forward, ")
currentLineNumber = 0
for line in Lines:
    if successfulLoad == False:
        skipLines-=1
        currentLineNumber+=1
        if skipLines <= 0: successfulLoad =True
        continue

    currentLineNumber+=1
    lineInQuestion = line.strip()
    
    if lineInQuestion == "":
        continue



    reply = input("Ln {}. {}\n".format(currentLineNumber, lineInQuestion))
    if reply == "":
        continue
    
    
    reggie = [0]
     # RegEx Logic # if string ends with .com
    reggie = reply.split()
    if reggie[0] == "skip":  # try except bracket
        skipLines = int(reggie[1])
        successfulLoad = False    
        continue
    if reply == "break":
        saveSaveState = open('E:\Programming\eclipseWorkspace\Planner\saveState.txt', 'w')
        saveSaveState.writelines(str(currentLineNumber))
        saveSaveState.close()
        break
    if reply == "sort":
        print("to", end = "")
        destination = input()
        destination = "E:\Programming\eclipseWorkspace\Planner\list" + destination +".txt"
        try:
            with open(destination, 'a') as sortFile:
                sortFile.write(lineInQuestion + "\n")
        except Exception as e:
            logger.error('Entry not saved correctly: '+ str(e))
        continue
    
    if reply == "end":
        saveSaveState = open('E:\Programming\eclipseWorkspace\Planner\saveState.txt', 'w')
        saveSaveState.writelines("0")
        saveSaveState.close()
        break
    if reply =="help":
        # Code goes here
        print("Reply to Lines")
        print("Enter end to reset and exit, type break to save progress")
        print("type nothing to skip a line, type skip 5 to skip ahead 5 lines, type skip forward to specify")
        continue
    if reply =="search":
        search_name = input("Enter search term : ")
        search_name = search_name.replace(" ", "+") 
        complete_url = "google.com/search?q=" + search_name
        webbrowser.open_new_tab(complete_url)
        continue
    if reply =="delete or insert or create or update":
        # Code goes here
        continue
    responseLines = responseLines + [reply]
    


replyFile = open('E:\Programming\eclipseWorkspace\Planner\list2.txt', 'a')

if len(responseLines) != 0:
    replyFile.writelines(datetime.date.today().isoformat() + "\n")

for linesHow in responseLines:
    replyFile.writelines(linesHow)
    replyFile.writelines("\n")
replyFile.close()