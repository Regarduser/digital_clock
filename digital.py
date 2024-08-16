from tkinter import *
import tkinter as tk
from tkinter import ttk
import datetime


def date_time():
    time = datetime.datetime.now()
    hr = time.strftime('%I')
    min = time.strftime('%M')
    sec = time.strftime('%S')
    am = time.strftime('%p')
    ms = time.strftime('%f')[:2]
    Lab_hr.config(text=hr)
    Lab_min.config(text=min)
    Lab_sec.config(text=sec)
    Lab_ms.config(text=ms)
    Lab_am.config(text=am)
    Lab_hr.after(200, date_time)


clock = Tk()
clock.title("my clock")
clock.geometry('1000x500')
img = tk.Image('photo', file='icon.gif')
clock.tk.call('wm', 'iconphoto', clock._w,img )
clock.resizable(False, False)
#creating style
style = ttk.Style()

#styling
style = style.configure('TNotebook.Tab', font=('Time New Roman',20, 'italic' ))

notebook = ttk.Notebook(clock)
#this is time tab
Frame1 = Frame(notebook, bg='#ccc')
Frame2 = Frame(notebook)

notebook.add(Frame1, text='Time')
notebook.add(Frame2, text='Timer')
notebook.pack(expand=True, fill='both')




Lab_hr = Label(Frame1,text="00", font=('Time New Roman', 100, 'italic', 'bold'), bg="#ccc", fg="black")
Lab_hr.place(x = 50, y=100, height=220, width=200)
Lab_hr_txt = Label(Frame1,text="Hours", font=('Time New Roman', 20, 'italic', 'bold'), bg="#ccc", fg="black")
Lab_hr_txt.place(x = 100, y=270, height=30, width=100)

Lab_min = Label(Frame1,text="00", font=('Time New Roman', 100, 'italic', 'bold'), bg="#ccc", fg="black")
Lab_min.place(x = 300, y=100, height=220, width=200)
Lab_min_txt = Label(Frame1,text="Min", font=('Time New Roman', 20, 'italic', 'bold'), bg="#ccc", fg="black")
Lab_min_txt.place(x = 350, y=270, height=30, width=100)

Lab_sec = Label(Frame1,text="00", font=('Time New Roman', 100, 'italic', 'bold'), bg="#ccc", fg="black")
Lab_sec.place(x = 500, y=100, height=220, width=200)
Lab_sec_txt = Label(Frame1,text="Sec", font=('Time New Roman', 20, 'italic', 'bold'), bg="#ccc", fg="black")
Lab_sec_txt.place(x = 550, y=270, height=30, width=100)

Lab_ms = Label(Frame1,text="00", font=('Time New Roman', 44, 'bold'), bg="#ccc", fg="black")
Lab_ms.place(x = 700, y=210, height=55, width=53 )
Lab_ms_dot_txt = Label(Frame1,text="0", font=('Time New Roman', 20, 'italic', 'bold'), bg="#ccc", fg="black")
Lab_ms_dot_txt.place(x = 670 , y=235, height=30, width=20)


Lab_am = Label(Frame1,text="00", font=('Time New Roman', 50, 'italic', 'bold'), bg="#ccc", fg="black")
Lab_am.place(x = 760, y=100, height=220, width=200)





date_time()
clock.mainloop()
