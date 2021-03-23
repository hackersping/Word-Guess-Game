import random
print("To stop the game type Q")
score = 0
while True:
    num = random.randint(0,10)
    guess = input("Enter a number: ")
    if guess == "Q":
        print("Game Over")
        break
        
    guess_num = int(guess)
    if guess_num is num:
       print("Congress. You won")
       score += 10
       print("new score: ", score)
    
    else:
     print("You lose")
     print("The number was: ", num)
