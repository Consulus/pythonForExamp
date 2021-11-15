import random

def startMenu():
    print("""
    1) Addition
    2) Subtraction
    """)
    choise = input("Enter 1 or 2: ")

    if choise.isdigit() == False:
        while choise.isdigit() == False:
            choise = input("Please enter number: ")

    return int(choise)        
    

def firstDiapazon():
    first = random.randint(5,20)
    second = random.randint(5,20)
    result = str(first + second)

    print("Please enter sum  of " + str(first) + " and " + str(second) + " ?")
    answer = input("Please you answer: ")
    
    if answer.isdigit() == False:
        while answer.isdigit() == False:
            answer = input("Please you answer: ")
    
    if result == answer:
        print("Correct")
    else:
        print("Incorrect, the answer is " + result)

    
    
def secondDiapazon():
    first = random.randint(1,25)
    second = random.randint(25,50)
    result = str(second - first)

    print("Please enter difference  of " + str(second) + " and " + str(first) + " ?")
    answer = input("Please you answer: ")
    
    if answer.isdigit() == False:
        while answer.isdigit() == False:
            answer = input("Please you answer: ")
    
    if result == answer:
        print("Correct")
    else:
        print("Incorrect, the answer is " + result)





