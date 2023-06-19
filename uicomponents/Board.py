import tkinter as tk

from uicomponents.DrawingCanvas import DrawingCanvas
from uicomponents.Menubar import MenuBar

if __name__ == '__main__':
    # Create a window
    window = tk.Tk()
    window.title("Sorting Visualizer")
    window.configure(bg="#373737")
    window.resizable(False, False)  # Disable window resizing

    icon_image = tk.PhotoImage(file="C:/Users/user/PycharmProjects/SortingVisualizer/list.png")
    window.iconphoto(False, icon_image)

    # Define the dimensions of the window
    window_width = 1280
    window_height = 680

    # Create the menu bar
    menu_bar = MenuBar(window, width=100, height=500)
    menu_bar.pack(side=tk.LEFT, fill=tk.Y)

    # Create the drawing canvas
    canvas = DrawingCanvas(window, bg="#373737")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    # Position the window in the top-left corner
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry(f"{window_width}x{window_height}+0+0")

    # Start the main event loop
    window.mainloop()



