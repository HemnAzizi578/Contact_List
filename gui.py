# Import tkinter module for creating GUI
import tkinter as tk
from tkinter import messagebox

# Import contact management functions from logic.py
import logic

# Load existing contacts from file at startup
contacts = logic.load_contacts()


# Function for adding a new contact through GUI
def gui_add():
    # Get input from name and phone entry fields
    name = entry_name.get()
    phone = entry_phone.get()
    if name and phone:
        # Add contact and show confirmation message
        logic.add_contact(contacts, name, phone)
        messagebox.showinfo("✅ Added", f"{name} added.")
        # Clear input fields after adding
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
    else:
        # Warn user if fields are empty
        messagebox.showwarning("⚠️ Error", "Please enter both name and phone.")


# Function for deleting a contact through GUI
def gui_delete():
    # Get input from name entry field
    name = entry_name.get()
    if name:
        # Check if contact exists
        if name in contacts:
            # Delete contact and show confirmation
            logic.delete_contact(contacts, name)
            messagebox.showinfo("🗑 Deleted", f"{name} deleted.")
            # Clear entry fields
            entry_name.delete(0, tk.END)
            entry_phone.delete(0, tk.END)
        else:
            # Warn if contact not found
            messagebox.showwarning("❌ Not Found", "Contact not found.")
    else:
        # Warn if no name is entered
        messagebox.showwarning("⚠️ Error", "Enter a name to delete.")


# Function for searching contacts through GUI
def gui_search():
    # Get input from search field
    query = entry_search.get()
    found = False
    results = ""
    # Search contacts for matching name or phone
    for name, phone in contacts.items():
        if query.lower() in name.lower() or query in phone:
            results += f"{name}: {phone}\n"
            found = True
    if found:
        # Show matching results in message box
        messagebox.showinfo("🔍 Results", results)
    else:
        # Inform user if no matches found
        messagebox.showinfo("❌ No Match", "No contact found.")


# Initialize main window
root = tk.Tk()
root.title("📒 Contact Manager")


# Create label and entry for Name
tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

# Create label and entry for Phone
tk.Label(root, text="Phone:").grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

# Create Add and Delete buttons
tk.Button(root, text="➕ Add", command=gui_add).grid(row=2, column=0, pady=5)
tk.Button(root, text="🗑 Delete", command=gui_delete).grid(row=2, column=1, pady=5)

# Create label and entry for Search
tk.Label(root, text="🔍 Search:").grid(row=3, column=0)
entry_search = tk.Entry(root)
entry_search.grid(row=3, column=1)

# Create Search button
tk.Button(root, text="Search", command=gui_search).grid(row=4, column=0, columnspan=2, pady=5)

# Run the GUI event loop
root.mainloop()
