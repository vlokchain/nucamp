wizard = "wizard"
elf = "Elf"
human = "Human"
orc = "Orc"

character_set = {"wizard", "elf", "human", "orc"}

wizard_hp = 70
elf_hp = 100
human_hp = 150
orc_hp = 80
dragon_hp = 300

wizard_dmg = 150
elf_dmg = 100
human_dmg = 20
orc_dmg = 130
dragon_dmg = 50

while True:
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")
    print("4. Orc")
    print("5. Exit")
    option = input("Choose your character:")
    if option == "1" or option.lower() == "wizard":
        character = wizard
        hp = wizard_hp
        dmg = wizard_dmg
        print("You have chosen the character: " + character)
        print("Health:", hp)
        print("Damage:", dmg)
        break
    elif option == "2" or option.lower() == "elf":
        character = elf
        hp = elf_hp
        dmg = elf_dmg
        print("You have chose the character: " + character)
        print("Health:", hp)
        print("Damage:", dmg)
        break
    elif option == "3" or option.lower() == "human":
        character = human
        hp = human_hp
        dmg = human_dmg
        print("You have chosen the character: " + character)
        print("Health:", hp)
        print("Damage:", dmg)
        break
    elif option == "4" or option.lower() == "orc":
        character = orc
        hp = orc_hp
        dmg = orc_dmg
        print("You have chosen the character: " + character)
        print("Health:", hp)
        print("Damage:", dmg)
        break
    elif option == "5" or option.lower() == "exit":
        print("You have exited the game!")
        quit()
    else:
        print("Unknown Character")

while True:
    dragon_hp = dragon_hp - dmg
    print("The", character, "damaged the Dragon!")
    print("The Dragon's health points are now:", hp)
    if dragon_hp <= 0:
        print("The Dragon has lost the battle")
        break
    hp = hp - dragon_dmg
    print("The Dragon strikes back at", character)
    print("The", character, "health points are now:", hp)
    if hp <= 0:
        print("The", character, "has lost the battle.")
        break
