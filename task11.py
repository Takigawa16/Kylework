# Basic Data Management Program

def display_data(data):
    """Display all entries in the data."""
    if not data:
        print("No data available.")
    else:
        print("Current Data Entries:")
        for index, entry in enumerate(data):
            print(f"{index + 1}: {entry}")

def add_single_entry(data):
    """Add a single entry to the data."""
    entry = input("Enter the data entry: ")
    data.append(entry)  # Using append to add a single entry
    print(f"Added: {entry}")

def add_multiple_entries(data):
    """Add multiple entries to the data."""
    entries = input("Enter multiple data entries separated by commas: ")
    for entry in entries.split(","):
        data.append(entry.strip())  # Using append for each entry
    print("Entries added.")

def delete_entry(data):
    """Delete an entry from the data."""
    display_data(data)
    index = int(input("Enter the number of the entry to delete: ")) - 1
    if 0 <= index < len(data):
        removed_entry = data.pop(index)
        print(f"Deleted: {removed_entry}")
    else:
        print("Invalid index.")

def delete_all_data(data):
    """Delete all entries from the data."""
    confirmation = input("Are you sure you want to delete all data? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        data.clear()
        print("All data has been deleted.")

def update_entry(data):
    """Update an existing entry in the data."""
    display_data(data)
    index = int(input("Enter the number of the entry to update: ")) - 1
    if 0 <= index < len(data):
        new_entry = input("Enter the new data entry: ")
        old_entry = data[index]
        data[index] = new_entry
        print(f"Updated: {old_entry} to {new_entry}")
    else:
        print("Invalid index.")

def main():
    """Main function to run the program."""
    data = []
    
    while True:
        # Display menu options
        print("\nMenu")
        print("1. SHOW ALL DATA")
        print("2. ADD SINGLE DATA")
        print("3. ADD MULTIPLE DATA")
        print("4. DELETE")
        print("5. DELETE ALL DATA")
        print("6. UPDATE DATA")
        print("7. EXIT")

        choice = input("Enter your choice (1-7): ")

        # Handle user choices
        if choice == '1':
            display_data(data)
        elif choice == '2':
            add_single_entry(data)
        elif choice == '3':
            add_multiple_entries(data)
        elif choice == '4':
            delete_entry(data)
        elif choice == '5':
            delete_all_data(data)
        elif choice == '6':
            update_entry(data)
        elif choice == '7':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please select a number between 1 and 7.")

    main()
  
