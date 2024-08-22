
import random
import logo_art
easylevelattempts=10
hardlevelattempts=5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return easylevelattempts
    else:
        return hardlevelattempts
def check_answer(guessed_number,answer,attempts):
    if guessed_number<answer:
        print("your guessed number is too low")
        return attempts-1
    elif guessed_number>answer:
        print("your guess is too high")
        return attempts-1
    else:
        print(f"your guess is right...the answer is {answer}")
    
    
    
def game():
    print(logo_art.logo)
    print("Let me think a no b/w 1to 50") 
    answer=random.randint(1,50)
    print(answer)
    level=input("choose level of difficulty...Type 'easy' or 'hard'")
    attempts=set_difficulty(level)
    guessed_number=0
    while guessed_number!=answer:
        print(f"you have{attempts} attempts remaining to guess the number")
        guessed_number=int(input("guess a number"))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts==0:
             print("you are out guess ....you lose!")
        elif guessed_number==answer:
             guessed_number=answer

game()
