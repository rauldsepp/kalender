from tkinter import *
from PIL import ImageTk, Image
import calendar
from datetime import date
import os
import webbrowser


text_cal = calendar.HTMLCalendar(firstweekday = 0)
 
year = 2018
month = 9
# default value of width is 0
 
# printing formatmonth
html = text_cal.formatyear(year, 3)
path = os.path.abspath('kalender.html')
url = 'file://' + path

with open(path, 'w') as f:
    f.write(html)
webbrowser.open(url)