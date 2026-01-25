# Week 02 Lab - Rock, Paper, Scissors

choices = ["Rock", "Paper", "Scissors"]

playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")

if not playerChoice.isdigit():
    print("Error: Choice must be between 1 and 3.")
    quit()

playerChoice = int(playerChoice)

if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
    quit()

computerChoice = input("Enter computer's choice (1-3): ")

if not computerChoice.isdigit():
    print("Error: Choice must be between 1 and 3.")
    quit()

computerChoice = int(computerChoice)

if computerChoice < 1 or computerChoice > 3:
    print("Error: Choice must be between 1 and 3.")
    quit()

playerChoiceName = choices[playerChoice - 1]
computerChoiceName = choices[computerChoice - 1]

print("You chose:", playerChoiceName)
print("Computer chose:", computerChoiceName)

if playerChoice == computerChoice:
    print("It's a tie!")
elif playerChoice == 1 and computerChoice == 3:
    print("Rock beats Scissors - You win!")
elif playerChoice == 2 and computerChoice == 1:
    print("Paper beats Rock - You win!")
elif playerChoice == 3 and computerChoice == 2:
    print("Scissors beats Paper - You win!")
else:
    print("You lose!")

if playerChoiceName != "Rock":
    print("You didn't pick the classic Rock...")