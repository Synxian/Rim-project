import tkinter
from PIL import ImageGrab
import time

window = tkinter.Tk()

window.geometry('300x300')
canvas = tkinter.Canvas(window, bg='black', highlightthickness=0)

it = 0

# Get coordinates from the event
# Event -> None
def canvas_coordintaes(event):
    global x_axis, y_axis
    x_axis, y_axis = event.x, event.y

# Draw a line based on a given event
# Event -> None
def draw(event):
    global x_axis, y_axis
    canvas.create_line((x_axis, y_axis, event.x, event.y), fill='white', width=2, smooth=True, splinesteps=50)
    x_axis, y_axis = event.x, event.y

# Save canvas as an image, then clear its content
# Event -> None
def save_and_erase(_):
    save_image(canvas)
    canvas.delete("all")

# Save canvas as an image, the name will be 'letter_n.jpg', where n is the current iteration, starting from 0
# Widget -> None
def save_image(widget):
    global it
    x=window.winfo_rootx()+widget.winfo_x()
    y=window.winfo_rooty()+widget.winfo_y()
    x1=x+widget.winfo_width()
    y1=y+widget.winfo_height()
    ImageGrab.grab().crop((x,y,x1,y1)).save(f'letter_{it}.jpg')
    it = it+1

# Binds left click and mouse motion to draw in canvas
canvas.bind('<Button-1>', canvas_coordintaes)
canvas.bind('<B1-Motion>', draw)
# activates the save_and_erase function with spacebar
window.bind('<space>', save_and_erase)
canvas.pack(anchor='nw', fill='both', expand=1)

window.mainloop()
