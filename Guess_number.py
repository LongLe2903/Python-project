import random

player_name = input("Please input your name: ")
print(f"Welcome {player_name} to the game!")
start_number = int(input("Please input the minimum number: "))
end_number = int(input("Please input the maximum number: "))
print(f"The guess number is from {start_number} to {end_number}")
guess_number = 0
comp_number = random.randint(start_number, end_number)
count = 0
count_limit = int(input("Please input the guess times: "))

while guess_number != comp_number:
    guess_number = int(input("Please input your guess number: "))
    count += 1
    if count > count_limit:
        print(f"Oh no, you get over {count_limit} times to guess")
        print("End game!")
        exit()
    if guess_number < comp_number:
        print("Your guess number is lower than real number, try again")
    if guess_number > comp_number:
        print("Your guess number is higher than real number")
print("You got the right number, good job!")
print(f"The number is: {guess_number}")

