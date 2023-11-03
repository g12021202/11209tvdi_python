import tkinter as tk
import tkintermapview

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        # create map widget
        map_widget = tkintermapview.TkinterMapView(self, width=1000, height=700, corner_radius=0)
        map_widget.pack(fill="both", expand=True)

        # set current position and zoom
        map_widget.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        narker = map_widget.set_position(25.083810, 121.546803, marker=True)  # 我家
        map_widget.set_zoom(17)
        narker.set_text("家")

if __name__ == '__main__':
    window = Window()
    window.geometry("1000x700")
    window.title("地圖")
    window.mainloop()