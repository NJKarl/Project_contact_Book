import numpy as np
import pandas as pd
import json
import os
import re

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

#----------------------------------------------------------------------
class Contact_Book:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

#----------------------------------------------------------------------
    def validate_email(self, email):
        if not email:
            print ("Email is empty, please enter an email!")
            return False
        mail_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(mail_pattern,email):
            return True
        else:
            return False

#----------------------------------------------------------------------
    def validate_phone(self, phone):
        if not phone:
            print("Phone number cannot be empty")
            return False
        clean_phone =re.sub(r'[\s\-\(\)\+]','', phone)

    #In the international system, a typical phone number may range from 9 to 11 digits. However,
    #  we'll allow a greater range to include extreme cases.
        if clean_phone.isdigit() and 8<=len(clean_phone)<=15:
            return True
        else:
            return False
#----------------------------------------------------------------------
    def load_contacts(self):
        try:
            if os.path.exists(self.filename):
                with open (self.filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.contacts=[Contact(
                        contact_data["name"],
                        contact_data["phone"],
                        contact_data["email"]
                        )for contact_data in data]
                print (f"{len(self.contacts)} contacts charged")
        except Exception as e :
            print (f" Error when loading:{e}")
            self.contacts = []

#----------------------------------------------------------------------
    def add_contact(self,name,phone,email):

        val_mail = self.validate_email(email)
        if not val_mail:
            print("Invalid email format")
            return False

        val_phone= self.validate_phone(phone)
        if not val_phone:
            print("Invalid phone number:the phone number should be 8-15 digits.")
            return False

        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print (f"The contact {name} already exists")
                return False

        self.contacts.append(Contact(name, phone, email))
        print (f"Contact {name} added successfully")
        return True
#----------------------------------------------------------------------
    def view_contacts(self):
        if not self.contacts:
            print ("No contact founded")

        print ("\n=== All Contacts ===")

        ordering_contacts= sorted (self.contacts, key= lambda x: x.name.lower())

        for i, contact in enumerate(ordering_contacts,start=1):
            print (f"{i}. {contact.name} | {contact.phone} | {contact.email}")
        print ("="*50)
        print (f"Total: {len(self.contacts)} contacts")


#----------------------------------------------------------------------
    def search_contact(self):
        if not self.contacts:
            print ("No contact found")
            return[]

        search_name= input ("Enter name to search: ")
        search_name= search_name.lower()

        found_contacts=[]

        for contact in self.contacts:
            if search_name in contact.name.lower():
                found_contacts.append(contact)

        if found_contacts:
            print (f"\n{len(found_contacts)} contacts found with '{search_name}' :")
            for i, contact in enumerate(found_contacts, 1):
                print (f"{i}. {contact.name} | {contact.phone} | {contact.email}")
        else:
            print(f"No contact found with '{search_name}'.")

        return found_contacts

#----------------------------------------------------------------------
    def delete_contact(self):

        if not self.contacts:
            print ("No contact to delete")
            return False

        name = input(f"Enter name of contact to delete:").lower()
        found_contacts=[]

        for contact in self.contacts:
            if name in contact.name.lower():
                found_contacts.append(contact)

        if not found_contacts:
            print(f"No contact found with '{name}'.")
            return False

        if len(found_contacts)==1:
            delete_contact = found_contacts[0]
            y_n= input (f'Are you sure you want to delete "{delete_contact.name}"? (yes/no):')
            if y_n.lower() =="yes":
                self.contacts.remove (delete_contact)
                print(f"Contact '{delete_contact.name}' deleted! ")
                return True
            else:
              print ("No contact deleted!")
              return False

        else: #several contacts have the same name
            print("\nMany contacts found, which one do you want to remove?")
            for i,contact in enumerate(found_contacts,1):
                print (f"{i}. {contact.name} | {contact.phone} | {contact.email}")

            try:
                n = int(input("Please enter the number of the contact you want to remove from your Contact Book: "))
                if 1<= n <= len (found_contacts):
                    delete_contact = found_contacts[n-1]

                    y_n= input (f'Are you sure you want to delete "{delete_contact.name}"? (yes/no):')
                    if y_n.lower() =="yes":
                        self.contacts.remove (delete_contact)
                        print(f"Contact '{delete_contact.name}' deleted! ")
                        return True
                    else:
                      print ("No contact deleted!")
                      return False
                else:
                    print ("Invalid number")
                    return False
            except ValueError:
                print ("Enter a valid number.")
                return False

#----------------------------------------------------------------------
    def edit_contact(self):
        if not self.contacts:
            print("No contact to edit")
            return False

        name = input(f"Enter name of contact to edit:").lower()

        found_contacts = []
        for contact in self.contacts:
            if name in contact.name.lower():
                found_contacts.append(contact)

        if not found_contacts:
            print (f"No contact found with '{name}' !")
            return False

        if len(found_contacts)==1:
            edit_contact = found_contacts[0]
        else:
            print("\nMany contacts found, which one do you want to remove?")
            for i,contact in enumerate(found_contacts,1):
                print (f"{i}. {contact.name} | {contact.phone} | {contact.email}")

            try:
                n = int(input("Please enter the number of the contact you want to edit from your Contact Book: "))
                if 1<= n <= len (found_contacts):
                    edit_contact = found_contacts[n-1]
                else:
                    print ("Invalid Number")
                    return False
            except ValueError:
                print ("Enter a valid number.")
                return (False)

        print("\nCurrent contact info: ")
        print(f" Name:{edit_contact.name}")
        print(f" Phone:{edit_contact.phone}")
        print(f" Email:{edit_contact.email}")

        new_name = input(f"Enter new name [{edit_contact.name}]").strip()
        new_phone= input(f"Enter new phone [{edit_contact.phone}]").strip()
        new_email= input(f"Enter new email [{edit_contact.email}]").strip()

        if new_name:
            edit_contact.name= new_name

        if new_phone:
            val_phone = self.validate_phone(new_phone)
            if not val_phone:
                print("Invalid phone number:the phone number should be 8-15 digits.")
                return False
            edit_contact.phone= new_phone

        if new_email:
            val_mail = self.validate_email(new_email)
            if not val_mail:
                print("Invalid email!")
                return False
            edit_contact.email= new_email

        print ("Contact updated !")
        return True
#----------------------------------------------------------------------
    def save_contacts(self):
        try:
            contact_data = []
            for contact in self.contacts:
                contact_data.append({
                    "name": contact.name,
                    "phone":contact.phone,
                    "email":contact.email
                })
            with open(self.filename, 'w', encoding= 'utf-8') as file:
                json.dump(contact_data, file, indent=2, ensure_ascii= False)
            print(f"{len(self.contacts)} contacts saved to {self.filename}")
            return True

        except Exception as e:
            print(f"Error saving contacts: {e}")
            return False
#----------------------------------------------------------------------
    def menu(self):
        print("\n" + "="*40)
        print("Contact Book")
        print("="*40)
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Edit Contact")
        print("5. Delete Contact")
        print("6. Save and Exit")
        print("\n\n")
        print("Choose an option (1-6)")
#----------------------------------------------------------------------
    def run(self):
        while True:
            self.menu()
            n= input("Choose an option (1-6)").strip()

            if n=="1":
                name= input ("Enter full name").strip()
                phone= input("Enter phone number").strip()
                email = input("Enter email adress").strip()
                self.add_contact(name,phone,email)

            elif n =="2":
                self.view_contacts()

            elif n== "3":
                self.search_contact()

            elif n =="4":
                self.edit_contact()

            elif n=="5":
                self.delete_contact()

            elif n=="6":
                self.save_contacts()
                break
            else:
                print ("Invalid choice, Please enter a number between 1-6.")



if __name__=="__main__":
    book = Contact_Book()
    book.run()
    #book.delete_contact()
    #book.add_contact("Alice Martin", "+33766645239", "alicem@gmail.com")
    #book.add_contact("Bob Dupont", "+41766645239", "bob@gmail.com")
    #book.add_contact("Alice Johnson", "+33612345678", "alicej@email.com")
    #book.add_contact("Karl Johann Ngankam", "+33766645239", "karl@gmail.com")
    #book.view_contacts()


    #book.view_contacts()

    #book.delete_contact()  # Devrait trouver 2 contacts et demander lequel supprimer
    #book.delete_contact('Karl Ngankam')
    #book.edit_contact("Bob Dupont")