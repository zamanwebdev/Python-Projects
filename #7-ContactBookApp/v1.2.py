import json
import os

FILE_NAME = "contacts.json"
PASSWORD = "1234"  # change this

# ---------- Load contacts ----------
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as f:
        contacts = json.load(f)
else:
    contacts = {}


# ---------- Save contacts ----------
def save_contacts():
    with open(FILE_NAME, "w") as f:
        json.dump(contacts, f)


# ---------- Show Contacts ----------
def show_contacts():
    if not contacts:
        print("\n📭 No contacts saved.\n")
        return

    print("\n📒 Contact List")
    print("-" * 40)
    for name, numbers in contacts.items():
        print(f"{name.title():<15} {', '.join(numbers)}")
    print()


# ---------- Add Contact ----------
def add_contact():
    name = input("Enter name: ").lower().strip()
    phone = input("Enter phone number: ").strip()

    if not phone.isdigit():
        print("❌ Phone must be numbers only!")
        return

    if name in contacts:
        contacts[name].append(phone)
    else:
        contacts[name] = [phone]

    save_contacts()
    print("✅ Contact saved.")


# ---------- Search Contact ----------
def search_contact():
    term = input("Search name: ").lower().strip()
    found = False

    for name in contacts:
        if term in name:
            print(f"📞 {name.title()}: {', '.join(contacts[name])}")
            found = True

    if not found:
        print("❌ No matching contacts.")


# ---------- Edit Contact ----------
def edit_contact():
    name = input("Enter name to edit: ").lower().strip()
    if name in contacts:
        print("Current numbers:", ", ".join(contacts[name]))
        phone = input("Enter new number to add: ")
        if phone.isdigit():
            contacts[name].append(phone)
            save_contacts()
            print("✏️ Number added.")
        else:
            print("Invalid number.")
    else:
        print("Contact not found.")


# ---------- Delete Contact ----------
def delete_contact():
    name = input("Enter name to delete: ").lower().strip()
    if name in contacts:
        confirm = input("Delete this contact? (y/n): ").lower()
        if confirm == "y":
            del contacts[name]
            save_contacts()
            print("🗑️ Contact deleted.")
    else:
        print("Contact not found.")


# ---------- Password Check ----------
attempt = input("Enter password to open contacts: ")
if attempt != PASSWORD:
    print("⛔ Wrong password!")
    exit()

# ---------- Main Menu ----------
while True:
    print("""
1. Add Contact
2. Search Contact
3. Display Contacts
4. Edit Contact
5. Delete Contact
6. Exit
""")

    try:
        option = int(input("Choose (1-6): "))
    except ValueError:
        print("Enter valid number!")
        continue

    if option == 1:
        add_contact()
    elif option == 2:
        search_contact()
    elif option == 3:
        show_contacts()
    elif option == 4:
        edit_contact()
    elif option == 5:
        delete_contact()
    elif option == 6:
        print("👋 Goodbye!")
        break
    else:
        print("Invalid option.")
