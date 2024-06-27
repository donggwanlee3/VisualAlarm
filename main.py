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

        #self.alarms have list of alarms and respective time
        #self.alarmtime and self.url are placeholders
        self.alarms = []
        self.alarm_time = None
        self.url = None

        self.update_time()

    def set_default_url(self, url):
        self.url_entry.insert(0, url)


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
        self.set_default_url("https://www.google.com")


    def set_url(self):
        self.url = self.url_entry.get()
        messagebox.showinfo("URL Set", f"URL set for {self.url}")

    def update_alarm_listbox(self):
        self.alarm_listbox.delete(0, tk.END)
        #sort the alarms by the alarm time
        for alarm_time, video_url in self.alarms:
            self.alarm_listbox.insert(tk.END, f"Alarm at {alarm_time} - Video URL: {video_url}")

    #function called when you press set_timer
    def set_timer(self):
        try:
            minutes = int(self.timer_entry.get())
            alarm_time = (datetime.now() + timedelta(minutes=minutes)).time()
            alarm_time = alarm_time.strftime("%H:%M")
            if self.url == None:
                messagebox.showerror("Invalid Input", "Please enter your URL")
                return
            url = self.url
            self.alarm_set(alarm_time, url)
            messagebox.showinfo("Timer Set", f"Alarm set for {alarm_time} with video {url} in {minutes} minutes")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number of minutes")


    #function called when you press set_URL
    def set_alarm(self):
        alarm_time = self.time_entry.get()
        if self.url == None:
            messagebox.showerror("Invalid Input", "Please enter your URL")
            return
        url = self.url
        self.alarm_set(alarm_time, url)

    # append alarm_listbox an alarms
    def alarm_set(self, alarm_time, url):
        try:
            # Check if the entered time is in the correct format
            alarm_entry = f"{alarm_time} {url}"
            self.alarm_listbox.insert(tk.END, alarm_entry)
            self.alarms.append([alarm_time, url])
            self.update_alarm_listbox()
            self.check_alarm()
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format.")

    
    def check_alarm(self):
        current_time = datetime.now().time().replace(second=0, microsecond=0).strftime("%H:%M")
        for alarm in self.alarms[:]:
            alarm_time, video_url = alarm
            if alarm_time == current_time and video_url:
                self.alarms.remove(alarm)
                self.show_alarm_window(video_url)
                #pop the element
                # self.alarm_listbox.delete(i)
                break

        else:
            self.root.after(1000, self.check_alarm)  # Continue checking every second

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.current_time_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_time)  # Update the time every minute

    def show_alarm_window(self, video_url):
        # Create a new window
        webbrowser.open_new(video_url)
        self.update_alarm_listbox()



if __name__ == "__main__":
    window = tk.Tk()
    app = AlarmApp(window)
    window.mainloop()



# The on_listbox_select method is designed to handle the event when an item in the listbox is selected. Here's a breakdown of what each part of the method does:

# Explanation of on_listbox_select
# python
# Copy code
# def on_listbox_select(self, event):
#     widget = event.widget
#     selection = widget.curselection()
#     if selection:
#         self.selected_index = selection[0]
#     else:
#         self.selected_index = None
# Binding the Event:

# The on_listbox_select method is bound to the <<ListboxSelect>> event of the listbox, which means it gets called whenever an item in the listbox is selected.
# This binding is done using self.alarm_listbox.bind('<<ListboxSelect>>', self.on_listbox_select).
# Event Object:

# The event parameter is an event object that gets passed to the method automatically when the event occurs.
# It contains information about the event, including which widget triggered it.
# Get the Widget:

# widget = event.widget retrieves the widget that triggered the event. In this case, it is the listbox.
# Get the Selected Item:

# selection = widget.curselection() retrieves the current selection in the listbox.
# curselection() returns a tuple of indices of the selected items. If no item is selected, it returns an empty tuple.
# Check the Selection:

# if selection: checks if the selection is not empty (i.e., an item is selected).
# If an item is selected, self.selected_index = selection[0] stores the index of the selected item in the self.selected_index attribute.
# If no item is selected, self.selected_index = None sets self.selected_index to None.
# Summary
# This method captures the index of the selected item in the listbox and stores it in the self.selected_index attribute. This captured index can later be used to perform operations on the selected item, such as deleting it from the list. If no item is selected, self.selected_index is set to None, ensuring that the program can handle cases where no item is selected.





