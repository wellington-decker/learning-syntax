import random
my_list = ["rock", "paper", "scissors"]
def r_p_s(your_guess):
    my_computers_guess = random.choice(my_list)
    if your_guess == "rock" or your_guess == "paper" or your_guess == "scissors":
        if your_guess == "scissors" and my_computers_guess == "paper":
            print("You win: your_guess is -", your_guess + " " + "my_computers_guess is -", my_computers_guess)
        elif your_guess == "rock" and my_computers_guess == "paper":
            print("Computer wins: your_guess is -", your_guess + " " + "my_computers_guess is -", my_computers_guess)
        elif your_guess == "paper" and my_computers_guess == "scissors":
            print("Computer wins: your_guess is -", your_guess + " " + "my_computers_guess is -", my_computers_guess)
        elif your_guess == "paper" and my_computers_guess == "rock":
            print("You win: your_guess is -", your_guess + " " + "my_computers_guess is -", my_computers_guess)
        elif your_guess == "rock" and my_computers_guess == "scissors":
            print("You win: your_guess is -", your_guess + " " + "my_computers_guess is -", my_computers_guess)
        elif your_guess == "scissors" and my_computers_guess == "rock":
            print("Computer wins: your_guess is -", your_guess + " " + "my_computers_guess is -", my_computers_guess)
        else:
            print("Tie: your_guess is -", your_guess + " " + "my_computers_guess is -", my_computers_guess)
    else:
        print("Your guess was neither rock, paper nor scissors")
    print("---------------------------------------------")
    do_you_want_to_continue = input("Do you want to continue.............Enter \"Y\" for Yes and \"N\" for No:\n").lower()
    if do_you_want_to_continue == 'y':
        my_computers_guess = random.choice(my_list)
        your_guess = input("Enter your guess:\n").lower()
        print(r_p_s(your_guess))
    else:
        return "That's the end of the game"


your_guess = input("Pick between ROCK, PAPER, SCISSORS:\n").lower()
r_p_s(your_guess)