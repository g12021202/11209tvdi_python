'''
學習Canvas
'''
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.geometry("300x250")
        self.title("Lines")
        self.configure(background='#FA876E')

class MyFrame(tk.Frame):
    def __init__(self,master,**kwargs):
        super().__init__(master=master,**kwargs)
        self.configure(background='#FAE86E')
        self.img = Image.open("pets.png")
        self.pets = ImageTk.PhotoImage(self.img)
        petLabel = tk.Label(self,image=self.pets)
        petLabel.pack()
        self.pack(fill='both', expand=1)

def main():
    window = Window()
    myFrame = MyFrame(window)
    window.mainloop()

if __name__ =="__main__":
    main()