import pickle

# Define file to store contacts
CONTACTS_FILE = 'contacts.pkl'

def load_contacts():
    """Load contacts from the file."""
    try:
        with open(CONTACTS_FILE, 'rb') as file:
            return pickle.load(file)
    except (FileNotFoundError, EOFError):
        return {}

def save_contacts(contacts):
    """Save contacts to the file."""
    with open(CONTACTS_FILE, 'wb') as file:
        pickle.dump(contacts, file)

def add_contact(contacts):
    """Add a new contact."""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {'phone': phone, 'email': email, 'address': address}
    print("Contact added.")

def view_contacts(contacts):
    """Display the list of all contacts."""
    if not contacts:
        print("No contacts available.")
        return
    print("\nContact List:")
    for name, details in contacts.items():
        print(f"Name: {name}, Phone: {details['phone']}")

def search_contact(contacts):
    """Search for a contact by name or phone number."""
    search_term = input("Enter the name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True
    if not found:
        print("No contact found.")

def edit_contact(contacts):
    """Edit contact details."""
    name = input("Enter the name of the contact to edit: ")
    if name in contacts:
        print("Leave the field empty if you don't want to change it.")
        phone = input(f"Enter new phone number (current: {contacts[name]['phone']}): ")
        email = input(f"Enter new email address (current: {contacts[name]['email']}): ")
        address = input(f"Enter new address (current: {contacts[name]['address']}): ")
        
        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address
        
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contact(contacts):
    """Delete a contact."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

def add_fake_contacts(contacts):
    """Add fake contacts for testing purposes."""
    fake_contacts = {
        "John Doe": {"phone": "555-1234", "email": "john.doe@example.com", "address": "123 Elm Street"},
        "Jane Smith": {"phone": "555-5678", "email": "jane.smith@example.com", "address": "456 Oak Avenue"},
        "Alice Johnson": {"phone": "555-8765", "email": "alice.johnson@example.com", "address": "789 Pine Road"},
        "Bob Brown": {"phone": "555-4321", "email": "bob.brown@example.com", "address": "101 Maple Lane"}
    }
    contacts.update(fake_contacts)
    print("Fake contacts added.")

def main():
    contacts = load_contacts()
    
    # Optionally add fake contacts for testing
    add_fake = input("Would you like to add fake contacts for testing? (y/n): ").lower()
    if add_fake == 'y':
        add_fake_contacts(contacts)
    
    while True:
        print("\nContact Book Application")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option (1/2/3/4/5/6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            edit_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
