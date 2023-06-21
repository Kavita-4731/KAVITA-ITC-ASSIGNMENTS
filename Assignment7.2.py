import tkinter as tk
import calendar

def show_calendar():
    try:
        year = int(year_entry.get())
       
        cal = calendar.calendar(year)
        calendar_text.config(text=cal)
       
    except ValueError:
        calendar_text.config(text="Please enter a valid year")

window = tk.Tk()
window.title("Calendar Application")

year_label = tk.Label(window, text="Enter Year:")
year_label.pack()

year_entry = tk.Entry(window)
year_entry.pack()

show_button = tk.Button(window, text="Show Calendar", command=show_calendar)
show_button.pack()

calendar_text = tk.Label(window, text="")
calendar_text.pack()

window.mainloop()
