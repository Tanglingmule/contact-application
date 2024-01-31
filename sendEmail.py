import tkinter as tk
from ttkbootstrap import ttk
from ttkbootstrap.constants import *
from ttkbootstrap.dialogs import *
import tkinter.messagebox as messagebox
import sqlite3
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail(tk.Toplevel):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Send Email")
        self.window_theme = ttk.Style(theme='darkly')
        self.resizable(False, False)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}")

        self.sender_email = tk.StringVar()
        self.recipient_email = tk.StringVar()
        self.subject = tk.StringVar()
        self.message = tk.StringVar()

        self.sender_email_label = ttk.Label(self, text="Sender Email:")
        self.sender_email_entry = ttk.Entry(self, textvariable=self.sender_email)
        self.recipient_email_label = ttk.Label(self, text="Recipient Email:")
        self.recipient_email_entry = ttk.Entry(self, textvariable=self.recipient_email)
        self.subject_label = ttk.Label(self, text="Subject:")
        self.subject_entry = ttk.Entry(self, textvariable=self.subject)
        self.message_label = ttk.Label(self, text="Message:")
        self.message_entry = ttk.Entry(self, textvariable=self.message)

        self.send_button = ttk.Button(self, text="Send Email", command=self.send_email, bootstyle="success")

        # Pack the widgets
        self.sender_email_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.sender_email_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        self.recipient_email_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.E)
        self.recipient_email_entry.grid(row=0, column=1, padx=10, pady=10, sticky=tk.W)
        self.subject_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)
        self.subject_entry.grid(row=1, column=1, padx=10, pady=10, sticky=tk.W)
        self.message_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.E)
        self.message_entry.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)
        self.send_button.grid(row=3, column=0, columnspan=2, pady=20)

    def send_email(self):
        if self.email.get() == "" or self.subject.get() == "" or self.message.get() == "":
            messagebox.showerror(title="Error", message="Please fill in all fields")
        else:
            with sqlite3.connect("database.db") as conn:
                c = conn.cursor()
                c.execute("SELECT * FROM users WHERE email=?", (self.email.get(),))
                if c.fetchone() is None:
                    messagebox.showerror(title="Error", message="Email not found")
                    return
                else:
                    with sqlite3.connect("database.db") as conn:
                        c = conn.cursor()   
                        c.execute("SELECT * FROM users WHERE email=?", (self.recipient_email.get(),))
                        if c.fetchone() is None:
                            messagebox.showerror(title="Error", message="Recipient email not found")
                            return
                        else:
                            # Set up the SMTP server
                            s = smtplib.SMTP(host='smtp.gmail.com', port=587)
                            s.starttls()
                            s.login(self.sender_email.get(), 'your-password')

                            # Create the email
                            msg = MIMEMultipart()
                            msg['From'] = self.sender_email.get()
                            msg['To'] = self.recipient_email.get()
                            msg['Subject'] = self.subject.get()
                            msg.attach(MIMEText(self.message.get(), 'plain'))

                            # Send the email
                            s.send_message(msg)
                            s.quit()

                            messagebox.showinfo(title="Success", message="Email sent successfully")