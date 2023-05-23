import pyttsx3
book = open("")#enter the file location 
book_text=book.readlines()
engine = pyttsx3.init()
for i in book_text:
    engine.say(i)
    engine.runAndWait()