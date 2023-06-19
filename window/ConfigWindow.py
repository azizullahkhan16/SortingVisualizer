import tkinter as tk
from tkinter import ttk


class ConfigWindow(tk.Toplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("Configuration")
        self.configure(bg="#f0f0f0")
        self.geometry("400x340")
        self.resizable(False, False)
        self.transient(master)  # Set as transient window to disable main window interaction
        self.grab_set()  # Grab focus to this window

        # Set window icon
        icon_image = tk.PhotoImage(file="C:/Users/user/PycharmProjects/SortingVisualizer/list.png")
        self.iconphoto(False, icon_image)

        # Center the window on the screen
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - 400) // 2
        y = (screen_height - 340) // 2
        self.geometry(f"+{x}+{y}")

        # Frame to contain the widgets
        frame = tk.Frame(self, bg="#f0f0f0")
        frame.pack(expand=True, padx=40, pady=40)

        # Slider for choosing the number of blocks
        blocks_label = tk.Label(frame, text="Number of Blocks:", bg="#f0f0f0", font=("Arial", 12))
        blocks_label.pack(pady=10)

        self.blocks_scale = tk.Scale(frame, from_=5, to=25, orient=tk.HORIZONTAL, length=300, showvalue=False,
                                     tickinterval=5, command=self.update_blocks_label)
        self.blocks_scale.set(10)  # Default value
        self.blocks_scale.pack()

        blocks_frame = tk.Frame(frame, bg="#f0f0f0")
        blocks_frame.pack(pady=10)

        blocks_label = tk.Label(blocks_frame, text="Blocks: ", bg="#f0f0f0", font=("Arial", 12))
        blocks_label.pack(side=tk.LEFT)

        self.blocks_selected_label = tk.Label(blocks_frame, text="10", bg="#ffffff", fg="#000000",
                                              font=("Arial", 12, "bold"), relief="solid", width=5, padx=5, pady=2)
        self.blocks_selected_label.pack(side=tk.LEFT)

        # Dropdown menu for selecting sorting algorithm
        sort_label = tk.Label(frame, text="Sorting Algorithm:", bg="#f0f0f0", font=("Arial", 12))
        sort_label.pack(pady=10)

        sorting_algorithms = ["Bubble Sort", "Merge Sort", "Quick Sort", "Insertion Sort", "Counting Sort",
                              "Selection Sort"]
        self.sort_var = tk.StringVar(value="Bubble Sort")
        self.sort_dropdown = ttk.Combobox(frame, textvariable=self.sort_var, values=sorting_algorithms,
                                          state="readonly", font=("Arial", 12))
        self.sort_dropdown.pack()

        # Button to apply the configuration
        apply_button = tk.Button(frame, text="Apply", command=self.apply_configuration,
                                 font=("Arial", 12), padx=20, pady=10, height=2)
        apply_button.pack(pady=(20, 10))

    def update_blocks_label(self, event=None):
        num_blocks = self.blocks_scale.get()
        self.blocks_selected_label.config(text=num_blocks)

    def apply_configuration(self):
        self.destroy()


