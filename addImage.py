import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import tkinter.messagebox as messagebox
from PIL import Image
import urllib.request
import main
#from runFiles import runMainFile


class AddImage(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Add Image")
        self.window_theme = ttk.Style(theme='darkly')
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")
        
        def runMainFile(self):
            self.withdraw()
            main.MainPage()

        

        self.image = tk.StringVar()
        self.image_local = tk.StringVar()
        self.image_name = tk.StringVar()

        self.image_label = ttk.Label(self, text="Image Link:")
        self.image_entry = ttk.Entry(self, textvariable=self.image)

        self.image_local_label = ttk.Label (self, text="Or Use A Local Image Path:")
        self.image_local_entry = ttk.Entry(self, textvariable=self.image_local)

        self.image_name_label = ttk.Label(self, text="Image Name:")
        self.image_name_entry = ttk.Entry(self, textvariable=self.image_name)

        self.add_button = ttk.Button(self, text="Add Image", command=self.imageGet, bootstyle="success")
        self.back_button= ttk.Button(self, text="Back", command=lambda:runMainFile(self), bootstyle="danger")

        # Pack the widgets
        self.image_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.image_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        self.image_local_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.image_local_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        self.image_name_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.image_name_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=20)
        self.back_button.grid(row=3, column=2, columnspan=2, pady=20)

    def imageGet(self):
        if self.image_name.get() == "":
            Messagebox.show_error(title="Error", message="Please enter image name")
            return
        elif self.image.get() == "" and self.image_local_entry.get() == "":
            Messagebox.show_error(title="Error", message="Please enter image link or path")
            return

        if self.image_entry.get() != "":
            url = self.image.get()
            urllib.request.urlretrieve(url, f'user_images/{self.image_name.get()}.jpg')
            Messagebox.show_info(title="Success", message=f"Image ({self.image_name.get()}) added successfully")
        elif self.image_local_entry.get() != "":
            path = self.image_local_entry.get()
            img = Image.open(path)
            img.save(f'user_images/{self.image_name.get()}.jpg')
            Messagebox.show_info(title="Success", message=f"Image ({self.image_name.get()}) added successfully")
