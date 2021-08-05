import random
my_list = ["rock", "paper", "scissors"]
my_computers_guess = random.choice(my_list)
my_guess = input("Enter your guess here:\n").lower()
if my_guess == "scissors" and my_computers_guess == "paper":
    print("You win: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
elif my_guess == "rock" and my_computers_guess == "paper":
   print("Computer wins: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
elif my_guess == "paper" and my_computers_guess == "scissors":
    print("Computer wins: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
elif my_guess == "paper" and my_computers_guess == "rock":
    print("You win: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
elif my_guess == "rock" and my_computers_guess == "scissors":
    print("You win: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
elif my_guess == "scissors" and my_computers_guess == "rock":
    print("Computer wins: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
else:
    print("Tie: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
print("---------------------------------------------")
do_you_want_to_continue = input("Do you want to continue.......Enter \"Y\" for Yes and \"N\" for No:\n").lower()
while do_you_want_to_continue == 'y':
    my_computers_guess = random.choice(my_list)
    my_guess = input("Enter your guess here:\n").lower()
    if my_guess == "scissors" and my_computers_guess == "paper":
        print("You win: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
    elif my_guess == "rock" and my_computers_guess == "paper":
        print("Computer wins: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
    elif my_guess == "paper" and my_computers_guess == "scissors":
        print("Computer wins: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
    elif my_guess == "paper" and my_computers_guess == "rock":
        print("You win: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
    elif my_guess == "rock" and my_computers_guess == "scissors":
        print("You win: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
    elif my_guess == "scissors" and my_computers_guess == "rock":
        print("Computer wins: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
    else:
        print("Tie: my_guess is -", my_guess + " " + "my_computers_guess is -", my_computers_guess)
    print("---------------------------------------------")
    do_you_want_to_continue = input("Do you want to continue............Enter \"Y\" for Yes and \"N\" for No:\n").lower()
else:
    print("That's the end of the game")