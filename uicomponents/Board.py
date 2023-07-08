import os
import tkinter as tk

from uicomponents.AnalysisSpace import AnalysisSpace
from uicomponents.DrawingCanvas import DrawingCanvas
from uicomponents.Menubar import MenuBar


class Board:
    if __name__ == '__main__':
        # Create a window
        window = tk.Tk()
        window.title("Sorting Visualizer")
        window.configure(bg="#373737")
        window.resizable(False, False)  # Disable window resizing

        # Get the absolute path of the script file
        script_dir = os.path.dirname(os.path.abspath(__file__))

        icon_image = tk.PhotoImage(file=os.path.join(script_dir, "res/list.png"))
        window.iconphoto(False, icon_image)

        # Define the dimensions of the window
        window_width = 1280
        window_height = 700

        # Create the menu bar
        menu_bar = MenuBar(window, width=100, height=200)
        menu_bar.pack(side=tk.LEFT, fill=tk.Y)

        # Create the drawing canvas
        canvas = DrawingCanvas(window, bg="#373737", width=window_width - 100, height=200)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        DrawingCanvas.create_blocks(canvas, 10)

        # Create the analysis space
        analysis_space = AnalysisSpace(window, width=window_width, height=window_height - 200)
        analysis_space.place(x=0, y=200)
        AnalysisSpace.create_graph(analysis_space)

        # Position the window in the top-left corner
        screen_width = window.winfo_screenwidth()
        screen_height = window.winfo_screenheight()
        window.geometry(f"{window_width}x{window_height}+0+0")

        # Bind the minimize button event to pause the animation
        window.bind("<Unmap>", menu_bar.pause_on_minimize)

        # Start the main event loop
        window.mainloop()


