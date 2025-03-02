# Student
# This program store student information and print it out.
# By Ignacio Riboldi

student = {
    "name" : "Ignacio",
    "modules" : [
        {
        "courseName" : "Programming",
         "grade" : 45
        },
        {
        "courseName" : "History",
         "grade" : 99
        }
    ]
}
print ("Student: {}".format(student["name"])) 
for module in student["modules"]: 
    print("\t {} \t: {}".format(module["courseName"], module["grade"])) 