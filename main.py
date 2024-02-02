import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import sqlite3
from PIL import Image, ImageTk  # Import PIL modules
import addUser
import showUser
import deleteUser
import addImage
import assignImage

with sqlite3.connect("database.db") as conn:
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT, number INTEGER, image TEXT)")
    conn.commit()

class MainPage(tk.Toplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from runFiles import runAddContactFile, runShowContactsFile, runDeleteContactFile, runAddImageFile, runAssignImageFile, runSendEmailFile, runUpdateUserFile
        self.title("Main Page")
        self.window_theme = ttk.Style(theme='darkly')
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        # Load and display background image
        background_image = Image.open("program_images/background.png")
        background_photo = ImageTk.PhotoImage(background_image)
        background_label = ttk.Label(self, image=background_photo)
        background_label.image = background_photo
        background_label.place(relwidth=1, relheight=1)

        # Centered Header
        header_frame = ttk.Frame(self)
        header_frame.pack(side=tk.TOP, pady=50)

       # Left buttons
        add_contact_button = ttk.Button(self, text="Add Contact", command=lambda: runAddContactFile(self), bootstyle="success")
        add_contact_button.pack(side=tk.LEFT, ipady=20, ipadx=20, pady=20, padx=20)  # Set internal and external padding

        add_image_button = ttk.Button(self, text="Add Image", command=lambda: runAddImageFile(self), bootstyle="success")
        add_image_button.pack(side=tk.LEFT, ipady=20, ipadx=20, pady=20, padx=20)  # Set internal and external padding

        send_email_button = ttk.Button(self, text="Send Email to Contact", command=lambda: runSendEmailFile(self), bootstyle="success")
        send_email_button.pack(side=tk.LEFT, ipady=20, ipadx=20, pady=20, padx=20)  # Set internal and external padding

        # Right buttons
        show_contacts_button = ttk.Button(self, text="Show Contacts", command=lambda: runShowContactsFile(self), bootstyle="success")
        show_contacts_button.pack(side=tk.RIGHT, ipady=20, ipadx=20, pady=20, padx=20)  # Set internal and external padding

        assign_image_button = ttk.Button(self, text="Assign Image To Contact", command=lambda: runAssignImageFile(self), bootstyle="success")
        assign_image_button.pack(side=tk.RIGHT, ipady=20, ipadx=20, pady=20, padx=20)  # Set internal and external padding

        update_user_button = ttk.Button(self, text="Update User Details", command=lambda: runUpdateUserFile(self), bootstyle="success")
        update_user_button.pack(side=tk.RIGHT, ipady=20, ipadx=20, pady=20, padx=20)  # Set internal and external padding

        delete_contact_button = ttk.Button(self, text="Delete Contact", command=lambda: runDeleteContactFile(self), bootstyle="danger")
        delete_contact_button.pack(side=tk.RIGHT, ipady=20, ipadx=20, pady=100, padx=20)  # Set internal and external padding



        # Bottom frame for the Exit Button
        bottom_frame = ttk.Frame(self)
        bottom_frame.pack(side=tk.BOTTOM, pady=20)

        # Exit Button
        exit_button = ttk.Button(self, text="Exit", command= lambda:exit('Program Terminated'), bootstyle="danger")
        exit_button.pack(side=tk.BOTTOM, pady=20)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = MainPage()  # Pass the root window to MainPage
    app.mainloop()  # Start the application's main loop
