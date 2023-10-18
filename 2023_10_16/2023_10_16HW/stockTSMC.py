#1, Imports the tkinter module.
import tkinter as tkinter

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("Image")
        
