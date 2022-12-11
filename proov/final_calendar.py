from tkinter import *
from tkcalendar import *
from datetime import *
from PIL import ImageTk, Image


def add_event():
    date = datetime.strptime(cal.get_date(), "%d.%m.%y")
    cal.calevent_create(date, event_entry.get(), 'reminder')
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
        
        
root = Tk()
root.title("Kalender")
root.iconbitmap("icon_calendar.ico")
root.geometry("600x600")
root.configure(bg="#B0E0E6")

header_frame = Frame(root, bg = "#B0E0E6")  
calendar_frame = Frame(root, bg = "#B0E0E6")  
date_frame = Frame(root, bg = "#B0E0E6")
entry_frame = Frame(root, bg = "#B0E0E6")
button_frame = Frame(root, bg = "#B0E0E6")

header_frame.pack(expand = True, fill = "both")
calendar_frame.pack(expand = True, fill = "both")  
date_frame.pack(expand = True, fill = "both")
entry_frame.pack(expand = True, fill = "both")
button_frame.pack(expand = True, fill = "both")


header_label = Label(header_frame,
                     text = "Kalender",
                     font = ('verdana','25','bold'),
                     bg = "#B0E0E6",
                     fg = "#191970"
                     )
header_label.pack(expand = True, fill = "both", pady=20)


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


add_button = Button(button_frame,
                    text="Lisa",
                    command=add_event
                    )
add_button.pack()




root.mainloop()


