import tkinter as tk
from tkinter import messagebox
from win10toast import ToastNotifier
import threading
import time
from datetime import datetime

# Create notifier
notifier = ToastNotifier()

# Global flag to control notifications
running = [False]

def notify_message(msg, interval_sec, schedule_time=None):
    while running[0]:
        now = datetime.now().strftime("%H:%M:%S")
        # If schedule_time is set, wait until that exact time
        if schedule_time:
            if now >= schedule_time:
                notifier.show_toast("Reminder", msg, duration=10, threaded=True)
                # Stop after one notification if scheduled
                running[0] = False
                break
        else:
            notifier.show_toast("Reminder", msg, duration=10, threaded=True)
            while notifier.notification_active():
                time.sleep(0.1)
            time.sleep(interval_sec)

def start_notifications():
    msg = message_entry.get()
    interval = interval_entry.get()
    seconds = seconds_entry.get()
    schedule_time = schedule_entry.get()

    if not msg:
        messagebox.showwarning("Warning", "Please enter a message!")
        return

    # Determine interval in seconds
    try:
        interval_sec = 0
        if interval:
            interval_sec += int(interval) * 60
        if seconds:
            interval_sec += int(seconds)
        if interval_sec == 0 and not schedule_time:
            messagebox.showwarning("Warning", "Please set an interval or schedule time!")
            return
    except ValueError:
        messagebox.showerror("Error", "Interval and seconds must be numbers!")
        return

    # Validate schedule time format if given
    if schedule_time:
        try:
            time.strptime(schedule_time, "%H:%M:%S")
        except ValueError:
            messagebox.showerror("Error", "Time must be in HH:MM:SS format!")
            return

    running[0] = True
    start_btn.config(state="disabled")
    stop_btn.config(state="normal")

    threading.Thread(target=notify_message, args=(msg, interval_sec, schedule_time), daemon=True).start()

def stop_notifications():
    running[0] = False
    start_btn.config(state="normal")
    stop_btn.config(state="disabled")

def exit_app():
    running[0] = False
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Advanced Desktop Notifier")
root.geometry("400x300")

tk.Label(root, text="Message:").pack(pady=5)
message_entry = tk.Entry(root, width=50)
message_entry.pack(pady=5)

tk.Label(root, text="Interval (minutes, optional):").pack(pady=5)
interval_entry = tk.Entry(root, width=10)
interval_entry.pack(pady=5)

tk.Label(root, text="Interval (seconds, optional):").pack(pady=5)
seconds_entry = tk.Entry(root, width=10)
seconds_entry.pack(pady=5)

tk.Label(root, text="Schedule Time (HH:MM:SS, optional):").pack(pady=5)
schedule_entry = tk.Entry(root, width=15)
schedule_entry.pack(pady=5)

start_btn = tk.Button(root, text="Start Notifications", command=start_notifications)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Stop Notifications", command=stop_notifications, state="disabled")
stop_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", command=exit_app)
exit_btn.pack(pady=5)

root.mainloop()
