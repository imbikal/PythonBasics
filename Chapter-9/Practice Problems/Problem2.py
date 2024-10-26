import random

def game():
    print("You're playing the game..")
    score = random.randint(1, 62)

    # Open the file and check if it's empty by reading its content
    with open("highscore.txt", "r") as f:
        highscore = f.read()
    
    # If the file is empty or doesn't contain a valid score, initialize highscore to 0
    if highscore:
        highscore = int(highscore)
    else:
        highscore = 0

    print(f"Your score: {score}")
    
    # Update the highscore if the current score is greater
    if score > highscore:
        print(f"New highscore! Your new highscore is {score}")
        with open("highscore.txt", "w") as f:
            f.write(str(score))
    else:
        print(f"Highscore remains {highscore}")
    
    return score

# Ensure the highscore file exists before calling the game
open("highscore.txt", "a").close()  # This creates the file if it doesn't exist

# Call the game function
game()

     

