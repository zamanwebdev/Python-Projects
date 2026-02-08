import tkinter as tk
from tkinter import messagebox, filedialog
import json, os
from openpyxl import Workbook

FILE_NAME = "contacts.json"

# ---------- Login Credentials ----------
USER = "admin"
PASSWORD = "1234"

# ---------- Load Contacts ----------
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        contacts = json.load(f)
else:
    contacts = {}

def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f)

# ---------- Functions ----------
def add_contact():
    name = name_var.get().lower().strip()
    phone = phone_var.get().strip()

    if not name or not phone.isdigit():
        messagebox.showerror("Error", "Enter valid name & number")
        return

    contacts.setdefault(name, []).append(phone)
    save_contacts()
    update_list()
    name_var.set("")
    phone_var.set("")
    messagebox.showinfo("Success", "Contact Saved")

def search_contact():
    term = name_var.get().lower()
    update_list(filter_term=term)

def delete_contact():
    selected = contact_list.get(tk.ACTIVE)
    if not selected:
        return
    name = selected.split(" : ")[0].lower()
    if name in contacts:
        del contacts[name]
        save_contacts()
        update_list()

def update_list(filter_term=""):
    contact_list.delete(0, tk.END)
    for name, nums in contacts.items():
        if filter_term in name:
            contact_list.insert(tk.END, f"{name.title()} : {', '.join(nums)}")

def export_excel():
    if not contacts:
        messagebox.showinfo("Info", "No contacts to export")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx",
                                             filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return

    wb = Workbook()
    ws = wb.active
    ws.title = "Contacts"
    ws.append(["Name", "Phone Numbers"])

    for name, nums in contacts.items():
        ws.append([name.title(), ", ".join(nums)])

    wb.save(file_path)
    messagebox.showinfo("Success", f"Contacts exported to {file_path}")

# ---------- Login Window ----------
def login():
    def attempt_login():
        user = user_var.get()
        pw = pass_var.get()
        if user == USER and pw == PASSWORD:
            login_win.destroy()
            main_window()
        else:
            messagebox.showerror("Error", "Wrong username or password")

    login_win = tk.Tk()
    login_win.title("Login")
    login_win.geometry("300x150")
    login_win.configure(bg="#1e1e2f")

    tk.Label(login_win, text="Username", bg="#1e1e2f", fg="white").pack(pady=5)
    user_var = tk.StringVar()
    tk.Entry(login_win, textvariable=user_var).pack()

    tk.Label(login_win, text="Password", bg="#1e1e2f", fg="white").pack(pady=5)
    pass_var = tk.StringVar()
    tk.Entry(login_win, textvariable=pass_var, show="*").pack()

    tk.Button(login_win, text="Login", command=attempt_login, bg="#4CAF50", fg="white").pack(pady=10)

    login_win.mainloop()

# ---------- Main Window ----------
def main_window():
    global name_var, phone_var, contact_list

    root = tk.Tk()
    root.title("Pro Contact Manager")
    root.geometry("550x500")
    root.configure(bg="#1e1e2f")

    tk.Label(root, text="📒 Contact Manager", font=("Arial", 18, "bold"), bg="#1e1e2f", fg="white").pack(pady=10)

    # Input Frame
    input_frame = tk.Frame(root, bg="#2c2c3e", padx=10, pady=10)
    input_frame.pack(pady=10)

    name_var = tk.StringVar()
    phone_var = tk.StringVar()

    tk.Label(input_frame, text="Name", bg="#2c2c3e", fg="white").grid(row=0, column=0, padx=5, pady=5)
    tk.Entry(input_frame, textvariable=name_var, width=25).grid(row=0, column=1, padx=5)

    tk.Label(input_frame, text="Phone", bg="#2c2c3e", fg="white").grid(row=1, column=0, padx=5, pady=5)
    tk.Entry(input_frame, textvariable=phone_var, width=25).grid(row=1, column=1, padx=5)

    # Buttons
    btn_frame = tk.Frame(root, bg="#1e1e2f")
    btn_frame.pack(pady=10)

    tk.Button(btn_frame, text="Add", width=12, bg="#4CAF50", fg="white", command=add_contact).grid(row=0, column=0, padx=5)
    tk.Button(btn_frame, text="Search", width=12, bg="#2196F3", fg="white", command=search_contact).grid(row=0, column=1, padx=5)
    tk.Button(btn_frame, text="Delete", width=12, bg="#f44336", fg="white", command=delete_contact).grid(row=0, column=2, padx=5)
    tk.Button(btn_frame, text="Export Excel", width=12, bg="#FFC107", fg="white", command=export_excel).grid(row=0, column=3, padx=5)

    # Listbox
    list_frame = tk.Frame(root)
    list_frame.pack(pady=10)

    contact_list = tk.Listbox(list_frame, width=60, height=15, font=("Arial", 10))
    contact_list.pack(side=tk.LEFT)

    scrollbar = tk.Scrollbar(list_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    contact_list.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=contact_list.yview)

    update_list()

    root.mainloop()

# ---------- Run App ----------
login()
