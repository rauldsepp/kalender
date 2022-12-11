from tkinter import *
from tkcalendar import *
from datetime import *
from PIL import ImageTk, Image


class Agenda(Calendar):

    def __init__(self, master=None, **kw):
        Calendar.__init__(self, master, **kw)
        # change a bit the options of the labels to improve display
        for i, row in enumerate(self._calendar):
            for j, label in enumerate(row):
                self._cal_frame.rowconfigure(i + 1, uniform=1)
                self._cal_frame.columnconfigure(j + 1, uniform=1)
                label.configure(justify="center", anchor="n", padding=(1, 4))

    def _display_days_without_othermonthdays(self):
        year, month = self._date.year, self._date.month

        cal = self._cal.monthdays2calendar(year, month)
        while len(cal) < 6:
            cal.append([(0, i) for i in range(7)])

        week_days = {i: 'normal.%s.TLabel' % self._style_prefixe for i in range(7)}  # style names depending on the type of day
        week_days[self['weekenddays'][0] - 1] = 'we.%s.TLabel' % self._style_prefixe
        week_days[self['weekenddays'][1] - 1] = 'we.%s.TLabel' % self._style_prefixe
        _, week_nb, d = self._date.isocalendar()
        if d == 7 and self['firstweekday'] == 'sunday':
            week_nb += 1
        modulo = max(week_nb, 52)
        for i_week in range(6):
            if i_week == 0 or cal[i_week][0][0]:
                self._week_nbs[i_week].configure(text=str((week_nb + i_week - 1) % modulo + 1))
            else:
                self._week_nbs[i_week].configure(text='')
            for i_day in range(7):
                day_number, week_day = cal[i_week][i_day]
                style = week_days[i_day]
                label = self._calendar[i_week][i_day]
                label.state(['!disabled'])
                if day_number:
                    txt = str(day_number)
                    label.configure(text=txt, style=style)
                    date = self.date(year, month, day_number)
                    if date in self._calevent_dates:
                        ev_ids = self._calevent_dates[date]
                        i = len(ev_ids) - 1
                        while i >= 0 and not self.calevents[ev_ids[i]]['tags']:
                            i -= 1
                        if i >= 0:
                            tag = self.calevents[ev_ids[i]]['tags'][-1]
                            label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))
                        # modified lines:
                        text = '%s\n' % day_number + '\n'.join([self.calevents[ev]['text'] for ev in ev_ids])
                        label.configure(text=text)
                else:
                    label.configure(text='', style=style)

    def _display_days_with_othermonthdays(self):
        year, month = self._date.year, self._date.month

        cal = self._cal.monthdatescalendar(year, month)

        next_m = month + 1
        y = year
        if next_m == 13:
            next_m = 1
            y += 1
        if len(cal) < 6:
            if cal[-1][-1].month == month:
                i = 0
            else:
                i = 1
            cal.append(self._cal.monthdatescalendar(y, next_m)[i])
            if len(cal) < 6:
                cal.append(self._cal.monthdatescalendar(y, next_m)[i + 1])

        week_days = {i: 'normal' for i in range(7)}  # style names depending on the type of day
        week_days[self['weekenddays'][0] - 1] = 'we'
        week_days[self['weekenddays'][1] - 1] = 'we'
        prev_m = (month - 2) % 12 + 1
        months = {month: '.%s.TLabel' % self._style_prefixe,
                  next_m: '_om.%s.TLabel' % self._style_prefixe,
                  prev_m: '_om.%s.TLabel' % self._style_prefixe}

        week_nb = cal[0][1].isocalendar()[1]
        modulo = max(week_nb, 52)
        for i_week in range(6):
            self._week_nbs[i_week].configure(text=str((week_nb + i_week - 1) % modulo + 1))
            for i_day in range(7):
                style = week_days[i_day] + months[cal[i_week][i_day].month]
                label = self._calendar[i_week][i_day]
                label.state(['!disabled'])
                txt = str(cal[i_week][i_day].day)
                label.configure(text=txt, style=style)
                if cal[i_week][i_day] in self._calevent_dates:
                    date = cal[i_week][i_day]
                    ev_ids = self._calevent_dates[date]
                    i = len(ev_ids) - 1
                    while i >= 0 and not self.calevents[ev_ids[i]]['tags']:
                        i -= 1
                    if i >= 0:
                        tag = self.calevents[ev_ids[i]]['tags'][-1]
                        label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))
                    # modified lines:
                    text = '%s\n' % date.day + '\n'.join([self.calevents[ev]['text'] for ev in ev_ids])
                    label.configure(text=text)

    def _show_event(self, date):
        """Display events on date if visible."""
        w, d = self._get_day_coords(date)
        if w is not None:
            label = self._calendar[w][d]
            if not label.cget('text'):
                # this is an other month's day and showothermonth is False
                return
            ev_ids = self._calevent_dates[date]
            i = len(ev_ids) - 1
            while i >= 0 and not self.calevents[ev_ids[i]]['tags']:
                i -= 1
            if i >= 0:
                tag = self.calevents[ev_ids[i]]['tags'][-1]
                label.configure(style='tag_%s.%s.TLabel' % (tag, self._style_prefixe))
            # modified lines:
            text = '%s\n' % date.day + '\n'.join([self.calevents[ev]['text'] for ev in ev_ids])
            label.configure(text=text)


if __name__ == '__main__':
    
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
    root.geometry("800x600")
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


    calendar_image = ImageTk.PhotoImage(Image.open('calendar.png').resize((50, 50), Image.ANTIALIAS))  

    image_label = Label(header_frame,
                        image = calendar_image,
                        bg = "#B0E0E6"
                        )  
    image_label.pack(expand = True, fill = "both")


    cal = Agenda(calendar_frame,
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

