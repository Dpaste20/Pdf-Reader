# Pdf reader using python
from PyPDF2 import PdfReader
import pyttsx3

engine = pyttsx3.init() 
voices = engine.getProperty('voices')     
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')                           
engine.setProperty('rate', 180)

def speak(a):
    """Speak function"""
    engine.say(a)
    engine.runAndWait()


reader = PdfReader("bitcoin.pdf")

number_of_pages = reader.getNumPages()

for pages in range(number_of_pages):
    page = reader.pages[pages]
    text = page.extract_text()
    speak(text)



