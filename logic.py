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
    print(f"✅ contacts {name} added.")

def delete_contact(contacts, name):
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑 contacts {name} Deleted.")
    else:
        print("❌ Contacts NotFound.")

def list_contacts(contacts):
    print("📒 Contacts List:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")

def search_contacts(contacts, query):
    found = False
    print(f"🔍 Search results for '{query}':")
    for name, phone in contacts.items():
        if query.lower() in name.lower() or query in phone:
            print(f"{name}: {phone}")
            found = True
    if not found:
        print("❌ No contact found.")
        pass

def main():
    contacts = load_contacts()

    while True:
        print("\n--- Contacts List Menu ---")
        print("1. Add New Contact")
        print("2. Delete Contact")
        print("3. Show All Contacts")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Select: ")

        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            add_contact(contacts, name, phone)
        elif choice == "2":
            name = input("Contact to Delete: ")
            delete_contact(contacts, name)
        elif choice == "3":
            list_contacts(contacts)
        elif choice == "4":
            query = input("Enter name to search: ")
            search_contacts(contacts, query)
        elif choice == "5":
            print("👋 Goodbye!")
            break
        else:
            print("Error")

main()
