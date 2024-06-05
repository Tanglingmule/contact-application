import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
from PIL import Image, ImageTk
import sqlite3
import main


class UpdateUser(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        def runMainFile():
            self.withdraw()
            main.MainPage()

        def open_edit_window():
            selected = self.tree.focus()
            values = self.tree.item(selected, 'values')
            name = values[0]
            email = values[1]
            number = values[2]

            # Create an EditUserDetails window
            edit_window = tk.Toplevel(self)
            edit_window.title("Edit Contact Details")
            edit_window.geometry("500x500")

            name_label = ttk.Label(edit_window, text="Name:")
            email_label = ttk.Label(edit_window, text="Email:")
            number_label = ttk.Label(edit_window, text="Number:")

            name_var = tk.StringVar(value=name)
            email_var = tk.StringVar(value=email)
            number_var = tk.StringVar(value=number)

            name_entry = ttk.Entry(edit_window, textvariable=name_var)
            email_entry = ttk.Entry(edit_window, textvariable=email_var)
            number_entry = ttk.Entry(edit_window, textvariable=number_var)

            save_button = ttk.Button(
                edit_window, text="Save", command=lambda: save_changes(name, name_var.get(), email_var.get(), number_var.get()), bootstyle="success"
            )
            cancel_button = ttk.Button(edit_window, text="Cancel", command=edit_window.destroy, bootstyle="danger")

            name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
            email_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
            number_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")

            name_entry.grid(row=0, column=1, padx=10, pady=5)
            email_entry.grid(row=1, column=1, padx=10, pady=5)
            number_entry.grid(row=2, column=1, padx=10, pady=5)

            save_button.grid(row=3, column=0, columnspan=2, pady=10)
            cancel_button.grid(row=3, column=3, pady=10)

        def save_changes(old_name, new_name, new_email, new_number):
            # Update the record in the database
            if new_name.strip() != "" and new_email.strip() != "" and new_number.strip() != "":
                with sqlite3.connect("database.db") as conn:
                    c = conn.cursor()
                    c.execute("UPDATE users SET name=?, email=?, number=? WHERE name=?", (new_name, new_email, new_number, old_name))
            else:
                Messagebox.showinfo("Error", "Please fill in all the fields.")

            # Update the Treeview
            selected = self.tree.focus()
            self.tree.item(selected, values=(new_name, new_email, new_number))

        self.title("Update Contacts")
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

        self.edit_button = ttk.Button(self, text="Edit Contact", command=open_edit_window, style="primary.TButton")
        self.back_button = ttk.Button(self, text="Back", command=runMainFile, style="danger.TButton")

        # Pack the widgets
        self.edit_button.pack(pady=10)
        self.back_button.pack(pady=10)


if __name__ == "__main__":
    root = tk.Tk()
    UpdateUser(root)
    root.mainloop()