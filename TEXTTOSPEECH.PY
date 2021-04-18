import pyttsx3
to_speak  = input("enter your sentence\n")
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
name = str(input("enter file name to save\n"))
name2 = ".mp3"
name3= name+name2
engine.save_to_file(str(to_speak),str(name3))
engine.runAndWait()
