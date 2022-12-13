from tkinter import *
from tkcalendar import *
from datetime import *
import time
from PIL import ImageTk, Image


def add_event():
    if event_entry.get() != "Lisa üritus või meeldetuletus" and event_entry.get() != "":
        date = datetime.strptime(cal.get_date(), "%d.%m.%y")
        reminder = event_entry.get() + ", kell " + hour_spin.get() + ":" + minute_spin.get()
        cal.calevent_create(date, reminder, 'reminder')
        clear_entry()

def clear_entry():
    event_entry.delete(0, 'end')
    event_entry.insert(0, 'Lisa üritus või meeldetuletus')
    root.focus_set()

def click(*args):
    if event_entry.get() == "Lisa üritus või meeldetuletus":
        event_entry.delete(0, 'end')
        
def sel(*args):
    date = cal.selection_get().strftime("%d.%m.%Y")
    if date == today.strftime("%d.%m.%Y"):
        date_label.config(text="Täna")
    else:
        date_label.config(text=date)
        
def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    
    clock_label.config(text=hour + ":" + minute + ":" + second)
    clock_label.after(1000, clock)
    
def disable(*args):
    root.focus_set()
    
        
root = Tk()
root.title("Kalender")
root.iconbitmap("icon_calendar.ico")
root.geometry("600x600")
root.configure(bg="#B0E0E6")

header_frame = Frame(root, bg = "#B0E0E6")  
calendar_frame = Frame(root, bg = "#B0E0E6")  
date_frame = Frame(root, bg = "#B0E0E6")
entry_frame = Frame(root, bg = "#B0E0E6")
time_frame = Frame(root, bg = "#B0E0E6")
button_frame = Frame(root, bg = "#B0E0E6")

header_frame.pack(expand = True, fill = "both")
calendar_frame.pack(expand = True, fill = "both")  
date_frame.pack(expand = True, fill = "both")
entry_frame.pack(expand = True, fill = "both")
time_frame.pack()
button_frame.pack(expand = True, fill = "both")


header_label = Label(header_frame,
                     text = "Kalender",
                     font = ('verdana','25','bold'),
                     bg = "#B0E0E6",
                     fg = "#191970"
                     )
header_label.pack(expand=True, fill="both", pady=20)


calendar_image = ImageTk.PhotoImage(Image.open('calendar.png').resize((50, 50)))  
image_label = Label(header_frame,
                    image = calendar_image,
                    bg = "#B0E0E6"
                    )  
image_label.pack(expand = True, fill = "both")


cal = Calendar(calendar_frame,
               selectmode="day",
               showweeknumbers=False,
               locale="est",
               cursor="hand2",
               font = ('verdana', '10', 'bold')
               )
cal.pack(pady=20, fill="both", expand=True)
cal.tag_config('reminder', background='red')
cal.bind("<<CalendarSelected>>", sel)


clock_label = Label(date_frame,
                    text="",
                    font=('verdana','25','bold'),
                    bg = "#B0E0E6",
                    fg = "#191970"
                    )
clock_label.pack(expand=True, fill="both")



today = date.today()
date_label = Label(date_frame,
                   text="Täna: "+str(today.strftime("%d.%m.%Y")),
                   font = ('verdana','15','bold'),
                   bg = "#B0E0E6",
                   fg = "#191970"
                   )
date_label.pack(pady=20)


event_entry = Entry(entry_frame,
                    width=60
                    )
event_entry.insert(0, "Lisa üritus või meeldetuletus")
event_entry.pack()
event_entry.bind("<Button-1>", click)


hours = ("00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23")
hour_spin = Spinbox(time_frame,
                    width=5,
                    values=hours
                    )
hour_spin.grid(row=0, column=0)
hour_spin.bind("<FocusIn>", disable)


minutes = ("00", "05", "10", "15", "20", "25", "30", "35", "40", "45", "50", "55")
minute_spin = Spinbox(time_frame,
                    width=5,
                    values=minutes
                    )
minute_spin.grid(row=0, column=1)
minute_spin.bind("<FocusIn>", disable)


add_button = Button(button_frame,
                    text="Lisa",
                    command=add_event
                    )
add_button.pack(pady=20)


clock()


root.mainloop()


