def enter():
    print("""
        1) Add to file
        2) View all records
        3) Quit program
    """)
    choise = input("Enter the number of your selection: ")
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

check = 0



while check != 3:
    check = enter()
    if check == 3:
        break
    elif check == 1:
        add()
    elif check == 2:
        view()    
    else:
        print("Incorrect number, please enter 1 - 3")    