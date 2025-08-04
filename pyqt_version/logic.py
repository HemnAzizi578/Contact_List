# Load contacts from a file and return them as a dictionary
def load_contacts(filename="contacts.txt"):
    contacts = {}
    try:
        with open(filename, "r")as file:
            for line in file:
                # Split each line into name and phone number
                name, phone = line.strip().split(",")
                contacts[name]= phone
    except FileNotFoundError:
        # Ignore if the file does not exist
        pass
    return contacts

# Save the current contacts dictionary to a file
def save_contacts(contacts, filename="contacts.txt"):
    with open(filename, "w") as file:
        for name, phone in contacts.items():
            # Write each contact in the format: name,phone
            file.write(f"{name},{phone}\n")

# Add a new contact to the dictionary and save changes
def add_contact(contacts, name, phone):
    contacts[name] = phone
    save_contacts(contacts)

# Delete a contact by name if it exists
def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
    else:
        # Do nothing if contact name not found
        pass

# Print a list of all contacts (currently not implemented)
def list_contacts(contacts):
    print("📒 Contacts List:")
    for name, phone in contacts.items():
        pass  # No action defined yet

# Search for contacts by name or phone number
def search_by_name(contacts, query):
    results = {}
    for name, phone in contacts.items():
        if query.lower() in name.lower():
            results[name] = phone
    return results

def search_by_phone(contacts, query):
    results = {}
    for name, phone in contacts.items():
        if query in phone:
            results[name] = phone
    return results


