def ran():
    import random
    
    small = input("Please Enter the small number: ")
    
    while small.isdigit() != True:
        small = input("Please Enter the small number: ")
    
    small = int(small)    
    
    big = input("Please Enter the big number: ")
    
    while big.isdigit() != True:
        big = input("Please Enter the big number: ")
    
    big = int(big)
    
    if small < big:
        comp_num = random.randint(small, big)
    else:
        comp_num = random.randint(big, small)
    
    return comp_num    

def think():
    
    print("I am thinking of a number...")
    answer = input("What number i think?")
    
    while answer.isdigit() != True:
        answer = input("What number i think?")
    
    answer = int(answer)
    
    return answer
    
def game():

    randomNumber = ran()
    choise = think()
    
    while True:
        
        if randomNumber == choise:
            print("Correct, you are win. The coorect number - " + str(randomNumber))
            return
        
        if randomNumber > choise:
            print("The input number is low then correct")
            choise = think()
            continue
        
        if randomNumber < choise:
            print("The input number is greater then correct")
            choise = think()
            continue

game()
    
        
