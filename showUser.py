import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
from PIL import Image, ImageTk
import sqlite3

class ShowUser(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Show Contacts")
        self.window_theme = ttk.Style(theme='darkly')
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM users")
            records = c.fetchall()

        self.canvas = tk.Canvas(self, width=screen_width, height=screen_width, bg='black')
        self.canvas.pack()

        y = 10  # Initial y-coordinate for images and text

        # Create headers
        self.canvas.create_text(10, y, anchor='nw', text="Image", fill='white')
        self.canvas.create_text(70, y, anchor='nw', text="Name", fill='white')
        self.canvas.create_text(200, y, anchor='nw', text="Email", fill='white')
        self.canvas.create_text(330, y, anchor='nw', text="Number", fill='white')

        y += 30  # Move the y-coordinate for the next image and text

        for record in records:
            name, email, number, image = record

            # Use try-except block for loading images
            try:
                profile_picture = Image.open(image)
                profile_picture = profile_picture.resize((50, 50))
                profile_picture = ImageTk.PhotoImage(profile_picture)

            except Exception as e:
                # Handle image loading errors gracefully
                print(f"Error loading image for {name}: {e}")
                profile_picture = None

            if profile_picture:
                self.canvas.create_image(10, y, anchor='nw', image=profile_picture)
                self.canvas.image = profile_picture  # Keep a reference to prevent garbage collection

            self.canvas.create_text(70, y, anchor='nw', text=name, fill='white')
            self.canvas.create_text(200, y, anchor='nw', text=email, fill='white')
            self.canvas.create_text(330, y, anchor='nw', text=number, fill='white')

            y += 60  # Move the y-coordinate for the next image and text
