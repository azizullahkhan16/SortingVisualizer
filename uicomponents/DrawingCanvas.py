import tkinter as tk
from datastructure.ArrayBlock import ArrayBlock


class DrawingCanvas(tk.Canvas):
    blocks = None
    canvas = None

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(highlightthickness=0)  # Remove the default border
        self.bind("<B1-Motion>", self.paint)

    # This function creates blocks on the canvas
    @classmethod
    def create_blocks(cls, canvas, num_blocks):
        cls.canvas = canvas
        cls.blocks = ArrayBlock(num_blocks)
        cls.paint(cls.canvas)

    # This functions deletes all the blocks and cleans the canvas
    @classmethod
    def delete_blocks(cls):
        cls.blocks.delete_blocks()
        cls.canvas.delete(tk.ALL)

    # This function cleans everything on the canvas and draws everything again
    @classmethod
    def update_blocks(cls):
        cls.canvas.delete(tk.ALL)
        cls.paint(cls.canvas)

    # This function calls the block's bubble sort
    @classmethod
    def bubble_sort(cls):
        cls.blocks.bubble_sort(cls.canvas)

    # This function returns the canvas on which we are drawing
    @classmethod
    def get_canvas(cls):
        return cls.canvas

    # This function calls the block's paint function
    @classmethod
    def paint(cls, canvas):
        cls.blocks.paint(canvas)
