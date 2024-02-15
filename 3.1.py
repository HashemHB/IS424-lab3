empoloyeeDB=dict()
choose="yes"
while(choose == "yes"):
    print("Pease Enter the Employee infotmation")
    name = input("Employee name :")
    salary = input("Employee's salary :")
    empoloyeeDB[name]=salary
    choose =input("Add more?")

print("closed!")
for key in empoloyeeDB:
    print(key ,":",empoloyeeDB[key])
