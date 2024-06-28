import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, timedelta
import webbrowser
from alarm_widget import AlarmWidget
from timer_widget import TimerWidget
from url_widget import UrlWidget
from log_widget import LogWidget
class AlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Visual Alarm App")
        self.root.geometry("500x800") 

        # Initialize widgets
        self.alarm_widget = AlarmWidget(self)
        self.timer_widget = TimerWidget(self)
        self.url_widget = UrlWidget(self)
        self.log_widget = LogWidget(self)
        # Show current time
        self.current_time_label = tk.Label(root, text="", font=("Helvetica", 14))
        self.current_time_label.pack(pady=10)

        self.alarms = []
        self.selected_index = None
        self.update_time()
        self.check_alarm()

    def update_time(self):
        current_time = datetime.now().strftime("%H:%M:%S")
        self.current_time_label.config(text=f"Current Time: {current_time}")
        self.root.after(1000, self.update_time)

    def check_alarm(self):
        current_time = datetime.now().strftime("%H:%M")
        for alarm in self.alarms[:]:
            alarm_time, video_url = alarm
            if alarm_time == current_time and video_url:
                self.alarms.remove(alarm)
                self.show_alarm_window(video_url)
                self.update_alarm_listbox()
                break
        else:
            self.root.after(1000, self.check_alarm)

    def show_alarm_window(self, video_url):
        webbrowser.open_new(video_url)
    def add_alarm(self, alarm_time, url):
        try:
            # Validate the entered time format
            datetime.strptime(alarm_time, "%H:%M")
        except ValueError:
            messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format.")
            return
        # Check if the entered time is in the correct format
        self.alarms.append([alarm_time, url])
        self.alarms.sort(key=lambda x: datetime.strptime(x[0], "%H:%M"))
        self.update_alarm_listbox()
        self.check_alarm()
    def update_alarm_listbox(self):
        self.log_widget.alarm_listbox.delete(0, tk.END)
        for alarm_time, video_url in self.alarms:
            self.log_widget.alarm_listbox.insert(tk.END, f"Alarm at {alarm_time} - Video URL: {video_url}")

if __name__ == "__main__":
    window = tk.Tk()
    app = AlarmApp(window)
    window.mainloop()




# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from datetime import datetime
# import time
# from datetime import datetime, timedelta
# import threading
# import webbrowser
# class AlarmApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Visual Alarm App")

#         #setting up the widget
#         self.alarm_widget_setter(root)
#         self.timer_widget_setter(root)
#         self.url_widget_setter(root)
#         self.root.geometry("500x800") 
        
#         #showing the current time
#         self.current_time_label = tk.Label(root, text="", font=("Helvetica", 14))
#         self.current_time_label.pack(pady=10)

#         #showing the log
#         self.create_widgets()

#         #self.alarms have list of alarms and respective time
#         #self.alarmtime and self.url are placeholders
#         self.alarms = []
#         self.alarm_time = None
#         self.url = None

#         self.update_time()

#     def create_widgets(self):
#         self.style = ttk.Style()
#         self.style.configure('TButton', font=('Helvetica', 12, 'bold'), padding=10, background='red', foreground='white')
#         self.delete_button = ttk.Button(self.root, text="Delete Selected Alarm", command=self.delete_selected_alarm, style='TButton')
#         self.delete_button.pack(pady=10)

#         self.alarm_listbox = tk.Listbox(self.root, font=("Helvetica", 14), width=50)
#         self.alarm_listbox.pack()
    
#         self.alarm_listbox.bind('<<ListboxSelect>>', self.on_listbox_select)
    

#     # def set_default_url(self, url):
#     #     self.url_entry.insert(0, url)


#     def alarm_widget_setter(self, root):
#         self.label = tk.Label(root, text="Set Alarm Time (HH:MM)", font=("Helvetica", 14))
#         self.label.pack(pady=20)

#         #setting a time
#         self.time_entry = tk.Entry(root, font=("Helvetica", 14), width=10)
#         self.time_entry.pack(pady=10)
#         self.set_button = tk.Button(root, text="Set Alarm", font=("Helvetica", 14), command=self.set_alarm)
#         self.set_button.pack(pady=20)

#     def timer_widget_setter(self, root):
#         #or set timer
#         self.label = tk.Label(root, text="Set Timer (minutes)", font=("Helvetica", 14))
#         self.label.pack(pady=20)

#         #setting a time
#         self.timer_entry = tk.Entry(root, font=("Helvetica", 14), width=10)
#         self.timer_entry.pack(pady=10)
#         self.set_button = tk.Button(root, text="Set Timer", font=("Helvetica", 14), command=self.set_timer)
#         self.set_button.pack(pady=20)

#     def url_widget_setter(self, root):
#         #setting an URL like
#         self.url_entry = tk.Entry(root, font=("Helvetica", 14), width=30)
#         self.url_entry.pack(pady=10)
#         self.label_url = tk.Button(root, text="Set URL", font=("Helvetica", 14), command= self.set_url)
#         self.label_url.pack(pady=10)
#         # self.set_default_url("https://www.google.com")


#     def set_url(self):
#         self.url = self.url_entry.get()
#         messagebox.showinfo("URL Set", f"URL set for {self.url}")

#     def update_alarm_listbox(self):
#         self.alarm_listbox.delete(0, tk.END)
#         #sort the alarms by the alarm time
#         for alarm_time, video_url in self.alarms:
#             self.alarm_listbox.insert(tk.END, f"Alarm at {alarm_time} - Video URL: {video_url}")

#     #function called when you press set_timer
#     def set_timer(self):
#         minutes = int(self.timer_entry.get())
#         if minutes == 0 or minutes < 0:
#                 messagebox.showerror("Invalid Input", "Please enter a valid number of minutes")
#                 return 
#         if self.url == None:
#             messagebox.showerror("Invalid Input", "Please enter your URL")
#             return
#         alarm_time = (datetime.now() + timedelta(minutes=minutes)).time()
#         alarm_time = alarm_time.strftime("%H:%M")
#         url = self.url
#         self.add_alarm(alarm_time, url)
#         # messagebox.showinfo("Timer Set", f"Alarm set for {alarm_time} with video {url} in {minutes} minutes")

#     #function called when you press set_URL
#     def set_alarm(self):
#         alarm_time = self.time_entry.get()
#         if self.url == None:
#             messagebox.showerror("Invalid Input", "Please enter your URL")
#             return
#         url = self.url
#         self.add_alarm(alarm_time, url)

#     def delete_selected_alarm(self):
#         if self.selected_index is not None:
#             del self.alarms[self.selected_index]
#             self.update_alarm_listbox()
#         else:
#             messagebox.showerror("Error", "No alarm selected")

#     # append alarm_listbox an alarms
#     def add_alarm(self, alarm_time, url):
#         try:
#             # Validate the entered time format
#             datetime.strptime(alarm_time, "%H:%M")
#         except ValueError:
#             messagebox.showerror("Invalid Time", "Please enter a valid time in HH:MM format.")
#             return
#         # Check if the entered time is in the correct format
#         alarm_entry = f"{alarm_time} {url}"
#         self.alarm_listbox.insert(tk.END, alarm_entry)
#         self.alarms.append([alarm_time, url])
#         self.alarms.sort(key=lambda x: datetime.strptime(x[0], "%H:%M"))
#         self.update_alarm_listbox()
#         self.check_alarm()

    
#     def check_alarm(self):
#         current_time = datetime.now().time().replace(second=0, microsecond=0).strftime("%H:%M")
#         for alarm in self.alarms[:]:
#             alarm_time, video_url = alarm
#             if alarm_time == current_time and video_url:
#                 self.alarms.remove(alarm)
#                 self.show_alarm_window(video_url)
#                 #pop the element
#                 # self.alarm_listbox.delete(i)
#                 break

#         else:
#             self.root.after(1000, self.check_alarm)  # Continue checking every second

#     def update_time(self):
#         current_time = datetime.now().strftime("%H:%M:%S")
#         self.current_time_label.config(text=f"Current Time: {current_time}")
#         self.root.after(1000, self.update_time)  # Update the time every minute

#     def show_alarm_window(self, video_url):
#         # Create a new window
#         webbrowser.open_new(video_url)
#         self.update_alarm_listbox()
#     def on_listbox_select(self, event):
#         widget = event.widget
#         selection = widget.curselection()
#         if selection:

#             self.selected_index = selection[0]
#         else:
#             self.selected_index = None



# if __name__ == "__main__":
#     window = tk.Tk()
#     app = AlarmApp(window)
#     window.mainloop()


