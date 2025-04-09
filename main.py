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
        
def update_record(record_list):
    if not record_list:
        print("No records available to update.")
        input("\nPress Enter to return to the main menu...")
        return

    user_input = input("\nEnter the name of the member you want to update: ")

    index = None
    record_index = 0
    while record_index < len(record_list):
        current_user = record_list[record_index]["user_name"].lower()
        if user_input.lower() == current_user:
            index = record_index
            break
        record_index += 1

    if index is None:
        print("Record not found.")
        input("\nPress Enter to return to the main menu...")
        return

    member = record_list[index]
    print("\nWhat do you want to update?")
    print("1 - Name")
    print("2 - Course and Section")
    print("3 - Programming Language")
    print("4 - Preferred Role")
    print("5 - Skill Level")

    try:
        update_choice = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    match update_choice:
        case 1:
            member["user_name"] = input("Enter new name: ").strip()
        case 2:
            member["course_section"] = input(
                "Enter new course and section: "
                ).strip()
        case 3:
            member["programming_language"] = input(
                "Enter new preferred programming language: "
                ).strip()
        case 4:
            member["role"] = input("Enter new preferred role: ").strip()
        case 5:
            member["skill_level"] = input("Enter new skill level: ").strip()
        case _:
            print("Invalid choice. No changes made.")
            return

    print("Record updated successfully.")
    input("\nPress Enter to return to the main menu...")

# Function to delete a record
def delete_record(record_list):
    if not record_list:
        print("No records available to delete.")
        input("\nPress Enter to return to the main menu...")
        return

    print(f"There are {len(record_list)} available records.\n")
    user_input = int(input(f"Enter Member Number ({len(record_list)}) "
                           "to delete: ")) #keep columns under 80
    #I used member number instead of record number
    #because the display is Member 1, Member 2, etc. 
    #This will make it easier to read

    if 1 <= user_input <= len(record_list):
        deleted_record = record_list.pop(user_input - 1)
        print(f"\nRecord {user_input} deleted successfully:")
        for key, value in deleted_record.items():
            print(f"{key}: {value}")
    else:
        print("Record Number not found.\n")

    input("\nPress Enter to return to the main menu...")

def search_record(record_list):
    print(f"There are {len(record_list)} available records in the record"
            " list.\n")
    
    user_input = input("Enter the name you are looking for: ")

    for item in record_list:
        if user_input.lower() == item["user_name"].lower():
            for key, value in item.items():
                print(f"{key}: {value}")
    
        else:
            print("Record not found.")

    input("\nPress Enter to return to the main menu...")

def main():
    record_list = [{        
        "user_name": "Eurielle",
        "course_section": "BSIT 2-1",
        "programming_language": "Python",
        "role": "Front-end",
        "skill_level": "Beginner"}]
    
    while True:
        clear()
        print("\n==============================================")
        print("||       HIGHPYVE MEMBERS TECH PROFILE      ||")
        print("==============================================")
        print("||  1 - List All                            ||")
        print("||  2 - Add                                 ||")
        print("||  3 - Update                              ||")
        print("||  4 - Delete                              ||")
        print("||  5 - Search                              ||")
        print("||  6 - Exit                                ||")
        print("==============================================")
        choice = input("\nEnter your choice: ")

        if not choice.isdigit():
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
                update_record(record_list)
            case 4:
                clear()
                delete_record(record_list)
            case 5:
                clear()
                search_record(record_list)
            case 6:
                print("Exiting HighPYve Tech Profile. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select from the menu.")

main()