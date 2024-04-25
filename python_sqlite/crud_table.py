#!/usr/bin/python3

from create_database import *
from create_table import *
from insert_table import *
from read_table import *
from delete_table import *
from update_table import *


def main():
    while True:
        print("\n ===== Database Application =====")
        print("1. Create Database")
        print("2. Create Table")
        print("3. Insert Table")
        print("4. Read Table")
        print("5. Update Table")
        print("6. Delete Table")
        print("7. Quit")
        
        print("\n")
        option = int(input("Enter your option: "))
        print("\n")

        if option == 1:
            create_database()
        elif option == 2:
            create_table()
        elif option == 3:
            student_id = input("Enter student_id: ")
            first_name = input("Enter first_name: ")
            last_name = input("Enter last_name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            
            insert_student_details(student_id, first_name, last_name, phone, email)
        elif option == 4:
            read_table()
        elif option == 5:
            print("=== Update Option ===")
            print("1. Update Phone")
            print("2. Update Email")

            print("\n")

            option_5 = int(input("Enter an option: "))
            if option_5 == 1:
                student_id = int(input("Enter student_id: "))
                phone = input("Enter phone: ")
                update_student_phone(student_id, phone)
            elif option_5 == 2:
                student_id = int(input("Enter student_id: "))
                email = input("Enter email: ")
                update_student_email(student_id, email)
            else:
                print("Invalid option, Please try again.")

        elif option == 6:
            student_id = int(input("Enter student_id: "))
            delete_student_details(student_id)
        elif option == 7:
            print("Database Application terminated")
            print("\n")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
