import tkinter as tk
from tkinter import messagebox
from win10toast import ToastNotifier
import threading
import time

# Create notifier
notifier = ToastNotifier()

# Function to run notifications in background
def start_notifications():
    try:
        interval = int(interval_entry.get()) * 60  # convert minutes to seconds
        msg = message_entry.get()
        if not msg:
            messagebox.showwarning("Warning", "Please enter a message!")
            return
        start_btn.config(state="disabled")
        stop_btn.config(state="normal")

        def notify():
            while running[0]:
                notifier.show_toast("Reminder", msg, duration=10, threaded=True)
                while notifier.notification_active():
                    time.sleep(0.1)
                time.sleep(interval)
        threading.Thread(target=notify, daemon=True).start()
    except ValueError:
        messagebox.showerror("Error", "Interval must be a number!")

# Function to stop notifications
def stop_notifications():
    running[0] = False
    start_btn.config(state="normal")
    stop_btn.config(state="disabled")

# GUI setup
root = tk.Tk()
root.title("Desktop Notifier")
root.geometry("350x200")

tk.Label(root, text="Message:").pack(pady=5)
message_entry = tk.Entry(root, width=40)
message_entry.pack(pady=5)

tk.Label(root, text="Interval (minutes):").pack(pady=5)
interval_entry = tk.Entry(root, width=10)
interval_entry.pack(pady=5)

running = [True]

start_btn = tk.Button(root, text="Start Notifications", command=start_notifications)
start_btn.pack(pady=10)

stop_btn = tk.Button(root, text="Stop Notifications", command=stop_notifications, state="disabled")
stop_btn.pack(pady=5)

root.mainloop()
