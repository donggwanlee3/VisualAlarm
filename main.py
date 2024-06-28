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



