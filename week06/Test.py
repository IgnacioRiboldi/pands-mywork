
def readModules():
 moduleName = input("\tEnter the first Module name (blank to quit) :").strip()
 modules =[]
 while moduleName != "":
   module = {}
   module["name"]= moduleName
   module["grade"]=int(input("\t\tEnter grade:"))
   modules.append(module)
   
   moduleName = input("\tEnter next module name (blank to quit) :").strip()
   return modules