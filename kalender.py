from tkinter import *
from PIL import ImageTk, Image
import calendar
from datetime import date

def displayCalendar():  
    # get the month and year data from the spin boxes  
    month = int(month_box.get())  
    year = int(year_box.get())  
  
    # using the month() method from the calendar module to  
    # get the month info and storing in the variable  
    output_calendar = calendar.month(year, month)  
  
    # using the delete() method to delete the output  
    calendar_field.delete(1.0, 'end')  
  
    # displaying the resultant calendar  
    calendar_field.insert('end', output_calendar)
    
def reset():  
    # using the delete() method to delete the output  
    calendar_field.delete(1.0, 'end')  
  
    # setting the values of the IntVar objects to current month and year  
    month_var.set(current_month)  
    year_var.set(current_year)  
  
    # using the config() method and assigning the  
    # textvariable parameter to different IntVar objects  
    month_box.config(textvariable = month_var)  
    year_box.config(textvariable = year_var)
    
def close():  
    # using the destroy() method to close the application  
    guiWindow.destroy()

def addEvent():
    newGUI = Tk()
    newGUI.title("Sündmus")
    newGUI.geometry("500x200")
    newGUI.resizable(0, 0)  
    newGUI.config(bg="#B0E0E6")

    header_frame = Frame(newGUI, bg = "#B0E0E6")  
    entry_frame = Frame(newGUI, bg = "#B0E0E6") 
    event_frame = Frame(newGUI, bg = "#B0E0E6")   
    button_frame = Frame(newGUI, bg = "#B0E0E6")  
  
    header_frame.pack(expand = True, fill = "both")
    entry_frame.pack(expand = True, fill = "both")  
    event_frame.pack(expand = True, fill = "both")
    button_frame.pack(expand = True, fill = "both")
    
    header_label = Label(  
        header_frame,  
        text = "Sündmus",  
        font = ('verdana','25','bold'),  
        bg = "#B0E0E6",  
        fg = "#191970"  
    )   
    event_field = Text(  
        event_frame,
        width = 40,   
        height = 2,  
        font = ("consolas", "14"),  
        relief = RIDGE,  
        borderwidth = 2  
    )
    add_button = Button(
        button_frame,
        text = "LISA",
        bg = "#191970",  
        fg = "#E0FFFF",
        command = add
    )
    day_label = Label(
        entry_frame,
        text = "Päev:",  
        font = ("consolas", "10", "bold"),  
        bg = "#B0E0E6",  
        fg = "#000000"  
    )
    month_label = Label(  
        entry_frame,  
        text = "Kuu:",  
        font = ("consolas", "10", "bold"),  
        bg = "#B0E0E6",  
        fg = "#000000"  
    )  
    year_label = Label(  
        entry_frame,  
        text = "Aasta:",  
        font = ("consolas", "10", "bold"),  
        bg = "#B0E0E6",  
        fg = "#000000"     
    )  
    # using the place() method to set the position of the labels
    day_label.place(x = 70, y = 0)
    month_label.place(x = 170, y = 0)  
    year_label.place(x = 270, y = 0)

    # creating the objects of the IntVar class
    day_var = IntVar(entry_frame)
    month_var = IntVar(entry_frame)  
    year_var = IntVar(entry_frame)  
      
    # storing the current month and year information
    current_day = date.today().day
    current_month = date.today().month  
    current_year = date.today().year  
      
    # setting the current month and year to the IntVar objects
    day_var.set(current_day)
    month_var.set(current_month)  
    year_var.set(current_year)  
      
    # creating the spin boxes to enter month and year
    day_box = Spinbox(
        entry_frame,
        from_ = 1,
        to = 31,
        width = "5",
        textvariable = day_var
    )
    month_box = Spinbox(  
        entry_frame,  
        from_ = 1,  
        to = 12,  
        width = "5",  
        textvariable = month_var   
        )  
    year_box = Spinbox(  
        entry_frame,  
        from_ = 0000,  
        to = 3000,  
        width = "5",  
        textvariable = year_var  
    )  
    # using the place() method to set the position of the spin boxes  
    day_box.place(x = 110, y = 0)
    month_box.place(x = 210, y = 0)  
    year_box.place(x = 320, y = 0)
    add_button.place(x = 240, y = 00)
    
    event_field.pack(expand = False, fill = None)
    header_label.pack(expand = True, fill = "both")
    newGUI.mainloop()
    
def add():
    return
    
    # main function  
if __name__ == "__main__":  
    # creating an object of the Tk() class  
    guiWindow = Tk()  
    # setting the title for the main window  
    guiWindow.title("Kalender")  
    # setting the size and position of the main window  
    guiWindow.geometry('500x550+650+250')  
    # disabling the resizable option  
    guiWindow.resizable(0, 0)  
    # setting the background color to #B0E0E6  
    guiWindow.configure(bg="#B0E0E6")  
    # setting the bitmap icon for the application  
    guiWindow.iconbitmap("icon_calendar.ico")  
    
    header_frame = Frame(guiWindow, bg = "#B0E0E6")  
    entry_frame = Frame(guiWindow, bg = "#B0E0E6")  
    result_frame = Frame(guiWindow, bg = "#B0E0E6")
    event_frame = Frame(guiWindow, bg = "#B0E0E6")
    button_frame = Frame(guiWindow, bg = "#B0E0E6")  
  
# using the pack() method to set the positions of the frames  
header_frame.pack(expand = True, fill = "both")
entry_frame.pack(expand = True, fill = "both")  
result_frame.pack(expand = True, fill = "both")
event_frame.pack(expand = True, fill = "both")
button_frame.pack(expand = True, fill = "both")

header_label = Label(  
    header_frame,  
    text = "Kalender",  
    font = ('verdana','25','bold'),  
    bg = "#B0E0E6",  
    fg = "#191970"  
    )  
# using the pack() method to set the position of the label  
header_label.pack(expand = True, fill = "both")

calendar_image = ImageTk.PhotoImage(Image.open('calendar.png').resize((50, 50), Image.ANTIALIAS))  
# creating the label to display the imported image  
image_label = Label(  
    header_frame,  
    image = calendar_image,  
    bg = "#B0E0E6"  
    )  
# using the pack() method to set the position of the label  
image_label.pack(expand = True, fill = "both")

month_label = Label(  
    entry_frame,  
    text = "Kuu:",  
    font = ("consolas", "10", "bold"),  
    bg = "#B0E0E6",  
    fg = "#000000"  
)  
year_label = Label(  
    entry_frame,  
    text = "Aasta:",  
    font = ("consolas", "10", "bold"),  
    bg = "#B0E0E6",  
    fg = "#000000"     
)  
# using the place() method to set the position of the labels  
month_label.place(x = 120, y = 0)  
year_label.place(x = 268, y = 0)

# creating the objects of the IntVar class  
month_var = IntVar(entry_frame)  
year_var = IntVar(entry_frame)  
  
# storing the current month and year information  
current_month = date.today().month  
current_year = date.today().year  
  
# setting the current month and year to the IntVar objects  
month_var.set(current_month)  
year_var.set(current_year)  
  
# creating the spin boxes to enter month and year  
month_box = Spinbox(  
    entry_frame,  
    from_ = 1,  
    to = 12,  
    width = "5",  
    textvariable = month_var   
    )  
year_box = Spinbox(  
    entry_frame,  
    from_ = 0000,  
    to = 3000,  
    width = "5",  
    textvariable = year_var  
)  
# using the place() method to set the position of the spin boxes  
month_box.place(x = 180, y = 0)  
year_box.place(x = 320, y = 0)

calendar_field = Text(  
    result_frame,  
    width = 20,   
    height= 8,  
    font = ("consolas", "14"),  
    relief = RIDGE,  
    borderwidth = 2  
)  
# using the pack() method to set the position of the textbox  
calendar_field.pack(expand = False, fill = None)

display_button = Button(  
    button_frame,  
    text = "NÄITA",  
    bg = "#191970",  
    fg = "#E0FFFF",  
    command = displayCalendar  
)  
  
# RESET BUTTON  
reset_button = Button(  
    button_frame,  
    text = "TAASTA",  
    bg = "#191970",  
    fg = "#E0FFFF",  
    command = reset  
)  
  
# CLOSE BUTTON  
close_button = Button(  
    button_frame,  
    text = "SULGE",  
    bg = "#191970",  
    fg = "#E0FFFF",  
    command = close  
)  

event_button = Button(
    button_frame,
    text = "LISA SÜNDMUS",
    bg = "#191970",  
    fg = "#E0FFFF",
    command = addEvent
)

# using the place() method to set the positions of the buttons  
display_button.place(x = 165, y = 0)  
reset_button.place(x = 230, y = 0)  
close_button.place(x = 305, y = 0)
event_button.place(x = 210, y = 30)

guiWindow.mainloop()  