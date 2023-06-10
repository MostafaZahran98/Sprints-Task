import csv
from datetime import datetime
from datetime import date

filename = datetime.now().strftime('contactbook_%m%d%Y.csv')


# this function for creating the file
def create_contact():
    username = input("Please Enter Your Username: ")
    email = input("Please Enter Your Email address: ")
    phone_number = input("Please Enter Your Number: ")
    address = input("Please Enter Your Address: ")
    insertion_date = date.today()
    contacts = [username, email, phone_number, address, insertion_date]

    # create a csv file with a daily date
    with open(filename, 'a', newline='') as f_output:
        csv_output = csv.writer(f_output)
        csv_output.writerow(contacts)
    print("The contact info is saved successfully! ")


def delete_contact():
    check = int(input("Please enter the contact ID you want to delete: "))
    with open(filename, "r") as f:
        reader = csv.reader(f)
        rows = list(reader)
    # check if the contact is found or not
    if int(check - 1) in range(0, len(rows)):
        print("Contact is found!")
        print("Contact is deleted successfully!")
        # remove a row
        row_to_delete = check - 1
        del rows[row_to_delete]
    else:
        print("Contact is not found!")
    # write updated data back to the CSV file
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(rows)


def update_contact():
    check = int(input("Enter the contact ID to update: "))
    # Open the CSV file in read mode
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        contacts = list(reader)
    # check if the contact is found or not
    if int(check - 1) in range(0, len(contacts)):
        contact = contacts[int(check) - 1]
        print("Contact is found!")
        entry = int(input("Enter the field to update \n"
                          "1. Username\n"
                          "2. Email\n"
                          "3. Phone numbers\n"
                          "4. Address\n"
                          "5. Insertion date\n"))
        if entry == 1:
            contact[0] = input("Please enter the updated username: ")
        elif entry == 2:
            contact[1] = input("Please enter the updated email: ")
        elif entry == 3:
            contact[2] = input("Please enter the updated username: ")
        elif entry == 4:
            contact[3] = input("Please enter the updated username: ")
        elif entry == 5:
            contact[4] = date.today()
            print("Insertion date is generated successfully!")

        # write updated data back to the CSV file
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(contacts)
        print("Contact updated successfully!")
    else:
        print("Contact is not found!")


while True:

    user_entry = input('Please press 1 to Create Contact \n'
                       'Please press 2 to Delete Contact\n'
                       'Please press 3 to Update Contact\n'
                       'Please press 4 to Exit\n')
    if user_entry == "1":
        create_contact()
    elif user_entry == "2":
        delete_contact()
    elif user_entry == "3":
        update_contact()
    elif user_entry == "4":
        break
    else:
        print("Please enter a valid number")
