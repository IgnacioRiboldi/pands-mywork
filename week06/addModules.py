# Add Modules
# This program add modules to the students
# By Ignacio Riboldi

students = []

def readModules():
    return []

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

doAdd(students)
doAdd(students)
print(students)