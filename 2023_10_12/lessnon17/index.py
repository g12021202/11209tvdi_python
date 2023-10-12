import dataSource
import tkinter as tk
from tkinter import ttk

def main():
    window = tk.Tk()
    window.title('這是標題')
    mylabel = tk.Label(window, text = '這是內容', font=('Arial',20,'bold'))
    mylabel.pack(padx=100, pady=100)

    window.mainloop()

if __name__ == "__main__":
    main()