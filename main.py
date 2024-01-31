import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import sqlite3
import addUser
import showUser
import deleteUser
import addImage
import assignImage




with sqlite3.connect("database.db") as conn:
    c = conn.cursor()
    c.execute(
        "CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT, number INTEGER, image TEXT)"
    )
    conn.commit()


class MainPage(ttk.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Main Page")
        self.window_theme=ttk.Style(theme='darkly')
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self.label = ttk.Label(self, text="Welcome to the Contacts App!")
        self.label.pack(pady=20)

        self.button = ttk.Button(
            self, text="Add Contact", command= addUser.AddContact, bootstyle="success"
        )
        self.button.pack(pady=20)

        self.button = ttk.Button(
            self, text="Show Contacts", command= showUser.ShowUser, bootstyle="success"
        )
        self.button.pack(pady=20)

        

        self.button = ttk.Button(
            self, text="Add Image", command= addImage.AddImage, bootstyle="success"
        )
        self.button.pack(pady=20)

        self.button = ttk.Button(
            self, text="Assign Image To Contact", command=assignImage.AssignImage, bootstyle="success"
        )
        self.button.pack(pady=20)

        self.button = ttk.Button(
            self, text="Delete Contact", command= deleteUser.deleteUser, bootstyle="danger"
        )
        self.button.pack(pady=20)

        self.button = ttk.Button(
            self, text="Exit", command=self.destroy, bootstyle="danger"
        )



if __name__ == "__main__":
    app = MainPage()
    app.mainloop()
