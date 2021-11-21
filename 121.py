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
    for row in file:
        print(row)

def add():
    file = open("Menu.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    num = len(rows)

    file = open("Menu.csv", "a")
    name = input("name: ")
    file.write(str(num) + ") " + name + "\n")
    file.close()



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

    while int(check) < 1 or int(check) > 5:
        check = input("""
        Please enter number in range 1 - 5:
            1 - Add name
            2 - Change name
            3 - Delete name
            4 - Print names
            5 - Exit programs
        """)  

    return int(check)

def change():
    file = open("Menu.csv", "r")
    arr = []
    for i in file:
        start = i.index(' ')
        end = i.index('\n')
        arr.append(i[start + 1:end])
    
    nameToChange = input("What name need to change: ")
    while nameToChange not in arr:
        showList()
        nameToChange = input("Please enter the correct name need to change: ")
    newName = input("Please enter new name: ")
    index = arr.index(nameToChange)
    arr[index] = newName
    
    file = open("Menu.csv", "w")
    for name in arr:
        newRecord = str(arr.index(name)) + ') ' + name + "\n" 
        file.write(str(newRecord))
    file.close()

def deleteName():
    file = open("Menu.csv", "r")
    arr = []
    for i in file:
        start = i.index(' ')
        end = i.index('\n')
        arr.append(i[start + 1:end])
    
    nameToChange = input("What name need to delete: ")
    while nameToChange not in arr:
        showList()
        nameToChange = input("Please enter the correct name need to delete: ")
    arr.remove(nameToChange)
    
    file = open("Menu.csv", "w")
    for name in arr:
        newRecord = str(arr.index(name)) + ') ' + name + "\n" 
        file.write(str(newRecord))
    file.close()



def main():
    value = 0 
    while value != 5:
        value = intro()

        if value == 5:
            break

        if value == 1:
            add()
            showList()
            continue

        if value == 2:
            change()
            showList()
            continue

        if value == 3:
            deleteName()
            showList()
            continue
        
        if value == 4:
            showList()
            continue

main()