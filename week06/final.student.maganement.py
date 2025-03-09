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

def doAdd(students):
    currentStudents = {}
    currentStudents ["name"] = input ("Enter name: ")
    currentStudents ["modules"] = readModules()
    students.append(currentStudents)

def readModules():
    modules = []
    moduleName = input("\tEnter the first Module name (blank to quit): ").strip()
    
    while moduleName != "":
        module = {}
        module["name"] = moduleName
        module["grade"] = int(input("\t\tEnter grade: "))
        modules.append(module)
        moduleName = input("\tEnter next module name (blank to quit): ").strip()
    
    return modules


def displayModules(modules):
 print ("\tName \tGrade")
 for module in modules:
    print(f"\t{ module['name']} \t{ module['grade']}") 

def doView(students):
    for currentStudent in students:
        print(currentStudent["name"])
        displayModules(currentStudent["modules"])

students =[]
choice = displayMenu()
while choice != 'q':
    if choice == 'a':
        doAdd(students)
    elif choice == 'v':
        doView(students)
    elif choice !='q':
        print("\n\nplease select either a,v or q")
    choice=displayMenu()
