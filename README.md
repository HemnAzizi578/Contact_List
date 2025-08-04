# 📒 Contact List App – PyQt6 Version

A simple and interactive contact management tool built with **PyQt6**.

> ⚠️ This is a PyQt-based version of the original project previously built using Tkinter.  
> You can find the Tkinter version in the `tkinter-version` branch.

## 🧩 Features

- Add, delete, and search contacts
- Search by name or phone number
- User interface designed with Qt Designer (.ui file)
- Contacts stored locally in a txt file

## 🚀 Getting Started

```bash
git clone https://github.com/HemnAzizi578/Contact_List.git
cd contact-list
pip install PyQt6
python main.py

📁 Project Structure
contact-list/
├── main.py              # Main application logic with PyQt UI integration
├── contact_form.ui      # UI layout file created in Qt Designer
├── logic.py             # Core functions: add, delete, search, load/save contacts
└── contacts.txt        # Auto-generated file for storing contact data

💡 Future Ideas
Edit contact information directly

Validate phone number input

Migrate to a database (SQLite or similar)

Made with ❤️ by Hemn