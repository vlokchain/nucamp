import random

# Task 1: Guess the number through user input

def guess_random_num(tries, start, stop):                      # A function |guess_random_num| w/ parameters |tries|, |start| and |stop|
    random_num = random.randint(start, stop)                   # |random| module to generate a random number between: |start| and |stop| itegers
    while tries:
        print("Number of tries left:", tries)                  # Print number of tries remaining
        guess = int(input("Guess a number between " + str(start) + " and " + str(stop) + ": "))            # Prompt user to input a guess
                                                               # Comparing the number guessed to the target number
        if guess == random_num:                                # If they are equal:
            print("You guessed the correct number!")           # print a success message:
            return                                             # and return out of the function
        if guess < random_num:                                 # If the number guessed is less than the target number:
            print("Guess higher!")                             # print "Guess higher!"
        else:                                                  # If the number guessed is greater than the target number:
            print("Guess lower!")                              # Print "Guess lower!"
        tries -= 1                                             # Decrement the value of tries by 1.
    print("You have failed to guess the number:", random_num)  # If guess not successful when tries = 0 print a failure message.

# Task 2: Guess the number programmatically through linear search

def guess_random_num_linear(tries, start, stop):                          # A function called |guess_random_num_linear| w/ parameters |tries|, |start| and |stop|
    random_num = random.randint(start, stop)                              # |random| module to generate a random number between: |start| and |stop| itegers
    print("The number for the program to guess is:", random_num)          # 
                                                                          # Every time the computer makes a comparison, that is one guess:
    for num in range(start, stop+1):
        if not tries:
            print("The program has failed to guess the correct number.")
            return
        print("Number of tries left:", tries) 
        print("The program is guessing...", num)
        if num == random_num: 
            print("The program has guessed the correct number!")
            return
        tries -= 1                                                        # Decrement the tries variable and stop the function

# Task 3: Guess the number programmatically using binary search

def guess_random_num_binary(tries, start, stop):                          # A function |guess_random_num_binary| w/ parameters |tries|, |start| and |stop|
    random_num = random.randint(start, stop)                              # |random| module to generate a random number between: |start| and |stop| itegers
    print("Random number to find:", random_num)
    lower_bound = start
    upper_bound = stop
    while tries:
        pivot = (lower_bound + upper_bound) // 2
        if pivot == random_num:
            print("Found it!", random_num)
            return
        if pivot > random_num:
            print("Guessing lower!")
            upper_bound = pivot - 1
        else:
            print("Guessing higher!")
            lower_bound = pivot + 1
        tries -= 1
    print("Your program failed to find the number.")

guess_random_num(5, 0, 10)
guess_random_num_linear(5, 0, 10)
guess_random_num_binary(5, 0, 100)