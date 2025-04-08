import os

def clear():
    os.system("cls")

def list_all_records(record_list):
    
    if not record_list:
        print("No records found.")
    else:
        print("\nList of All Users:")
        counter = 1
        for record in record_list:
            print(f"\nMember {counter}:")
            for key, value in record.items():
                print(f"{key}: {value}")
            counter += 1
    
    input("\nPress Enter to return to the main menu...")

def add_record(record_list):
    
    user_name = input("\nEnter your name (LN, FN MI) : ")
    course_section = input("\nEnter your course and section : ")
    programming_language = input("\nEnter your preferred programming "
                                "language (ex: Python) : ")
    role = input("\nEnter your preferred role (ex: Backend) : ")
    skill_level = input("\nEnter your skill level (Beginner, Intermediate, "
                        "Advanced) : ")

    user_record = {
        "user_name"             : user_name,
        "course_section"        : course_section,
        "programming_language"  : programming_language,
        "role"                  : role,
        "skill_level"           : skill_level
    }

    record_list.append(user_record)
    
    input("\nUser Record added successfully. Press Enter to return "
          "to the main menu...")
        

# TODO (BAYOS): Create a function to update a record
def update_record():
    pass

# TODO (BARTOLOME): Create a function to delete a record 
def delete_record():
    pass

# TODO (ANIPAN): Create a function to search for a specific record
def search_record():
    pass


def main():
    record_list = []
    while True:
        clear()
        print("\nHIGHPYVE TECH PROFILE")
        print("\n1 - List All")
        print("2 - Add")
        print("3 - Update")
        print("4 - Delete")
        print("5 - Search")
        print("6 - Exit")

        choice = input("\nEnter your choice: ")

        if not choice.isnumeric():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        match choice:
            case 1:
                clear()
                list_all_records(record_list)
            case 2:
                clear()
                add_record(record_list)
            case 3:
                clear()
                update_record()
            case 4:
                clear()
                delete_record()
            case 5:
                clear()
                search_record()
            case 6:
                print("Exiting HighPYve Tech Profile. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select from the menu.")

main()