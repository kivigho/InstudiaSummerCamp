# Contact Book
contacts = {}

def add_contact(name, number):
    contacts[name] = number

def delete_contact(name):
    if name in contacts:
        del contacts[name]

def search_contact(name):
    return contacts.get(name, "Contact not found")

while True:
    choice = input("Enter choice (add/delete/search/exit): ")
    if choice == 'add':
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == 'delete':
        name = input("Enter name: ")
        delete_contact(name)
    elif choice == 'search':
        name = input("Enter name: ")
        print(search_contact(name))
    elif choice == 'exit':
        break
    else:
        print("Invalid input")
# To-Do List
tasks = []

def add_task(task):
    tasks.append(task)

def delete_task(task):
    if task in tasks:
        tasks.remove(task)

def view_tasks():
    return tasks

while True:
    choice = input("Enter choice (add/delete/view/exit): ")
    if choice == 'add':
        task = input("Enter task: ")
        add_task(task)
    elif choice == 'delete':
        task = input("Enter task: ")
        delete_task(task)
    elif choice == 'view':
        print(view_tasks())
    elif choice == 'exit':
        break
    else:
        print("Invalid input")


