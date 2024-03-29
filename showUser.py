import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
from PIL import Image, ImageTk
import sqlite3
import main

class ShowUser(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def runMainFile():
            self.withdraw()
            main.MainPage()

        self.title("Show Contacts")
        self.window_theme = ttk.Style(theme='darkly')
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        # Create the "Back" button directly on the Toplevel window
        self.back_button = ttk.Button(
            self, text="Back", command=runMainFile, style="danger.TButton"
        )
        self.back_button.pack(side="bottom", padx=50, pady=50)

        self.canvas = tk.Canvas(self, width=screen_width, height=screen_height, bg='black')
        self.canvas.pack()

        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM users")
            records = c.fetchall()

        y = 10  # Initial y-coordinate for images and text
        self.image_references = []  # Store references to PhotoImage objects

        # Create headers
        self.canvas.create_text(10, y, anchor='nw', text="Image", fill='white')
        self.canvas.create_text(70, y, anchor='nw', text="Name", fill='white')
        self.canvas.create_text(200, y, anchor='nw', text="Email", fill='white')
        self.canvas.create_text(330, y, anchor='nw', text="Number", fill='white')

        y += 30  # Move the y-coordinate for the next image and text

        for record in records:
            name, email, number, image = record

            try:
                profile_picture = Image.open(image)
                profile_picture = profile_picture.resize((50, 50))
                photo_image = ImageTk.PhotoImage(profile_picture)
                self.image_references.append(photo_image)

            except Exception as e:
                print(f"Error loading image for {name}: {e}")
                self.image_references.append(None)

            if self.image_references[-1]:  # Check if the image was successfully loaded
                self.canvas.create_image(10, y, anchor='nw', image=self.image_references[-1])

            self.canvas.create_text(70, y, anchor='nw', text=name, fill='white')
            self.canvas.create_text(200, y, anchor='nw', text=email, fill='white')
            self.canvas.create_text(330, y, anchor='nw', text=number, fill='white')

            y += 60  # Move the y-coordinate for the next image and text

# Example usage
if __name__ == "__main__":
    app = ShowUser()
    app.mainloop()
