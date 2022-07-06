import random

high_score = 0

def dice_game():
    global high_score
    while True:
        print("Current High Score:", high_score)
        print("1) Roll Dice")
        print("2) Leave Game")
        user_choice = input("Enter your choice:")
        if user_choice == "1":
            dice_one = random.randint(1, 6)
            dice_two = random.randint(1, 6)
            total = dice_one + dice_two
            print("\nYou roll a...", dice_one)
            print("\nYou roll a...", dice_two)
            print("\nYou have rolled a total of:", dice_one + dice_two)
            if total > high_score:
                print("\nNew high score!")
                continue
        elif user_choice == "2":
            print("Goodbye!")
        quit()

dice_game()
