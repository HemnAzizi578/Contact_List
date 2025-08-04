from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6 import uic
from logic import load_contacts, save_contacts, add_contact, delete_contact, search_by_name, search_by_phone


class ContactApp(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("contact_form.ui", self)


        self.contacts = load_contacts()

        self.add_button.clicked.connect(self.add)
        self.delete_button.clicked.connect(self.delete)
        self.search_button.clicked.connect(self.search)

        self.name_input.textChanged.connect(self.check_inputs)
        self.phone_input.textChanged.connect(self.check_inputs)

        self.refresh_list()


    def add(self):
        name = self.name_input.text().strip()
        phone = self.phone_input.text().strip()

        if name and phone:
            add_contact(self.contacts, name, phone)
            self.name_input.clear()
            self.phone_input.clear()
            self.refresh_list()
        else:
            QMessageBox.warning(self, "Error", "Enter name and number.")


    def delete(self):
        name = self.name_input.text().strip()
        if name in self.contacts:
            delete_contact(self.contacts, name)
            self.name_input.clear()
            self.phone_input.clear()
            self.refresh_list()
        else:
            QMessageBox.information(self, "Not found", "Contact not found.")




    def check_inputs(self):
        if not self.name_input.text().strip() and not self.phone_input.text().strip():
            self.refresh_list()


    def search(self):
        name_query = self.name_input.text().strip()
        phone_query = self.phone_input.text().strip()

        if name_query:
            results = search_by_name(self.contacts, name_query)
        elif phone_query:
            results = search_by_phone(self.contacts, phone_query)
        else:
            self.refresh_list()
            return

        self.contact_list.clear()
        for name, phone in results.items():
            self.contact_list.addItem(f"{name}: {phone}")

            
    def refresh_list(self):
        self.contact_list.clear()
        for name, phone in self.contacts.items():
            self.contact_list.addItem(f"{name}: {phone}")


if __name__ == "__main__":
    app = QApplication([])
    window = ContactApp()
    window.show()
    app.exec()
