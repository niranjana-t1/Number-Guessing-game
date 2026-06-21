import random

secret_num=random.randint(1,30)
print("WELCOME TO NUMBER GUESSING GAME!\n")
attempts=0
def number_guessing(secret_num,guess):
    
    if guess==secret_num:
        print("You guessed right! ")
        return True
    elif guess>secret_num:
        print("Try lower.")
        return False
    elif guess<secret_num:
        print("Try higher.")
        return False

while True:
    guess=int(input("Enter your guess between 1 and 30 (both inclusive): "))
    if guess<1 or guess>30:
        print("\nPlease enter a number between 1 and 30.\n ")
        continue
    attempts+=1
    result=number_guessing(secret_num,guess)
   
    if result:
        print(f"You found the number in {attempts} attempts!\n")
        rep=input("Play again? (yes/no)\n")
        if rep=="yes":
            secret_num=random.randint(1,30)
            attempts=0
            continue
        else:
            break
