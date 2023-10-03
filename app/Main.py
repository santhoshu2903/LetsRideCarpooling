from tkinter import *

import Controller
import Model
import View
import ttkbootstrap as tb

if __name__ == '__main__':
    root = tb.Window(title="Let's Go Ride with US", themename="superhero",size=(600,400),iconphoto='images/icon.jpg' )
    view = View.View(root)
    root.mainloop()
