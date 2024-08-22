
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
dict={
    "+":add,
    "-":sub,
    "*":multiply,
    "/":divide,
    }
def calculator():
    num1=float(input("enter number 1:"))
    for i in dict:
      print(i)
    contin=True
    while contin:
        operator=input("enter the operation:")
        num2=float(input("enter number 2:"))
        calc_function=dict[operator]
        output=calc_function(num1,num2)
        print(f"{num1}{operator}{num2}={output}")

        should_contin=input(f"enter y to continue with {output} or n to start a new calculation or any to exit").lower()
        if should_contin=='y':
           num1=output
        
        elif should_contin=='n':
           contin=False
           calculator()
        else:
           cotin=False
           exit(1)

calculator() 
     
        
        
        
        
        






