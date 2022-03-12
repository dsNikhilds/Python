#Calculator

def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mult(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2

operators = {
    "+":add,
    "-":sub,
    "*":mult,
    "/":div,
}



def calculator():
    repeat = True
    num1 = int(input("What is the first number\n"))
    while repeat:
        num2 = int(input("What is the second number\n"))
        print("Which of these operations you want to do?")
        for i in operators:
            print(i)
        operation_symbol = input("Pick a symbol from the operation symbol\n")
        
        answer = operators[operation_symbol](num1,num2)
        print(f"{num1} {operation_symbol} {num2} = {answer} ")
    
        if input(f"Type 'Y' to continue calculating with {answer}, or 'n' to start a new calculation. \n").lower()=="n":
            repeat = False
            calculator()
        else:
            num1 = answer

 
calculator()




