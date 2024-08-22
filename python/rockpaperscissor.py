import random
rock='✊'
paper='✋'
scissor='✌️'
list=[rock,paper,scissor]
user_chc=int(input("enter choice 0.rock 1.paper 2.scissor"))
if user_chc>=3 or user_chc<0:
    print("invalid chc ,you lose")
else:
    print(list[user_chc])
    comp_chc=random.randint(0,2)
    print(f"computer choice:{comp_chc}")
    
    print(list[comp_chc])
    if comp_chc==2 and user_chc==0:
        print("you won")
    elif comp_chc==0 and user_chc==2:
        print("you lose")
    elif comp_chc==user_chc :
        print("draw")
    elif comp_chc>user_chc:
        print("you lose")
    elif comp_chc<user_chc:
        print("you won")
        
       
        
