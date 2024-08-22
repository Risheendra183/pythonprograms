def greet(name):
    print(f"hi {name}")
    print("are u from cs")

greet("jenny")
greet("rishi")

def add(a,b):
    print(a+b)

add(62,58)
    
def greet(name,no,dept):
    print(f"HI{name}")
    print(f"Are you from {dept} department?")
    print(f"your roll  no.{no}")

greet("rishi",64,"csm")
#arguments single args ARE FIXED CANOT CHANGE
def sum(*numbers):
    c=0
    for i in numbers:
        c+=i
    print(f"sum is {c}")
sum(2,4,5,3)
def sums(a,*numbers):
    print(numbers)
    c=0
    for i in numbers:
          c+=i
    print(f"sum={c}")
sums(2,4,6)
  
    
    
#kwargs can change 
def info_person(**kwargs):
    for key,values in kwargs.items():
        print(key,values)


info_person(name="rishi",age=20,dept="CSE")
info_person(name="firoz",age=19,dept="csm")
