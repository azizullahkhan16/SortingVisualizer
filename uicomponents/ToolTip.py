import tkinter as tk


class Tooltip:
    def __init__(self, widget, text, bg="#ffffff", fg="#000000"):
        self.widget = widget
        self.text = text
        self.bg = bg
        self.fg = fg
        self.tooltip = None
        self.widget.bind("<Enter>", self.show_tooltip)
        self.widget.bind("<Leave>", self.hide_tooltip)

    def show_tooltip(self, event=None):
        x, y, _, _ = self.widget.bbox("insert")
        x += self.widget.winfo_rootx() + 25
        y += self.widget.winfo_rooty() + 25

        self.tooltip = tk.Toplevel(self.widget)
        self.tooltip.wm_overrideredirect(True)
        self.tooltip.wm_geometry(f"+{x}+{y}")

        self.label = tk.Label(
            self.tooltip,
            text=self.text,
            background=self.bg,
            foreground=self.fg,
            relief="solid",
            borderwidth=1,
            font=("Arial", 10)
        )
        self.label.pack()

    def hide_tooltip(self, event=None):
        if self.tooltip:
            self.tooltip.destroy()
            self.tooltip = None

    def update_tooltip_text(self, text):
        self.text = text
        if self.tooltip:
            self.label.config(text=self.text)

