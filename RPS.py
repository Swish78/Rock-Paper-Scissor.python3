import random

countu = 0
countc = 0
choice = ["Rock", "Paper", "Scissor"]
print(choice)
print('Enter number of times you want to play this game: ')
for _ in range(int(input())):
    user_choice = input("Enter your choice(from aforementioned choices):")
    comp_choice = random.choice(choice)
    if user_choice == "Rock":
        print('Computers choice: ', random.choice(choice))
        if comp_choice == "Paper":
            print("oopsie")
            countc = countc + 1
        elif comp_choice == "Scissor":
            print("You won")
            countu = countu + 1
        elif comp_choice == "Rock":
            print("Damn,match tied")
    if user_choice == "Scissor":
        print('Computers choice: ', random.choice(choice))
        if comp_choice == "Paper":
            print("oopsie")
            countc = countc + 1
        elif comp_choice == "Scissor":
            print("Damn,match tied")
        elif comp_choice == "Rock":
            print("You won")
            countu = countu + 1
    if user_choice == "Paper":
        print('Computers choice: ', random.choice(choice))
        if comp_choice == "Paper":
            print("Damn,match tied")
        elif comp_choice == "Scissor":
            print("oopsie")
            countc = countc + 1
        elif comp_choice == "Rock":
            print("You won")
            countu = countu + 1
    print("Your score is:", countu)
    print("Computer's score is:", countc)
if countu > countc:
    print("Congrats, You won..Hurray :) ")
elif countc > countu:
    print("Better luck next time :( ")
else:
    print("LOL, Match tied")
