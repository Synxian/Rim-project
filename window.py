import tkinter
from PIL import ImageGrab
import time

window = tkinter.Tk()

window.geometry('300x300')
canvas = tkinter.Canvas(window, bg='black', highlightthickness=0)

it = 0

def canvas_coordintaes(event):
    global x_axis, y_axis
    x_axis, y_axis = event.x, event.y

def draw(event):
    global x_axis, y_axis
    canvas.create_line((x_axis, y_axis, event.x, event.y), fill='white', width=2, smooth=True, splinesteps=50)
    x_axis, y_axis = event.x, event.y

def save_and_erase(_):
    getter(canvas)
    canvas.delete("all")

def getter(widget):
    global it
    x=window.winfo_rootx()+widget.winfo_x()
    y=window.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(f'letter{it}.jpg')
    it = it+1

canvas.bind('<Button-1>', canvas_coordintaes)
canvas.bind('<B1-Motion>', draw)
window.bind('<space>', save_and_erase)
canvas.pack(anchor='nw', fill='both', expand=1)

window.mainloop()
