contact = {}

def showfunction():
    print(contact.items())
    print("Name \t Contact")
    for key in contact:
        print("{} \t {}".format(key,contact.get(key)))

while True:
    choice = int(input("1. Add new contact \n"
                   "2. Search the contact \n"
                   "3. Display the contact \n"
                   "4. Edit the contact \n"
                   "5. Delete the contact \n"
                   "6. Exit \n"
                   "Please write the number between 1-6: "))
    if choice == 1:
        name = input("Add your contact name: ")
        phone = input("Add your phone number: ")
        contact[name] = phone

    elif choice == 2:
        contactname = input("search the contact: ")
        if contactname in contact:
            print(contactname, "contact number is ",contact[contactname])
        else:
            print("Not found this contact")

    elif choice == 3:
        if not contact:
            print("contact book is empty")
        else:
            showfunction()
    elif choice == 4:
        Editcontact = input("Edit your contact: ")
        if Editcontact in contact:
            phone = input("Enter your new number: ")
            contact[Editcontact] = phone
            print("contact updated successfully ")
            showfunction()
        else:
            print("Name is not found")
    elif choice == 5:
        del_contact = input("Which contact do you want to delete?: ")
        if del_contact in contact:
            confirm_del = input("Do you want to delete this contact [y/n]: ")
            if confirm_del == "y" or confirm_del == "Y":
                contact.pop(del_contact)
            showfunction()
        else:
            print("The name is not found in the contact")

    else:
        break











