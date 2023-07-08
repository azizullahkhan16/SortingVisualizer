import os
import tkinter as tk
from tkinter import ttk
from uicomponents.DrawingCanvas import DrawingCanvas


class ConfigWindow(tk.Toplevel):
    num_blocks = 10  # Class variable to store the number of blocks
    sort_algo = "Merge Sort"

    def __init__(self, master):
        super().__init__(master)
        self.title("Configuration")
        self.configure(bg="#f5f6f8")
        self.geometry("400x340")
        self.resizable(False, False)
        self.transient(master)  # Set as transient window to disable main window interaction
        self.grab_set()  # Grab focus to this window

        # Get the absolute path of the script file
        script_dir = os.path.dirname(os.path.abspath(__file__))

        icon_image = tk.PhotoImage(file=os.path.join(script_dir, "res/list.png"))
        self.iconphoto(False, icon_image)

        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 340) // 2
        self.geometry(f"+{x}+{y}")

        # Frame to contain the widgets
        frame = tk.Frame(self, bg="#f5f6f8")
        frame.pack(expand=True, padx=40, pady=20)

        self.blocks_scale = tk.Scale(frame, from_=5, to=25, orient=tk.HORIZONTAL, length=300, showvalue=False,
                                     tickinterval=5, command=self.update_blocks_label)
        self.blocks_scale.set(10)  # Default value
        self.blocks_scale.pack(pady=(0, 20))  # Increased vertical padding

        blocks_frame = tk.Frame(frame, bg="#f5f6f8", width=350)  # Adjusted width
        blocks_frame.pack()

        blocks_label = tk.Label(blocks_frame, text="Blocks:", bg="#f5f6f8", font=("Arial", 12, "bold"))
        blocks_label.pack(side=tk.LEFT, padx=(0, 10), pady=(0, 10))  # Increased vertical padding

        self.blocks_selected_label = tk.Label(blocks_frame, text="10", bg="#ffffff", fg="#000000",
                                              font=("Arial", 12, "bold"), relief="solid", width=5, padx=5, pady=2)
        self.blocks_selected_label.pack(side=tk.LEFT, pady=(0, 10))  # Increased vertical padding

        sorting_algorithms = ["Merge Sort", "Quick Sort", "Heap Sort", "Radix Sort", "Tim Sort", "Counting Sort",
                              "Shell Sort", "Insertion Sort", "Selection Sort", "Bubble Sort", "Tree Sort"]
        self.sort_var = tk.StringVar(value="Merge Sort")
        self.sort_dropdown = ttk.Combobox(frame, textvariable=self.sort_var, values=sorting_algorithms,
                                          state="readonly", font=("Arial", 12), width=20)  # Adjusted width
        # Adjust the combobox height
        self.sort_dropdown.configure(height=7)  # Adjust the height as desired
        self.sort_dropdown.pack(pady=(20, 20))  # Increased vertical padding

        # Button to apply the configuration
        apply_button = tk.Button(frame, text="Apply", command=self.apply_configuration,
                                 font=("Arial", 12), padx=10, pady=5, width=10, height=1)
        apply_button.pack(pady=(20, 0))

    def update_blocks_label(self, event=None):
        num_blocks = self.blocks_scale.get()
        self.blocks_selected_label.config(text=num_blocks)
        ConfigWindow.num_blocks = num_blocks  # Update the class variable

    def apply_configuration(self):
        from uicomponents.AnalysisSpace import AnalysisSpace
        DrawingCanvas.delete_blocks()
        DrawingCanvas.create_blocks(DrawingCanvas.get_canvas(), ConfigWindow.num_blocks)
        ConfigWindow.sort_algo = self.sort_var.get()
        self.destroy()
        AnalysisSpace.update_graph()
        AnalysisSpace.paint()



