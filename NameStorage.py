import numpy as np

#Das Programm fordert den Nutzer auf, Daten für einen Array einzugebene, der Namen und das dazugehörige Alter speichert.

# print(names)
# print(ages)
# print(names.ndim)
# print(ages.ndim)

count = 0
names = np.full(200, fill_value="", dtype="S40")
ages = np.zeros_like(names, dtype=int)



print("Welcome to your contacts!")


def contacts():
    load_saved_files()
    adding_new_contacts()


def adding_new_contacts():
    add_new_contacts = input("Would you like to add new contacts? \nYes [y]\nNo [n]\n")
    if add_new_contacts == "y":
        new_entry()
    elif add_new_contacts == "n":
        closing_program()
    else:
        print("Error. Enter y or n.")
        adding_new_contacts()


def new_entry():
    global count
    if count == 0:
        names[0] = str(input("Enter the first name: "))                                 #todo Add error when name is longer than 40 chars
        ages[0] = int(input("Enter age of " + names[0].decode("utf-8") + ": "))         #todo Add error when age is not valid
        successfully_added()
    elif count > 0:
        names[count] = str(input("Enter name no. " + str(count + 1) + ": "))
        ages[count] = int(input("Enter age of " + names[count].decode("utf-8") + ": "))
        successfully_added()
    count += 1
    another_entry()


def another_entry():
    more_entries = input("Would you like to add more entries [a],\nsee your contact list [b]\nor exit this program [c]? \n")
    if more_entries == "a":
        new_entry()
    elif more_entries == "b":
        for i in range(count):
            print("Name: " + names[i].decode("utf-8") + "      Age: " + str(ages[i]))
        another_entry()
    elif more_entries == "c":
        closing_program()
    else:
        print("Error. Type a, b or c.")
        another_entry()


def successfully_added():
    print(names[count].decode("utf-8") + " with the age of " + str(ages[count]) + " successfully added to your contacts. \n")


def closing_program():
    np.save("savednames.npy", names)
    np.save("savedages.npy", ages)
    print("Saved. Closing program...")


def load_saved_files():
    global names
    global ages
    try:
        names = np.load("savednames.npy")
        print(names)
    except FileNotFoundError:
        print("No saved file for names found. Creating save when closing program.")
    except:
        print("Something went wrong loading saved files.")

    try:
        ages = np.load("savedages.npy")
        print(ages)
    except FileNotFoundError:
        print("No saved file for ages found. Creating save when closing program.")
    except:
        print("Something went wrong loading saved files.")


contacts()


#todo Saved contacts do not show up when rerunning the script