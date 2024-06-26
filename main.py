import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time
from datetime import datetime, timedelta
import threading
import webbrowser
class AlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Alarm App")

        #setting up the widget
        self.alarm_widget_setter(root)
        self.timer_widget_setter(root)
        self.url_widget_setter(root)
        
        #showing the current time
        self.current_time_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.current_time_label.pack(pady=10)

        #showing the log
        self.alarm_listbox = tk.Listbox(root, font=("Helvetica", 14), width=50)
        self.alarm_listbox.pack(pady = 10)


        self.update_time()
        self.alarms = []
        self.alarm_time = None
        self.url = None

    def alarm_widget_setter(self, root):
        self.label = tk.Label(root, text="Set Alarm Time (HH:MM)", font=("Helvetica", 14))
        self.label.pack(pady=20)

        #setting a time
        self.time_entry = tk.Entry(root, font=("Helvetica", 14), width=10)
        self.time_entry.pack(pady=10)
        self.set_button = tk.Button(root, text="Set Alarm", font=("Helvetica", 14), command=self.set_alarm)
        self.set_button.pack(pady=20)

    def timer_widget_setter(self, root):
        #or set timer
        self.label = tk.Label(root, text="Set Timer (minutes)", font=("Helvetica", 14))
        self.label.pack(pady=20)

        #setting a time
        self.timer_entry = tk.Entry(root, font=("Helvetica", 14), width=10)
        self.timer_entry.pack(pady=10)
        self.set_button = tk.Button(root, text="Set Timer", font=("Helvetica", 14), command=self.set_timer)
        self.set_button.pack(pady=20)

    def url_widget_setter(self, root):
        #setting an URL like
        self.url_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
        self.url_entry.pack(pady=10)
        self.label_url = tk.Button(root, text="Set URL", font=("Helvetica", 14), command= self.set_url)
        self.label_url.pack(pady=10)


    def set_url(self):
        self.url = self.url_entry.get()
        messagebox.showinfo("URL Set", f"URL set for {self.url}")

    def update_alarm_listbox(self):
        self.alarm_listbox.delete(0, tk.END)
        for alarm_time, video_url in self.alarms:
            self.alarm_listbox.insert(tk.END, f"Alarm at {alarm_time} - Video URL: {video_url}")

    def set_timer(self):
        try:
            minutes = int(self.timer_entry.get())
            alarm_time = (datetime.now() + timedelta(minutes=minutes)).time()
            alarm_time = alarm_time.strftime("%H:%M")
            self.alarm_set(alarm_time)
            messagebox.showinfo("Timer Set", f"Alarm set for {alarm_time} with video {self.url} in {minutes} minutes")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of minutes")



    def set_alarm(self):
        alarm_time = self.time_entry.get()
        if self.url == None:
            messagebox.showerror("Invalid Input", "Please enter your URL")
            return
        self.alarm_set(alarm_time)

    def alarm_set(self, alarm_time):
        try:
            # Check if the entered time is in the correct format
            self.alarm_time = alarm_time
            video_url = self.url
            if video_url == None:
                messagebox.showerror("Invalid Input", "Please enter your URL")
                return
            self.alarms.append((alarm_time, video_url))
            self.update_alarm_listbox()
            self.check_alarm()
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format.")
    def check_alarm(self):
        current_time = datetime.now().time().replace(second=0, microsecond=0).strftime("%H:%M")
        print(self.alarm_time)
        print(current_time)
        print(self.alarm_time == current_time)
        if self.alarm_time == current_time and self.url:
            self.alarm_time = None  # Reset the alarm
            self.show_alarm_window()
        else:
            self.root.after(1000, self.check_alarm)  # Continue checking every second

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.current_time_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_time)  # Update the time every minute

    def show_alarm_window(self):
        # Create a new window
        webbrowser.open_new(self.url)



if __name__ == "__main__":
    window = tk.Tk()
    app = AlarmApp(window)
    window.mainloop()


