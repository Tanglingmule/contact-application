import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import sqlite3
import tkinter.messagebox as messagebox

class AddContact(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Add Contact")
        self.window_theme=ttk.Style(theme='darkly')
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self.name = tk.StringVar()
        self.email = tk.StringVar()
        self.number = tk.StringVar()

        self.name_label = ttk.Label(self, text="Name:")
        self.name_entry = ttk.Entry(self, textvariable=self.name)
        self.email_label = ttk.Label(self, text="Email:")
        self.email_entry = ttk.Entry(self, textvariable=self.email)
        self.number_label = ttk.Label(self, text="Number:")
        self.number_entry = ttk.Entry(self, textvariable=self.number)

        self.add_button = ttk.Button( self, text="Add Contact", command=self.validation, bootstyle="success")

         # Pack the widgets
        self.name_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.name_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        self.email_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.email_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        self.number_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.number_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=20)


    def validation(self):
        if self.name.get() == "" or self.email.get() == "" or self.number.get() == "":
            messagebox.showerror(title="Error", message="Please fill in all fields")
        else:
            with sqlite3.connect("database.db") as conn:
                c = conn.cursor()
                c.execute(
                    "INSERT INTO users VALUES(:name, :email, :number)",
                    {
                        "name": self.name.get(),
                        "email": self.email.get(),
                        "number": self.number.get(),
                    },
                )