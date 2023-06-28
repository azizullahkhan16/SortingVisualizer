import tkinter as tk
from datastructure.Arrayblock import ArrayBlock


class DrawingCanvas(tk.Canvas):
    blocks = None
    canvas = None
    animation_paused = False
    is_sorted = False

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(highlightthickness=0, height=200)  # Remove the default border
        self.bind("<B1-Motion>", self.paint)

    # This function creates blocks on the canvas
    @classmethod
    def create_blocks(cls, canvas, num_blocks):
        cls.canvas = canvas
        cls.blocks = ArrayBlock(num_blocks)
        cls.paint(canvas)

    # This functions deletes all the blocks and cleans the canvas
    @classmethod
    def delete_blocks(cls):
        cls.blocks.delete_blocks()
        cls.canvas.delete(tk.ALL)
        cls.is_sorted = False
        cls.animation_paused = False

    # This function cleans everything on the canvas and draws everything again
    @classmethod
    def update_blocks(cls):
        cls.canvas.delete(tk.ALL)
        cls.paint(cls.canvas)

    # This function calls the block's bubble sort
    @classmethod
    def bubble_sort(cls):
        cls.blocks.bubble_sort(cls.canvas)

    # This function calls the block's insertion sort
    @classmethod
    def insertion_sort(cls):
        cls.blocks.insertion_sort(cls.canvas)

    # This function calls the block's selection sort
    @classmethod
    def selection_sort(cls):
        cls.blocks.selection_sort(cls.canvas)

    # This function calls the block's quick sort
    @classmethod
    def quick_sort(cls):
        cls.blocks.quick_sort(cls.canvas)

    # This function calls the block's merge sort
    @classmethod
    def merge_sort(cls):
        cls.blocks.merge_sort(cls.canvas)

    # This function calls the block's tim sort
    @classmethod
    def tim_sort(cls):
        cls.blocks.tim_sort(cls.canvas)

    # This function calls the block's Shell-sort
    @classmethod
    def shell_sort(cls):
        cls.blocks.shell_sort(cls.canvas)

    # This function calls the block's counting sort
    @classmethod
    def counting_sort(cls):
        cls.blocks.counting_sort(cls.canvas)

    # This function calls the block's radix sort
    @classmethod
    def radix_sort(cls):
        cls.blocks.radix_sort(cls.canvas)

    # This function calls the block's heap sort
    @classmethod
    def heap_sort(cls):
        cls.blocks.heap_sort(cls.canvas)

    # This function calls the block's tree sort
    @classmethod
    def tree_sort(cls):
        cls.blocks.tree_sort(cls.canvas)

    # This function returns the canvas on which we are drawing
    @classmethod
    def get_canvas(cls):
        return cls.canvas

    # This function calls the block's paint function
    @classmethod
    def paint(cls, canvas):
        cls.blocks.paint(canvas)

        # Display current pass text in the top right corner
        current_pass_text = "Swaps: " + str(cls.blocks.num_swaps)
        if cls.is_sorted:
            color = "#00bf63"
        else:
            color = "#E44444"
        DrawingCanvas.get_canvas().create_text(canvas.winfo_width() - 10, 10, anchor="ne", text=current_pass_text,
                                               fill=color, font=('Arial', 12, 'bold'))

    @classmethod
    def get_animation_paused(cls):
        return cls.animation_paused

    @classmethod
    def set_animation_paused(cls, animation_paused):
        cls.animation_paused = animation_paused

    @classmethod
    def get_is_sorted(cls):
        return cls.is_sorted

    @classmethod
    def set_is_sorted(cls, is_sorted):
        cls.is_sorted = is_sorted

    @classmethod
    def get_num_swaps(cls):
        return cls.blocks.num_swaps

    @classmethod
    def set_num_swaps(cls, current_pass):
        cls.blocks.num_swaps = current_pass
