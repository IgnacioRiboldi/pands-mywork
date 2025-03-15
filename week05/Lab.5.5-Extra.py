# Extra exercise
# This program will create a list of data from students.
# By Ignacio Riboldi

student = {
    "name" : "",
    "modules"   : []
}
student["name"] = input("Insert studen name: ")

while True:
    module_name = input("Enter a module name (or press Enter to finish): ")
    if module_name == "":
        break
    
    try:
        grade = int(input(f"Enter the grade for {module_name}: "))
    except ValueError:
        print("Invalid input! Please enter a numeric grade.")
        continue

    student["modules"].append({
        "courseName": module_name,
        "grade": grade
    })

print("Student: {}".format(student["name"]))
for module in student["modules"]:
    print("{} : {}".format(module["courseName"], module["grade"]))