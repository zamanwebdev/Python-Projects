contacts = {}


def show_contacts():
    if not contacts:
        print("\n📭 No contacts saved.\n")
        return

    print("\n📒 Contact List")
    print("-" * 30)
    print("Name\t\tPhone")
    print("-" * 30)
    for name, phone in contacts.items():
        print(f"{name.title():<15}{phone}")
    print()


def add_contact():
    name = input("Enter name: ").lower().strip()
    if name in contacts:
        print("⚠️ Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    if not phone.isdigit():
        print("❌ Phone must contain only numbers!")
        return

    contacts[name] = phone
    print("✅ Contact added.")


def search_contact():
    name = input("Search name: ").lower().strip()
    if name in contacts:
        print(f"📞 {name.title()}'s number is {contacts[name]}")
    else:
        print("❌ Contact not found.")


def edit_contact():
    name = input("Enter name to edit: ").lower().strip()
    if name in contacts:
        phone = input("Enter new number: ").strip()
        if phone.isdigit():
            contacts[name] = phone
            print("✏️ Contact updated.")
        else:
            print("Invalid phone number.")
    else:
        print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").lower().strip()
    if name in contacts:
        confirm = input("Are you sure? (y/n): ").lower()
        if confirm == "y":
            del contacts[name]
            print("🗑️ Contact deleted.")
    else:
        print("Contact not found.")


# -------- Main Menu Loop --------
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
        print("❌ Enter a valid number!\n")
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
        print("👋 Exiting program...")
        break
    else:
        print("Invalid choice.")
