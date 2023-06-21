import tkinter as tk
from PIL import Image, ImageTk
from uicomponents.DrawingCanvas import DrawingCanvas
from uicomponents.ToolTip import Tooltip
from window.ConfigWindow import ConfigWindow


class MenuBar(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(bg="#373737")
        self.is_playing = False

        # Create menu buttons
        self.config_button = tk.Button(
            self,
            width=40,
            height=40,
            bd=0,
            highlightthickness=0,
            bg="#373737",
            activebackground="#373737"  # Set active-background to the same color as the background
        )
        self.config_button.pack(side=tk.TOP, pady=5)
        self.config_button.config(command=self.on_config_button_click)
        Tooltip(self.config_button, "Set Configuration")

        self.play_pause_button = tk.Button(
            self,
            width=40,
            height=40,
            bd=0,
            highlightthickness=0,
            bg="#373737",
            activebackground="#373737"  # Set active-background to the same color as the background
        )
        self.play_pause_button.pack(side=tk.TOP, pady=5)
        self.play_pause_button_tooltip = Tooltip(self.play_pause_button, "Sort")

        # Set custom icons for the buttons
        self.set_icon(
            self.config_button,
            "C:/Users/user/PycharmProjects/SortingVisualizer/configUnpressed.png",
            "C:/Users/user/PycharmProjects/SortingVisualizer/configPressed.png"
        )
        self.set_play_pause_icons(
            "C:/Users/user/PycharmProjects/SortingVisualizer/playUnpressed.png",
            "C:/Users/user/PycharmProjects/SortingVisualizer/pausePressed.png"
        )

    def on_config_button_click(self):
        # Add your config logic here
        config_window = ConfigWindow(self)
        print("Config button clicked")

    def set_icon(self, button, icon_path_unpressed, icon_path_pressed):
        icon_image_unpressed = Image.open(icon_path_unpressed)
        icon_image_unpressed = icon_image_unpressed.resize((30, 30))  # Adjust the size as needed
        photo_image_unpressed = ImageTk.PhotoImage(icon_image_unpressed)

        icon_image_pressed = Image.open(icon_path_pressed)
        icon_image_pressed = icon_image_pressed.resize((30, 30))  # Adjust the size as needed
        photo_image_pressed = ImageTk.PhotoImage(icon_image_pressed)

        button.config(image=photo_image_unpressed)
        button.image = photo_image_unpressed  # Save a reference to prevent garbage collection

        button.bind("<Button-1>", lambda event: button.config(image=photo_image_pressed))
        button.bind("<ButtonRelease-1>", lambda event: button.config(image=photo_image_unpressed))

    def set_play_pause_icons(self, icon_path_play_unpressed,
                             icon_path_pause_pressed):
        def on_button_click(event=None):
            self.is_playing = not self.is_playing
            if self.is_playing:
                self.play_pause_button.config(image=photo_image_pause_pressed)
                self.play_pause_button_tooltip.update_tooltip_text(text="Stop")
                # Add your logic for play button clicked
                print("Play button clicked")
                DrawingCanvas.bubble_sort()
            else:
                self.play_pause_button.config(image=photo_image_play_unpressed)
                self.play_pause_button_tooltip.update_tooltip_text(text="Sort")
                # Add your logic for pause button clicked
                print("Pause button clicked")

        icon_image_play_unpressed = Image.open(icon_path_play_unpressed)
        icon_image_play_unpressed = icon_image_play_unpressed.resize((30, 30))
        photo_image_play_unpressed = ImageTk.PhotoImage(icon_image_play_unpressed)

        icon_image_pause_pressed = Image.open(icon_path_pause_pressed)
        icon_image_pause_pressed = icon_image_pause_pressed.resize((30, 30))
        photo_image_pause_pressed = ImageTk.PhotoImage(icon_image_pause_pressed)

        self.play_pause_button.config(image=photo_image_play_unpressed)
        self.play_pause_button.image = photo_image_play_unpressed

        self.play_pause_button.bind("<Button-1>", on_button_click)
