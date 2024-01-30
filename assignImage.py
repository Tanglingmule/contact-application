import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import tkinter.messagebox as messagebox
from PIL import Image
import sqlite3

class AssignImage(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Assign Image")
        self.window_theme = ttk.Style(theme='darkly')
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self.image_name = tk.StringVar()

        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM users")
            records = c.fetchall()


        self.tree = ttk.Treeview(self, columns=("Name", "Email", "Number"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Number", text="Number")
        self.tree.column("Name", width=400)
        self.tree.column("Email", width=400)
        self.tree.column("Number", width=400)

        # Insert records into the Treeview
        for record in records:
            self.tree.insert("", "end", values=record)
        
        
        self.assign_button = ttk.Button(self, text="Assign Image", command=self.assign)




        self.image_name_label = ttk.Label(self, text="Image Name:")
        self.image_name_entry = ttk.Entry(self, textvariable=self.image_name)

        # Pack the widgets
        self.tree.pack()
        self.assign_button.pack()
        self.image_name_label.pack()
        self.image_name_entry.pack()

        def assign(self):
            selected = self.tree.focus()
            values = self.tree.item(selected, 'values')
            name = values[0]
            image_name = self.image_name.get()
            with sqlite3.connect("database.db") as conn:
                c = conn.cursor()
                c.execute("UPDATE users SET image_name=? WHERE name=?", (image_name, name))
            




        