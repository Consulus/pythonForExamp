import csv
import os

if os.path.exists("./Menu.csv") and os.path.getsize("./Menu.csv") > 0:
    print("File exist and no empty")
elif os.path.exists("./Menu.csv") == False:
    file = open("Menu.csv", "w")
    file.close()
elif os.path.exists("./Menu.csv") and os.path.getsize("./Menu.csv") == 0:
    print("File exist and empty")    

def showList():
    file = open("Menu.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    for i in rows:
        print(i)

def intro():
    check = input("""
        Please check what need to do:
            1 - Add name
            2 - Change name
            3 - Delete name
            4 - Print names
            5 - Exit programs
        """)    

    while check.isdigit() == False:
        check = input("""
        Please enter number in range 1 - 5:
            1 - Add name
            2 - Change name
            3 - Delete name
            4 - Print names
            5 - Exit programs
        """)    

    return int(check)




        

def add():
    file = open("Menu.csv", "a")
    name = input("Enter name: ")
    newRecord = name + "\n"
    file.write(str(newRecord))
    file.close()

def change():
    file = open("Menu.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    file.close()

    file = open("Menu.csv", "w")

    name = input("Please enter the name to change: ")
    while name not in rows:
        name = input("Name not in list, please enter another name: ")

    for i in rows:
        if i == name:
            file.write(str(name) + "\n")
        else:
            file.write(str(i) + "\n")
    file.close()


value = 0



while value != 5:
    value = intro()
    while value < 1 or value > 5:
        print("Please enter number in range 1 - 5")
        value = intro()

    if value == 1:
        add()
    if value == 2:
        change()
    if value == 3:
        print("aa")
    if value == 4:
        showList()
    if value == 5:
        print("Programm close")            






def delete():
    print("im delete menu")






# file = open("Menu.csv", "r")
# reader = csv.reader(file)
# print(len(reader))

# if len(rows) == 0:
#     file.close()
    
#     file = open("Menu.csv", "w")
#     reader = csv.reader(file)
#     rows = list(reader)
    
#     check = input("""
#         Please check what need to do:
#             1 - Add name
#             2 - Change name
#             3 - Delete name
#             4 - Print names
#             5 - Exit programs
#         """)
    
#     while check.isdigit() == False:
#         check = input("""
#         Please check number:
#             1 - Add name
#             2 - Change name
#             3 - Delete name
#             4 - Print names
#             5 - Exit programs
#         """)
    
#     check = int(check)
    
#     print([1,2,3,4,5].index(check) )
    
# file.close()


