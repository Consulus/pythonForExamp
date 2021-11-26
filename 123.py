def enter():
    print("""
        1) Add to file
        2) View all records
        3) Delete a record
        4) Quit program
    """)
    choise = input("Enter the number of your selection: ")
    while choise.isdigit() == False:
        print("""
        1) Add to file
        2) View all records
        3) Delete a record
        4) Quit program
    """)
        choise = input("Enter the number!!!")
    return int(choise)

def add():
    import os
    import csv

    if os.path.exists("./Salaries.csv") and os.path.getsize("./Salaries.csv") > 0:
        print("File exist and no empty")
    elif os.path.exists("./Salaries.csv") == False:
        file = open("Salaries.csv", "w")
        file.close()
    elif os.path.exists("./Salaries.csv") and os.path.getsize("./Salaries.csv") == 0:
        print("File exist and empty") 

    file = open("Salaries.csv", "r")
    reader = csv.reader(file)
    rows = list(reader)
    num = len(rows) + 1

    file = open("Salaries.csv", "a")
    name = input("name: ")
    salary = input("salary of " + name + " : ")
    file.write(str(num) + ") " + name + " " + salary + "\n")
    file.close()       

def view():
    import csv

    file = open("Salaries.csv", "r")
    for i in file:
        print(i)

def delete():

    target = input("Please enter the number of list need to delete")

    import csv
    arr = []
    file = open("Salaries.csv", "r")
    reader = csv.reader(file)
    row = list(reader)

    for j in row:
        temp = j[0].split(")")
        if int(target) == int(temp[0]):
            continue
        arr.append(j)

    file = open("Salaries.csv", "w")
    num = 1
    for z in arr:
        name = z[0].split(" ")
        newRecord = str(num) +") " + name[1] + " " + name[2] + "\n"
        file.write(str(newRecord))
        num = num + 1
    file.close()

check = 0



while check != 4:
    check = enter()
    if check == 4:
        break
    elif check == 3:
        delete()
    elif check == 1:
        add()
    elif check == 2:
        view()    
    else:
        print("Incorrect number, please enter 1 - 4")    