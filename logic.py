def load_contacts(filename="contacts.txt"):
    contacts = {}
    try:
        with open(filename, "r")as file:
            for line in file:
                name, phone = line.strip().split(",")
                contacts[name]= phone
    except FileNotFoundError:
        pass
    return contacts

def save_contacts(contacts, filename="contacts.txt"):
    with open(filename, "w") as file:
        for name, phone in contacts.items():
            file.write(f"{name},{phone}\n")

def add_contact(contacts, name, phone):
    contacts[name] = phone
    save_contacts(contacts)

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
    else:
        pass

def list_contacts(contacts):
    print("📒 Contacts List:")
    for name, phone in contacts.items():
        pass

def search_contacts(contacts, query):
    found = False
    for name, phone in contacts.items():
        if query.lower() in name.lower() or query in phone:
            found = True
    if not found:
        pass

