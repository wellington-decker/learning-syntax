import random
raffle = []
tries = int(input("How many times do you want to try:\n"))
attempts = 0
for i in range(1, 21):
    raffle.append(i)
    computer_guess = random.choice(raffle)
while attempts < tries: 
    num = int(input("Enter your guess:\n"))   
    if num > computer_guess:
        print("Guess is to large")
        attempts += 1
    elif num < computer_guess:
        print("Guess is to low")
        attempts += 1
    else:
        print("\n")
        print("Your guess and the computers guess are equal")
        print("||..Genius, you guessed right..||:)")
        break     
else:
    print("\n")
    print("||..Game Over..||:(")