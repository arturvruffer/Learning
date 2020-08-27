import numpy as np
import os

#Das Programm fordert den Nutzer auf, Daten für einen Array einzugebene, der Namen und das dazugehörige Alter speichert.

# print(names)
# print(ages)
# print(names.ndim)
# print(ages.ndim)

def contacts():
    print("Welcome to your contacts!")
    initialise_variables()
    load_saved_files()
    adding_new_contacts()


def adding_new_contacts():
    add_new_contacts = input("Would you like to add new contacts [a] or view your contact list [v]?\n")
    if add_new_contacts == "a":
        new_entry()
    elif add_new_contacts == "v":
        view_contacts()
    else:
        print("Error. Enter y or n.")
        adding_new_contacts()


def new_entry():
    global contact_count
    if contact_count == 0:
        names[0] = str(input("Enter the first name: "))                                 #todo Add error when name is longer than 40 chars
        ages[0] = int(input("Enter age of " + names[0].decode("utf-8") + ": "))         #todo Add error when age is not valid
        successfully_added()
    elif contact_count > 0:
        names[contact_count] = str(input("Enter name no. " + str(contact_count + 1) + ": "))
        ages[contact_count] = int(input("Enter age of " + names[contact_count].decode("utf-8") + ": "))
        successfully_added()
    contact_count += 1
    another_entry()


def another_entry():
    more_entries = input("Would you like to add more entries [a],\nsee your contact list [b]\nor exit this program [c]? \n")
    more_entries = more_entries.casefold()
    if more_entries == "a":
        new_entry()
    elif more_entries == "b":
        view_contacts()
    elif more_entries == "c":
        closing_program()
    elif more_entries == "delete":
        delete_contacts()
    else:
        print("Error. Type a, b or c.")
        another_entry()


def successfully_added():
    print(names[contact_count].decode("utf-8") + " with the age of " + str(ages[contact_count]) + " successfully added to your contacts. \n")


def closing_program():
    contacts_count_save = np.array([contact_count])
    np.save("savedcontactcount.npy", contacts_count_save)
    np.save("savednames.npy", names)
    np.save("savedages.npy", ages)
    print("Saved. Closing program...")


def load_saved_files():
    global names
    global ages
    global contact_count
    try:
        names = np.load("savednames.npy")
        print("Names successfully loaded.")
    except FileNotFoundError:
        print("No saved file for names found. Creating save when closing program.")
    except:
        print("Something went wrong loading saved names.")

    try:
        ages = np.load("savedages.npy")
        print("Ages successfully loaded.")
    except FileNotFoundError:
        print("No saved file for ages found. Creating save when closing program.")
    except:
        print("Something went wrong loading saved ages.")

    try:
        contact_count = np.load("savedcontactcount.npy")[0]
        print("Contact count successfully loaded.")
    except FileNotFoundError:
        print("No saved file for contact count found. Creating save when closing program.")
    except:
        print("Something went wrong loading the contact count.")


def view_contacts():
    if contact_count == 0:
        print("No saved contacts. Try adding entries.")

    for i in range(contact_count):
        print("Name: " + names[i].decode("utf-8") + "      Age: " + str(ages[i]))
    another_entry()


def delete_contacts():
    try:
        os.remove("savednames.npy")
        os.remove("savedages.npy")
        os.remove("savedcontactcount.npy")
        initialise_variables()
        print("Contacts successfully deleted.")
    except:
        print("Error. Could not delete saved contacts.")


def initialise_variables():
    global contact_count
    global names
    global ages
    contact_count = 0
    names = np.full(200, fill_value="", dtype="S40")
    ages = np.zeros_like(names, dtype=int)


contacts()


#todo Saved contacts do not show up when rerunning the script


#count is being reset after every start of the program
