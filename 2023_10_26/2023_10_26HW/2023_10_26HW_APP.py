import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datasource

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        try:
            datasource.download_air_data()
        except Exception as e:
            messagebox.showerror("錯誤",f'{e}\n將關閉應用程式\n請稍後再試')
            self.destroy()

def main():
    window = Window()
    window.title('空氣品質監測站基本資料')
    # window.geometry('600x300')
    window.resizable(height = False, width = False)
    update_data(window)
    window.mainloop()

if __name__ == '__main__':
    main()