import tkinter as tk
import ttkbootstrap as ttk
import sqlite3

class deleteUser(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Delete Contact")
        self.window_theme = ttk.Style(theme='darkly')
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM users")
            records = c.fetchall()

        self.tree = ttk.Treeview(self, columns=("Name", "Email", "Number"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Number", text="Number")
        self.tree.column("Name", width=200)
        self.tree.column("Email", width=200)
        self.tree.column("Number", width=200)

        # Insert records into the Treeview
        for record in records:
            self.tree.insert("", "end", values=record)

        self.tree.pack()

        self.delete_button = ttk.Button(self, text="Delete Contact", command=self.delete)

        # Pack the widgets

        self.delete_button.pack(pady=20)

    def delete(self):
        selected = self.tree.focus()
        values = self.tree.item(selected, 'values')
        name = values[0]
        with sqlite3.connect("database.db") as conn:
            c = conn.cursor()
            c.execute("DELETE FROM users WHERE name=?", (name,))
        self.tree.delete(selected)
        