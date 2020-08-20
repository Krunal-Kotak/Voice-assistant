import pyttsx3
import os

pyttsx3.speak("Welcome to my tools")


while True:
	pyttsx3.speak("chat with me with your requirements")
	print("chat with me with your requirements : "  , end=' ')
	p = input()

	
 # it will ignore the line which contains no,don't,never,shouldnt like word or words
 
	if (("never" in p) or ("Never" in p) or ("NEVER" in p) or ("DON'T" in p) or ("don't" in p) or ("Don't" in p) or ("dont" in p) or ("Dont" in p) or ("DONT" in p) or ("shouldn't" in p) or ("Shouldn't" in p) or ("SHOULDN'T" in p) or ("shouldnt" in p) or ("Shouldnt" in p) or ("SHOULDNT" in p) or ("should not" in p) or ("Should not" in p) or ("SHOULD NOT" in p)) and (("run" in p) or ("RUN" in p) or ("Run" in p) or ("rUN" in p) or ("ruN" in p) or ("rUn" in p) or  ("execute" in p ) or ("EXECUTE" in p) or ("Execute" in p) or ("launch" in p) or ("Launch" in p) or ("LAUNCH" in p) or ("RUN" in p) or ("START" in p) or ("start" in p) or ("Start" in p) or ("open" in p)  or ("OPEN" in p) or ("Open" in p) or ("begin" in p) or ("BEGIN" in p) or ("FIND" in p) or ("Find" in p)  or ("find" in p) or ("Begin" in p) ) :
	  pyttsx3.speak("I will take care of it")
	  continue

# it will ignore lines with no, dont,never, shouldnt like words

	elif (("run" in p) or ("RUN" in p) or ("Run" in p) or ("rUN" in p) or ("ruN" in p) or ("rUn" in p) or  ("execute" in p ) or ("EXECUTE" in p) or ("Execute" in p) or ("launch" in p) or ("Launch" in p) or ("LAUNCH" in p) or ("RUN" in p) or ("START" in p) or ("start" in p) or ("Start" in p) or ("open" in p)  or ("OPEN" in p) or ("Open" in p) or ("begin" in p) or ("BEGIN" in p) or ("FIND" in p) or ("Find" in p)  or ("find" in p) or ("Begin" in p) )  and (("chrome" in p) or ("Chrome" in p) or ("CHROME" in p) or ("browser" in p) or ("Browser" in p) or ("BROWSER" in p)):
	  pyttsx3.speak("Opening " + p)
	  os.system("chrome")
	  continue

#it will launch chrome

	elif (("run" in p) or ("RUN" in p) or ("Run" in p) or ("rUN" in p) or ("ruN" in p) or ("rUn" in p) or  ("execute" in p ) or ("EXECUTE" in p) or ("Execute" in p) or ("launch" in p) or ("Launch" in p) or ("LAUNCH" in p) or ("RUN" in p) or ("START" in p) or ("start" in p) or ("Start" in p) or ("open" in p)  or ("OPEN" in p) or ("Open" in p) or ("begin" in p) or ("BEGIN" in p) or ("FIND" in p) or ("Find" in p)  or ("find" in p) or ("Begin" in p) ) and  (("notepad" in p) or ("NOTEPAD" in p) or ("Notepad" in p) or ("note pad" in p) or ("NOTE PAD" in p) or ("Note pad" in p) or ("EDITOR" in p) or ("Editor" in p) or ("editor" in p) or ("writer" in p) or ("Writer" in p) or ("WRITER" in p) or ("notebook" in p) or ("Notebook" in p) or ("NOTEBOOK" in p) or ("note book" in p) or ("Note book" in p) or ("NOTE BOOK" in p) or ("texteditor" in p) or ("text editor" in p) or ("Text editor" in p) or ("Texteditor" in p) or ("TEXTEDITOR" in p) or ("TEXT EDITOR" in p) or ("text writer" in p) or ("textwriter" in p) or ("Text writer" in p) or ("Textwriter" in p) or ("Text Writer" in p) or ("TextWriter" in p) or ("TEXT WRITER" in p) or ("TEXTWRITER" in p) or ("txt writer" in p) or ("txtwriter" in p) or ("Txt writer" in p) or ("Txtwriter" in p) or ("Txt Writer" in p) or ("TxtWriter" in p) or ("TXT WRITER" in p) or ("TXTWRITER" in p) or ("txt editer" in p) or ("txtediter" in p) or ("Txt editer" in p) or ("Txtediter" in p) or ("Txt Editer" in p) or ("TxtEditer" in p) or ("TXT EDITER" in p) or ("TXTEDITER" in p)) :
	  pyttsx3.speak("Opening " + p)
	  os.system("notepad")
	  continue

# it will launch notepad

	elif (("run" in p) or ("RUN" in p) or ("Run" in p) or ("rUN" in p) or ("ruN" in p) or ("rUn" in p) or  ("execute" in p ) or ("EXECUTE" in p) or ("Execute" in p) or ("launch" in p) or ("Launch" in p) or ("LAUNCH" in p) or ("RUN" in p) or ("START" in p) or ("start" in p) or ("Start" in p) or ("open" in p)  or ("OPEN" in p) or ("Open" in p) or ("begin" in p) or ("BEGIN" in p) or ("FIND" in p) or ("Find" in p)  or ("find" in p) or ("Begin" in p) ) and (("player" in p) or ("Player" in p) or ("PLAYER" in p) or ("wmediaplayer" in p) or ("WMEDIAPLAYER" in p) or ("winmediaplayer" in p) or ("WINMEDIAPLAYER" in p) or ("mediaplayer" in p) or ("MEDIAPLAYER" in p) or ("windowplayer" in p) or ("WINDOWPLAYER" in p) or ("winplayer" in p) or ("WINPLAYER" in p) or ("PLAYER" in p) or ("media" in p) or ("MEDIA" in p) or ("wmplayer" in p) or ("WMPLAYER" in p) or ("MPLAYER" in p) or ("WPLAYER" in p) or ("WMPLAYER" in p) or ("WMplayer" in p) or ("Wplayer" in p) or ("WPLAYER" in p) or ("Mplayer" in p) or ("MPLAYER" in p) or ("mplayer" in p) or ("wplayer" in p) or ("window player" in p) or ("WINDO PLAYER" in p) or ("window media" in p) or ("WINDOW MEDIA" in p) or ("windows media" in p) or ("WINDOWS MEDIA" in p) or ("windows player" in p) or ("WINDOWS PLAYER" in p) or ("video player" in p) or ("VIDEO PLAYER" in p) or ("player for video" in p) or ("PLAYER FOR VIDEO" in p) or ("videos player" in p) or ("VIDEOS PLAYER" in p) or ("player of windows" in p) or ("PLAYER OF WINDOWS" in p) ):
	  pyttsx3.speak("Opening " + p)
	  os.system("wmplayer")
	  continue

# it will launch Windows Media player

	elif (("run" in p) or ("RUN" in p) or ("Run" in p) or ("rUN" in p) or ("ruN" in p) or ("rUn" in p) or  ("execute" in p ) or ("EXECUTE" in p) or ("Execute" in p) or ("launch" in p) or ("Launch" in p) or ("LAUNCH" in p) or ("RUN" in p) or ("START" in p) or ("start" in p) or ("Start" in p) or ("open" in p)  or ("OPEN" in p) or ("Open" in p) or ("begin" in p) or ("BEGIN" in p) or ("FIND" in p) or ("Find" in p)  or ("find" in p) or ("Begin" in p) ) and (("write" in p) or ("wordpad" in p) or ("Wordpad" in p) or ("WORDPAD" in p)):
	  pyttsx3.speak("Opening " + p)
	  os.system("write")
	  continue

# it will launch WordPad

	elif (("run" in p) or ("RUN" in p) or ("Run" in p) or ("rUN" in p) or ("ruN" in p) or ("rUn" in p) or  ("execute" in p ) or ("EXECUTE" in p) or ("Execute" in p) or ("launch" in p) or ("Launch" in p) or ("LAUNCH" in p) or ("RUN" in p) or ("START" in p) or ("start" in p) or ("Start" in p) or ("open" in p)  or ("OPEN" in p) or ("Open" in p) or ("begin" in p) or ("BEGIN" in p) or ("FIND" in p) or ("Find" in p)  or ("find" in p) or ("Begin" in p) ) and (("calc" in p) or ("calculator" in p) or ("Calculator" in p) or ("CALCULATOR" in p)):
	  pyttsx3.speak("Opening " + p)
	  os.system("calc")
	  continue

# it will launch Caculator






	elif (("run" in p) or ("RUN" in p) or ("Run" in p) or ("rUN" in p) or ("ruN" in p) or ("rUn" in p) or  ("execute" in p ) or ("EXECUTE" in p) or ("Execute" in p) or ("launch" in p) or ("Launch" in p) or ("LAUNCH" in p) or ("RUN" in p) or ("START" in p) or ("start" in p) or ("Start" in p) or ("open" in p)  or ("OPEN" in p) or ("Open" in p) or ("begin" in p) or ("BEGIN" in p) or ("FIND" in p) or ("Find" in p)  or ("find" in p) or ("Begin" in p) ) and (("folder" in p) or ("Folder" in p) or ("FOLDER" in p) or ("directory" in p) or ("Directory" in p) or ("DIRECTORY" in p)):
	  print("Please enter the name of the folder you want to open : " , end='')
	  foldername=input()
	  if os.path.isdir(foldername):
	    pyttsx3.speak("Opening " + foldername)
	    os.startfile(foldername)
	    continue
	  else:
	    pyttsx3.speak("Sorry the folder named " + foldername + " doesn't exist in current directory.")
	    print("Sorry! the folder named "  + foldername +" doesn't exist in current directory.")
	    continue

# it will open a folder from current directory for you 









	elif (("make" in p) or ("Make" in p) or ("MAKE" in p) or ("create" in p) or ("Create" in p) or ("CREATE" in p) or ("build") or ("Build" in p) or ("BUILD" in p) or ("add" in p) or ("Add" in p) or ("ADD" in p) or ("MD" in p) or ("md" in p) or ("Md" in p) or ("mkdir" in p) or ("MKDIR" in p) or ("Mkdir" in p) or ("MkDir" in p)) and (("folder" in p) or ("Folder" in p) or ("FOLDER" in p) or ("directory" in p) or ("Directory" in p) or ("DIRECTORY" in p) or ("MD" in p) or ("md" in p) or ("Md" in p) or ("mkdir" in p) or ("MKDIR" in p) or ("Mkdir" in p) or ("MkDir" in p)):
	  pyttsx3.speak("Please enter a name for folder.")
	  print("Please enter a name for folder : " ,  end=' ')
	  f = input()
	  os.mkdir(f)
	  pyttsx3.speak("Done. Do you want to open it.")
	  print("Done! A folder with name " + f + " has been created. Do you want to open it :" , end='') 
	  choice=input()
	  if (("yes" in choice) or ("Yes" in choice) or ("YES" in choice) or ("yeah" in choice) or ("Yeah" in choice) or ("YEAH" in choice) or ("ok" in choice) or ("Ok" in choice) or ("OK" in choice) or ("okay" in choice) or ("Okay" in choice) or ("OKAY" in choice) or ("okey" in choice) or ("Okey" in choice) or ("OKEY" in choice) or ("ofcourse" in choice) or ("Ofcourse" in choice) or ("OFCOURSE" in choice)):
	    pyttsx3.speak("Okay.")
	    os.startfile(f)
	  else:
	    pyttsx3.speak(" Ok then.")
	    print("Ok then!")
	  continue

	elif (("no" in p) or ("No" in p) or ("NO" in p) or ("thanks" in p) or ("Thanks" in p) or ("THANKS" in p)):
	  pyttsx3.speak("Ok then. Have a nive day.")
	  print("Ok then! Have a nice day!")
	  break

# it will make a folder in current directory and ask you its name and after creating it it will ask you if you want to launch it 








	elif ( ("q" in p) or ("exit" in p) or ("EXIT" in p) or ("Exit" in p) or ("quit" in p) or ("QUIT" in p) or ("Quit" in p) or ("exit()" in p) or ("EXIT()" in p) or ("Exit()" in p) or ("quit()" in p) or ("QUIT()" in p) or ("Quit()" in p) or ("SHUT" in p) or ("shut" in p) or ("Shut" in p) or ("close" in p) or ("Close" in p) or ("CLOSE" in p) or ("TURN OFF" in p) or ("turn off" in p) or ("Turn off" in p) or ("turnoff" in p) or ("Turnoff" in p) or ("TURNOFF" in p) or ("BREAK" in p) or ("Break" in p) or ("break" in p) or ("stop" in p) or ("Stop" in p) or ("STOP" in p) or ("SHUTDOWN" in p) or ("Shutdown" in p) or ("shutdown" in p) or ("over" in p) or ("Over" in p) or ("OVER" in p) or ("finish" in p) or ("Finish" in p) or ("FINISH" in p)):
	  print("Have a nice day!")
	  break
  
# it is for breaking the loop and go back to command prompt or for exiting from python file
  
  
  
  
	elif ( " " in p) :
	  print("Please enter something else")
	  continue
# it will ask you  enter somthing when you don't enter any word'
	  
	  
	else:
	  print("dont support")
	  continue

# if the line you've entered is not satisfing any of the statements it will show you that what the statement is about is not defined in this programme

#thankyou for reading it it was quit interesting 

# Special thanks to Vimal Daga sir who gave this chance to participate in a contest like this
 
 # and one last thing i my pc doesn't supports pyttsx3 if there is error then sorry for that