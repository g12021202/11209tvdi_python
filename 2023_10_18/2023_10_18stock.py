from tkinter import *
from tkinter import ttk
import yfinance as yf

class tsmc:
    def __init__(self):
        self.entry_stock = ttk.Entry(self.frame_content, width = 30,  font=('Arial', 15))
        self.entry_stock.grid(row=4, colimn=0, )