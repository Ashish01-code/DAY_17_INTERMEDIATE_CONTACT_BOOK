#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#CONTACT_BOOK_INFO_WITH_OOPS_AND_FILES
class ContactBook:
    def __init__(self,filename):
        self.filename=filename
        self.contact={}
        self.load()
    def add(self):
        name=input("ENTER NAME: ")
        if name in self.contact:
            print("NAME ALREADY EXISTS")
            return
        phone=input("ENTER PHONE NUMBER: ")
        self.contact[name]=phone
        self.save(name,phone)
    def save(self,name,phone):
        with open(self.filename,"a") as f:
            f.write(f"{name},{phone}\n")
        print("CONTACT SAVED SUCCESSFULLY")
    def view(self):
        print("\n----CONTACT LIST-----")
        try:
            with open(self.filename,"r") as f:
                for line in f:
                    name,phone=line.strip().split(",")
                    print(f"NAME: {name}| Phone: {phone}")
        except FileNotFoundError:
            print("NO CONTACTS FOUND")
    def search(self):
        Sname=input("ENTER NAME TO SEARCH")
        found=False
        try:
            with open(self.filename,"r") as f:
                for line in f:
                    name,phone=line.strip().split(",")
                    if name==Sname:
                        print(f"FOUND  NAME : {name},Phone: {phone}")
                        found=True
                        break
        except FileNotFoundError:
            print("FILES NOT FOUND")
        if not found:
            print("CONTACT NOT FOUND")
    def delete(self):
        Dname=input("ENTER THE NAME TO DELETE")
        if Dname not in self.contact:
            print("CONTACT NOT FOUND")
            return
        del self.contact[Dname]
        with open(self.filename,"w") as f:
            for name,phone in self.contact.items():
                f.write(f"{name},{phone}\n")
        print("CONTACT DELETED")
    def update(self):
        Uname=input("ENTER THE NAME TO UPDATE: ")
        if Uname not in self.contact:
            print("CONTACT NOT FOUND")
            return
        Unum=input("ENTER THE NUMBER")
        self.contact[Uname]=Unum
        with open(self.filename,"w") as f:
            for name,phone in self.contact.items():
                f.write(f"{name},{phone}\n")
        print("CONTACT UPDATED")
    def load(self):
        try:
            with open(self.filename,"r") as f:
                for line in f:
                    name,phone=line.strip().split(",")
                    self.contact[name]=phone
        except FileNotFoundError:
            pass
    def length(self):
        print("THE NUMBER OF CONTACTS IS : ",len(self.contact))
c1=ContactBook(r"E:\TEST\TEXT.txt")
while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Count the contacts")
    print("5. Delete a contact")
    print("6. Update contact")
    print("7. Exit")
    try:
        choice = int(input("Enter choice: "))
    except ValueError:
        print("Please enter a number.")
        continue
    if choice == 1:
        c1.add()
    elif choice == 2:
        c1.view()
    elif choice == 3:
        c1.search()
    elif choice==4:
        c1.length()
    elif choice==5:
        c1.delete()
    elif choice==6:
        c1.update()
    elif choice == 7:
        print("Exiting Contact Book...")
        break
    else:
        print("Invalid choice.")    


# In[ ]:





# In[ ]:




