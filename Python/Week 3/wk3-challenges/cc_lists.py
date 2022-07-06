import random

diamonds = ["AD", "2D", "3D", "4D", "5D", "6D", "7D", "8D", "9D", "10D", "JD", "QD", "KD"]
hand = []

while diamonds:
    draw = input("Press enter to pick a card, or type Q to quit: ")
    if draw.upper() == "Q":
        break
    random_card = random.choice(diamonds)
    diamonds.remove(random_card)
    hand.append(random_card)
    print("Your hand:", hand)
    print("Remaining cards:", diamonds)
if not diamonds:
    print("There are no more cards to pick.")
