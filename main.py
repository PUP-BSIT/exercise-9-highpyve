def list_all_records(record_list):
    if not record_list:
        print("No records found.")
    else:
        print("\nList of All Member(s):")
        counter = 1
        for record in record_list:
            print(f"\nMember {counter}:")
            for key, value in record.items():
                print(f"{key}: {value}")
            counter += 1

# TODO (TOLENTINO): Create a function to add a record 
def add_record():
    pass

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
    record_list = [
        {
        "Name": "Jaira Isabel F. Ocariza",
        "Course & Section": "BSIT 2-1",
        "Preferred Programming Language": "Python",
        "Preferred Role": "Backend Developer",
        "Skill Level": "Beginner"
        }
    ]
    while True:
        print("\nHIGHPYVE TECH PROFILE")
        print("1 - List All")
        print("2 - Add")
        print("3 - Update")
        print("4 - Delete")
        print("5 - Search")
        print("6 - Exit")

        choice = input("Enter your choice: ")

        if not choice.isnumeric():
            print("Please enter a valid number.")
            continue

        choice = int(choice)

        match choice:
            case 1:
                list_all_records(record_list)
            case 2:
                add_record()
            case 3:
                update_record()
            case 4:
                delete_record()
            case 5:
                search_record()
            case 6:
                print("Exiting HighPYve Tech Profile. Goodbye!")
                break
            case _:
                print("Invalid choice. Please select from the menu.")

main()