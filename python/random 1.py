#choosing random person to pay the bill
import random
name=input("enter names")
names_list=name.split(",")
len=len(names_list)
a=random.randint(0,len-1)
print(f"{names_list[a]} will pay the bill")

b=random.choice(names_list)
print(f"{b} will pay the bill")
