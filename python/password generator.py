import random
letters=['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['@','#','$','*','_']
print("password :")
n_letters=int(input("enter no.of letters in password"))
n_numbers=int(input("enter no.of numbers in password"))
n_symbols=int(input("enter no.of symbols in password"))
password=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password+=char
for i in range(1,n_numbers+1):
    char=random.choice(numbers)
    password+=char
for i in range(1,n_symbols+1):
    char=random.choice(symbols)
    password+=char
print(password)
random.shuffle(password)
print(password)
passw=""
for char in password:
    password+=char
print(passw)


