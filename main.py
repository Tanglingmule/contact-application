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



class MainPage(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from runFiles import runAddContactFile, runShowContactsFile, runDeleteContactFile, runAddImageFile, runAssignImageFile, runSendEmailFile
        self.title("Main Page")
        self.window_theme=ttk.Style(theme='darkly')
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        

        self.label = ttk.Label(self, text="Welcome to the Contacts App!", font=("Helvetica", 24))
        self.label.pack(pady=20)
       
        self.button = ttk.Button(
            self, text="Add Contact", command= lambda:runAddContactFile(self), bootstyle="success"
        )
        self.button.pack(pady=20)

        self.button = ttk.Button(
            self, text="Show Contacts", command=lambda:runShowContactsFile(self),bootstyle="success"
        )
        self.button.pack(pady=20, )

        

        self.button = ttk.Button(
            self, text="Add Image", command= lambda:runAddImageFile(self), bootstyle="success"
        )
        self.button.pack(pady=20)

        self.button = ttk.Button(
            self, text="Assign Image To Contact", command= lambda:runAssignImageFile(self), bootstyle="success"
        )
        self.button.pack ( pady=20, )

        self.button = ttk.Button(
            self, text="Delete Contact", command= lambda: runDeleteContactFile(self), bootstyle="danger"
        )
        self.button.pack ( pady=20)

        self.button = ttk.Button(
            self, text="Exit", command=self.destroy, bootstyle="danger")
        self.button.pack ( pady=20, )


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the self.back_button = ttk.Button(self, text="Back", command=runMainFile, bootstyle="danger")main window
    app = MainPage()  # Pass the root window to MainPage
    app.mainloop()  # Start the application's main loop


    
