import tkinter as tk


class DrawingCanvas(tk.Canvas):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(highlightthickness=0)  # Remove the default border
        self.bind("<B1-Motion>", self.paint)

    def paint(self, event):
        x, y = event.x, event.y
        self.create_oval(x - 2, y - 2, x + 2, y + 2, fill="black")
