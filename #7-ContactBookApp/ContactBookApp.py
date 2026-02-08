from random import choice

contact = {}

def ShowFuntion():
    print(contact.items())
    print("Name \t Phone Number")
    for key in contact:
        print("{} \t {}".format(key,contact.get(key)))
while True:
    choice = int( input("1. Add New Contact. \n"
                   "2. Search the Contact. \n"
                   "3. Display the Contact. \n"
                   "4. Edit the Contact. \n"
                   "5. Delete the Contact. \n"
                   "6. Exit. \n"
                   "Please write the Number between 1-6: ")
                  )
    if choice == 1:
        name = input("Add your Contact Name : ")
        phone = input("Add your Phone Number: ")
        contact[name] = phone
    elif choice == 2:
        ContactName = input("Search the Contact: ")
        if ContactName in contact:
            print(ContactName,"Contact Number is ",contact[ContactName])
        else:
            print("Not found the Contact Number")
    elif choice == 3:
        if not contact:
            print("Contact Not Found")
        else:
            ShowFuntion()
    elif choice == 4:
        EditContact = input("Edit the Contact: ")
        if EditContact in contact:
            phone = input("Change your Phone Number: ")
            contact[EditContact] = phone
            print("Contact updated successfully")
        else:
            print("Name is not found")
            ShowFuntion()
    elif choice == 5:
        DeleteContact = input("Witch contact do you want to Delete? ")
        if DeleteContact in contact:
            DeleteConfirm = input("do you want to delete this contact? [y/n]")
            if DeleteConfirm == "y" or DeleteConfirm == "Y":
                contact.pop(DeleteContact)
                ShowFuntion()
        else:
            print("The name is Not Found in the Contact")
    else:
        break

