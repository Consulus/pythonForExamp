import csv
import os

if os.path.exists("./Menu.csv") and os.path.getsize("./Menu.csv") > 0:
    print("File exist and no empty")
elif os.path.exists("./Menu.csv") == False:
    print("File not exist")
elif os.path.exists("./Menu.csv") and os.path.getsize("./Menu.csv") == 0:
    print("File exist and empty")    

# file = open("Menu.csv", "r")
# reader = csv.reader(file)
# print(len(reader))

# if len(rows) == 0:
    # file.close()
    
    # file = open("Menu.csv", "w")
    # reader = csv.reader(file)
    # rows = list(reader)
    
    # check = input("""
        # Please check what need to do:
            # 1 - Add name
            # 2 - Change name
            # 3 - Delete name
            # 4 - Print names
            # 5 - Exit programs
        # """)
    
    # while check.isdigit() == False:
        # check = input("""
        # Please check number:
            # 1 - Add name
            # 2 - Change name
            # 3 - Delete name
            # 4 - Print names
            # 5 - Exit programs
        # """)
    
    # check = int(check)
    
    # print([1,2,3,4,5].index(check) )
    
# file.close()

# def show(lis):
    # print(lis)

# def add():
    # print("im add menu")

# def change():
    # print("im change menu")

# def delete():
    # print("im delete menu")
