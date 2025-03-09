# Student Management
# This progam will help with the management of the students.
# By Ignacio Riboldi

def displayMenu():
    print("What would you like to do?")
    print("\t(a) Add new Student")
    print("\t(v) View Students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):".strip())
    return choice

def doAdd():
    print("Addind")

def doView():
    print("Viewing")


choice = displayMenu()
while(choice !='q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print("\n\nPlease select either a,v or q")
    
    choice = displayMenu()