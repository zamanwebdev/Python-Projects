from win10toast import ToastNotifier
import time

# Create notifier object
Toast = ToastNotifier()

# Show the toast notification
Toast.show_toast(
    "Learning Time",                       # Title
    "Hello Zaman! It's time to learn something new.",  # Message
    duration=10,                            # Duration in seconds
    threaded=True                           # Allows program to continue running
)

# Keep script alive while notification is active
while Toast.notification_active():
    time.sleep(0.1)
