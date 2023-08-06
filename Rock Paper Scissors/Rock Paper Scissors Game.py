import random as ran

arr = ["rock", "paper", "scissor", "lizard", "spock"]
user = 0
computer = 0
draw = 0
round = 1

def get_user_choice() -> str:
    while True:
        try:
            user_choice = int(input("Enter your choice (Rock: 1, Paper: 2, Scissors: 3, Lizard: 4, or Spock: 5): "))
            return arr[user_choice - 1]
                    
        except:
            print("Invalid input provided")
            continue
            

def get_computer_choice() -> str:
    # computer_choice = ran.randint(0, 2)
    # return arr[computer_choice]
    return ran.choice(arr)


def find_winner(userChoice, computerChoice) -> str:
    rules = {
        'rock': ['scissor', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissor': ['paper', 'lizard'],
        'lizard': ['paper', 'spock'],
        'spock': ['rock', 'scissor']
    }
    global computer
    global draw
    global user

    print()
    print("****")
    if userChoice == computerChoice:
        draw += 1
        print("It's a Tie, No one won!!")
        
    elif computerChoice in rules[userChoice]:
        user += 1
        print("Yippee!, You won!!")
        
    else:
        computer += 1
        print("Woohoo!, Computer won!!")
    print("****")
        


    
while True:
    if round != 1:
        choiceToPlay = str(input("Want to Play again (YES: 'y' _OR_ NO: 'n'): ")).strip()
            
        if choiceToPlay == "n":
            break
        elif choiceToPlay != "y":
            print("Invalid input provided.")
            continue
            
    
    userChoice = get_user_choice()
    computerChoice = get_computer_choice()
    round += 1
    find_winner(userChoice, computerChoice)
    print()
    print(f"Your wins: {user}, Computer wins: {computer}, Ties: {draw}")
    print()