import tkinter
import os
from PIL import ImageGrab
from search import Searcher
import shutil

window = tkinter.Tk()

window.geometry('300x300')
canvas = tkinter.Canvas(window, bg='black', highlightthickness=0)

IT = 0

def canvas_coordintaes(event):
    """Get coordinates from the event"""
    global x_axis, y_axis
    x_axis, y_axis = event.x, event.y

def draw(event):
    """Draw a line based on a given event"""
    global x_axis, y_axis
    canvas.create_line((x_axis, y_axis, event.x, event.y), fill='white', width=18, smooth=True, splinesteps=32, capstyle='round', joinstyle='round')
    x_axis, y_axis = event.x, event.y

# Save canvas as an image, then clear its content
def save_and_erase(_):
    """Save canvas as an image, then clear its content"""
    save_image(canvas)
    canvas.delete("all")


def save_image(widget):
    """Save canvas as an image, the name will be 'letter_n.jpg', where n is the current iteration,
    starting from 0"""
    global IT
    space = True
    if not canvas.find_all()==():
        x=window.winfo_rootx()+widget.winfo_x()
        y=window.winfo_rooty()+widget.winfo_y()
        x1=x+widget.winfo_width()
        y1=y+widget.winfo_height()
        image = ImageGrab.grab().crop((x,y,x1,y1))
        image.resize((32, 32)).save(f'inputs/letter_{IT}.jpg')
        space=False
    searcher.add_letter(space)
    IT = IT+1

# Binds left click and mouse motion to draw in canvas
canvas.bind('<Button-1>', canvas_coordintaes)
canvas.bind('<B1-Motion>', draw)
# activates the save_and_erase function with spacebar
window.bind('<space>', save_and_erase)
canvas.pack(anchor='nw', fill='both', expand=1)
searcher=Searcher()
os.makedirs('inputs', exist_ok=True)

window.mainloop()
shutil.rmtree('inputs')
