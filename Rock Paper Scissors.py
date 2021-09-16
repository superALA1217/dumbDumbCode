import random

Options = [0, 1, 2]

Score = int(0)

repeat = "yes"
while repeat.lower().strip() == 'yes':
    playerInput = input("Rock Paper Scissors: ").lower()

    if playerInput == "rock":
        playerInput = int(0)
    elif playerInput == "paper":
        playerInput = int(1)
    elif playerInput == "scissors":
        playerInput = int(2)
    elif playerInput == "fuck you":
        playerInput = int(4)
    else:
        print("Please choose an actual option")

    Computer = 3
    Computer = random.randint(0, 2)
# anadir el "int" a todas los cambios en el puntaje
    if playerInput == 0 and Computer == 0:
        print("We both choose Rock. It's a tie :|")
        print("Your score is: " + str(Score))
    elif playerInput == 0 and Computer == 1:
        print("You choose Rock and I choose paper. You Loose :(")
        Score -= int(1)
        print("Your score is: " + str(Score))
    elif playerInput == 0 and Computer == 2:
        print("You Choose Rock and I Choose Scissors. You Win:D")
        Score += int(1)
        print("Your score is: " + str(Score))
    elif playerInput == 1 and Computer == 0:
        print("You Choose Paper and I choose rock, You Win:D")
        Score += int(1)
        print("Your Score Is: " + str(Score))
    elif playerInput == 1 and Computer == 1:
        print("We both choose paper. Nobody wins :|")
        print("Your score is: " + str(Score))
    elif playerInput == 1 and Computer == 2:
        print("You choose paper and I choose Scissors. You Loose :(")
        Score -= int(1)
        print("Your score is: " + str(Score))
    elif playerInput == 2 and Computer == 0:
        print("You choose Scissors, I choose Rock. You Loose :(")
        Score -= int(1)
        print("Your score is: " + str(Score))
    elif playerInput == 2 and Computer == 1:
        print("You choose Scissors and I choose Paper. You Win :D")
        Score += int(1)
        print("Your score is: " + str(Score))
    elif playerInput == 2 and Computer == 2:
        print("We both choose Scissors. Nobody wins :|")
        print("Your score is: " + str(Score))
    elif playerInput == 4:
        Score -= int(1000000000)
        print("just because ur an asshole I gib u minus 2003km/h of points")