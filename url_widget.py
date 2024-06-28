import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class UrlWidget:
    def __init__(self, app):
        self.app = app
        self.root = app.root

        self.url_entry = tk.Entry(self.root, font=("Helvetica", 14), width=30)
        self.url_entry.pack(pady=10)

        self.label_url = tk.Button(self.root, text="Set URL", font=("Helvetica", 14), command=self.set_url)
        self.label_url.pack(pady=10)

        self.url = None


    def set_url(self):
        self.url = self.url_entry.get()
        messagebox.showinfo("URL Set", f"URL set for {self.url}")
