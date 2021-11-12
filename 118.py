def askNumber():
    num = input("Please enter the number: ")
    
    while num.isdigit() != True: 
        print("Please enter the number: ")
        num = input("Please enter the number: ")
    
    return int(num)    
    
def traker():
    n = askNumber()
    for number in range(1,n + 1):
        print(number)

traker()
        
        