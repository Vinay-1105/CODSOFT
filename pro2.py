# Python program to prompt the user to choice between Rock, Paper, Scissors.
# import random module 
import random 
options = ['Rock', 'Paper', 'Scissors']
user_Score, computer_Score=0, 0
total_Rounds=3

for i in range(total_Rounds):
    user_Option=int(input('Press 1 for Rock, 2 for Paper, 3 for Scissors: '))
    user_Choice=options[user_Option-1]

    # randint() inbuilt function is used for generating random value between 0 and 2.
    computer_Choice=options[random.randint(0,2)]
    
    # Display user and computer's choices
    print(f'User choose: {user_Choice}')
    print(f'Computer choose: {computer_Choice}')
    
    result="It's a Draw!"

    if user_Choice=="Rock":
        if computer_Choice=="Paper":
            result="Computer won this round!"
            computer_Score+=1
        elif computer_Choice=="Scissors":
            result="User won this round!"
            user_Score+=1
    elif user_Choice=="Paper":
        if computer_Choice=="Scissors":
            result="Computer won this round!"
            computer_Score+=1 
        elif computer_Choice=="Rock":
            result="User won this round!"
            user_Score+=1
    elif user_Choice=="Scissors":
        if computer_Choice=="Rock":
            result="Computer won this round!"
            computer_Score+=1
        elif computer_Choice=="Paper":
            result="User won this round!"
            user_Score+=1
    print(result + '\n')

    print(f'User score: {user_Score}')
    print(f"Computer's score: {computer_Score}")
# Comparing the two scores and determining the winner.
if user_Score>computer_Score:
    print('User won most rounds!')
elif computer_Score>user_Score:
    print('Computer won most rounds!')
else:
    print("Draw")


        