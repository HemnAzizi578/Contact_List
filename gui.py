import tkinter as tk
from tkinter import messagebox
import logic


contacts = logic.load_contacts()


def gui_add():
    name = entry_name.get()
    phone = entry_phone.get()
    if name and phone:
        logic.add_contact(contacts, name, phone)
        messagebox.showinfo("✅ Added", f"{name} added.")
        entry_name.delete(0, tk.END)
        entry_phone.delete(0, tk.END)
    else:
        messagebox.showwarning("⚠️ Error", "Please enter both name and phone.")

def gui_delete():
    name = entry_name.get()
    if name:
        if name in contacts:
            logic.delete_contact(contacts, name)
            messagebox.showinfo("🗑 Deleted", f"{name} deleted.")
            entry_name.delete(0, tk.END)
            entry_phone.delete(0, tk.END)
        else:
            messagebox.showwarning("❌ Not Found", "Contact not found.")
    else:
        messagebox.showwarning("⚠️ Error", "Enter a name to delete.")

def gui_search():
    query = entry_search.get()
    found = False
    results = ""
    for name, phone in contacts.items():
        if query.lower() in name.lower() or query in phone:
            results += f"{name}: {phone}\n"
            found = True
    if found:
        messagebox.showinfo("🔍 Results", results)
    else:
        messagebox.showinfo("❌ No Match", "No contact found.")



root = tk.Tk()
root.title("📒 Contact Manager")



tk.Label(root, text="Name:").grid(row=0, column=0)
entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1)

tk.Label(root, text="Phone:").grid(row=1, column=0)
entry_phone = tk.Entry(root)
entry_phone.grid(row=1, column=1)

tk.Button(root, text="➕ Add", command=gui_add).grid(row=2, column=0, pady=5)

tk.Button(root, text="🗑 Delete", command=gui_delete).grid(row=2, column=1, pady=5)

tk.Label(root, text="🔍 Search:").grid(row=3, column=0)
entry_search = tk.Entry(root)
entry_search.grid(row=3, column=1)

tk.Button(root, text="Search", command=gui_search).grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()