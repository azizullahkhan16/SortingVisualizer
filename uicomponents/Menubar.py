import os
import tkinter as tk
from PIL import Image, ImageTk

import animation.Animation
from animation import Animation
from uicomponents import AnalysisSpace
from uicomponents.DrawingCanvas import DrawingCanvas
from uicomponents.ToolTip import Tooltip
from window.ConfigWindow import ConfigWindow


class MenuBar(tk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.photo_image_pause_pressed = None
        self.photo_image_play_unpressed = None
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

        self.shuffle_button = tk.Button(
            self,
            width=40,
            height=40,
            bd=0,
            highlightthickness=0,
            bg="#373737",
            activebackground="#373737"  # Set active-background to the same color as the background
        )
        self.shuffle_button.pack(side=tk.TOP, pady=5)
        self.shuffle_button.config(command=self.on_shuffle_button_click)
        Tooltip(self.shuffle_button, "Shuffle")

        # Get the absolute path of the script file
        script_dir = os.path.dirname(os.path.abspath(__file__))

        # Set custom icons for the buttons
        self.set_icon(
            self.config_button,
            os.path.join(script_dir, "res/configUnpressed.png"),
            os.path.join(script_dir, "res/configPressed.png")
        )
        self.set_play_pause_icons(
            os.path.join(script_dir, "res/playUnpressed.png"),
            os.path.join(script_dir, "res/pausePressed.png")
        )
        self.set_icon(
            self.shuffle_button,
            os.path.join(script_dir, "res/shuffleUnpressed.png"),
            os.path.join(script_dir, "res/shufflePressed.png")
        )

    def on_config_button_click(self):
        # Add your config logic here
        config_window = ConfigWindow(self)
        print("Config button clicked")

    def on_shuffle_button_click(self):
        DrawingCanvas.delete_blocks()
        DrawingCanvas.create_blocks(DrawingCanvas.get_canvas(), ConfigWindow.num_blocks)

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

        def update_play_pause_button():
            if DrawingCanvas.get_is_sorted():
                self.is_playing = not self.is_playing
                self.config_button.config(state=tk.NORMAL)  # Enable the config button
                self.shuffle_button.config(state=tk.NORMAL)  # Enable the shuffle button
                self.play_pause_button.config(image=self.photo_image_play_unpressed)
                self.play_pause_button_tooltip.update_tooltip_text(text="Sort")

        def on_button_click(event=None):
            self.is_playing = not self.is_playing
            if self.is_playing:
                self.play_pause_button.config(image=self.photo_image_pause_pressed)
                self.play_pause_button_tooltip.update_tooltip_text(text="Stop")

                self.config_button.config(state=tk.DISABLED)  # disable the config button
                self.shuffle_button.config(state=tk.DISABLED)  # disable the shuffle button

                # Add your logic for play button clicked
                print("Play button clicked")
                if DrawingCanvas.get_animation_paused() and not DrawingCanvas.get_is_sorted():
                    DrawingCanvas.set_animation_paused(False)
                else:
                    if not DrawingCanvas.get_is_sorted():
                        match ConfigWindow.sort_algo:
                            case "Merge Sort":
                                DrawingCanvas.merge_sort()
                            case "Quick Sort":
                                DrawingCanvas.quick_sort()
                            case "Heap Sort":
                                DrawingCanvas.heap_sort()
                            case "Radix Sort":
                                DrawingCanvas.radix_sort()
                            case "Tim Sort":
                                DrawingCanvas.tim_sort()
                            case "Counting Sort":
                                DrawingCanvas.counting_sort()
                            case "Shell Sort":
                                DrawingCanvas.shell_sort()
                            case "Insertion Sort":
                                DrawingCanvas.insertion_sort()
                            case "Selection Sort":
                                DrawingCanvas.selection_sort()
                            case "Bubble Sort":
                                DrawingCanvas.bubble_sort()
                            case "Tree Sort":
                                DrawingCanvas.tree_sort()
                    update_play_pause_button()

            else:
                self.play_pause_button.config(image=self.photo_image_play_unpressed)
                self.play_pause_button_tooltip.update_tooltip_text(text="Sort")

                self.config_button.config(state=tk.NORMAL)  # Enable the config button
                self.shuffle_button.config(state=tk.NORMAL)  # Enable the shuffle button

                # Add your logic for pause button clicked
                print("Pause button clicked")
                DrawingCanvas.set_animation_paused(True)

        icon_image_play_unpressed = Image.open(icon_path_play_unpressed)
        icon_image_play_unpressed = icon_image_play_unpressed.resize((30, 30))
        self.photo_image_play_unpressed = ImageTk.PhotoImage(icon_image_play_unpressed)

        icon_image_pause_pressed = Image.open(icon_path_pause_pressed)
        icon_image_pause_pressed = icon_image_pause_pressed.resize((30, 30))
        self.photo_image_pause_pressed = ImageTk.PhotoImage(icon_image_pause_pressed)

        self.play_pause_button.config(image=self.photo_image_play_unpressed)
        self.play_pause_button.image = self.photo_image_play_unpressed
        self.play_pause_button.bind("<Button-1>", on_button_click)

        # Start the periodic update of the play/pause button state
        update_play_pause_button()

    def pause_on_minimize(self, event):
        if not DrawingCanvas.get_animation_paused() and not DrawingCanvas.get_is_sorted():
            self.is_playing = not self.is_playing

            self.play_pause_button.config(image=self.photo_image_play_unpressed)
            self.play_pause_button_tooltip.update_tooltip_text(text="Sort")

            self.config_button.config(state=tk.NORMAL)  # Enable the config button
            self.shuffle_button.config(state=tk.NORMAL)  # Enable the shuffle button

            # Add your logic for pause button clicked
            print("Pause button clicked")
            DrawingCanvas.set_animation_paused(True)

