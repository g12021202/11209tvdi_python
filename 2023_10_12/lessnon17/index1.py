import dataSource
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('這是標題')
        mylabel = tk.Label(self, text = '這是內容', font=('Arial',20,'bold'))
        mylabel.pack(padx=100, pady=100)

def main():
    window = Window()
    window.mainloop()

if __name__ == "__main__":
    main()