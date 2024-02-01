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

        self.send_button = ttk.Button(self, text="Send Email", command= self.send_email(self), bootstyle="success")

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
                sender = self.sender_email.get()
                recipient = self.recipient_email.get()
                subject = self.subject.get()
                message = self.message.get()
                

                with sqlite3.connect("database.db") as conn:
                    c = conn.cursor()
                    c.execute("SELECT * FROM users WHERE email=?", (recipient,))
                    records = c.fetchall()

                if len(records) == 0:
                        messagebox.showerror(title="Error", message="Recipient email not found")
                else:
                        message = f"Subject: {subject}\n\n{message}"
                        try:
                            smtp_obj = smtplib.SMTP('localhost')
                            smtp_obj.sendmail(sender, recipient, message)
                            messagebox.showinfo(title="Success", message="Email sent successfully!")
                        except:
                            messagebox.showerror(title="Error", message="Failed to send email")


if __name__ == "__main__":
    app = SendEmail()
    app.mainloop()
