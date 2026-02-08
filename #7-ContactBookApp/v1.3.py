import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "contacts.json"

# ---------- Load Data ----------
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
    name = name_entry.get().lower().strip()
    phone = phone_entry.get().strip()

    if not name or not phone.isdigit():
        messagebox.showerror("Error", "Enter valid name and number")
        return

    if name in contacts:
        contacts[name].append(phone)
    else:
        contacts[name] = [phone]

    save_contacts()
    messagebox.showinfo("Success", "Contact Added")
    update_listbox()


def search_contact():
    term = name_entry.get().lower().strip()
    result_list.delete(0, tk.END)

    for name in contacts:
        if term in name:
            result_list.insert(tk.END, f"{name.title()} : {', '.join(contacts[name])}")


def delete_contact():
    selected = result_list.get(tk.ACTIVE)
    if not selected:
        return

    name = selected.split(" : ")[0].lower()
    if name in contacts:
        del contacts[name]
        save_contacts()
        update_listbox()
        messagebox.showinfo("Deleted", "Contact removed")


def update_listbox():
    result_list.delete(0, tk.END)
    for name, nums in contacts.items():
        result_list.insert(tk.END, f"{name.title()} : {', '.join(nums)}")


# ---------- Window Setup ----------
root = tk.Tk()
root.title("📒 Contact Manager")
root.geometry("400x450")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)
tk.Button(root, text="Search", command=search_contact).pack(pady=5)
tk.Button(root, text="Delete Selected", command=delete_contact).pack(pady=5)

result_list = tk.Listbox(root, width=50)
result_list.pack(pady=10)

update_listbox()

root.mainloop()
