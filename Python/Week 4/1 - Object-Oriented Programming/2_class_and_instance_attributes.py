# CHANGE CLASS ATTRIBUTE
# EXAMPLE 1:

class Player:
    max_hp = 300

player1 = Player()
print(player1.max_hp)
player2 = Player()
print(player2.max_hp)

Player.max_hp = 650         # How to change the |class Player:| attribute
print(player1.max_hp)
print(player2.max_hp)

"""
EXAMPLE 1 OUTPUT :
300
300
650
650
"""
# INSTANCE ATTRIBUTES & THE CONSTRUCTOR METHOD

# INITIALIZE INSTANCE ATTRIBUTES INSIDE CLASS: 
""" 
NOTE: 
1. Instance attributes are stored per instance rather than on the class
2. When you change an instance attribute it does not affect the other instances
"""
# EXAMPLE 2:

class Player:
    def __init__(self, name, hp): # We can initialize instance attributes inside a class by definining a method called |init| and it must have parameter list. The first parameter |self| refers to object being created
        self.name = name          # |self| object + |name| string  = |name| instance attribute
        self.hp = hp              # |self| object + |hp  | intefer = |hp  | instance attribute
        self.score = 0            # No need to paremeterize every single attribute. We only need to pass in attributes via the parameter list where we want to set the initial value dynamically. We can setup attributes with a default initial value by declaring them in the constructor without adding them to the parameter list.

player1 = Player("Aaron", 1200)   # |self| parameter is only passed in when creating class: here only 2 parameters are passed in |name| = "Aron" and |hp| = 1200
player2 = Player("Irene", 1300)   # |player2| variable = |Player| class (|name| parameter, |hp| parameter)

print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score)
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score)

"""
OUTPUT:
P1: Aaron  -- HP: 1200 -- SCORE:  0
P2: Irene  -- HP: 1300 -- SCORE:  0
"""
player1.hp += 500                 # Adds/changes hp integer for player1
player1.score += 65               # Adds/changes score integer for playe1
print("P1:", player1.name, " -- HP:", player1.hp, "-- SCORE: ", player1.score)
print("P2:", player2.name, " -- HP:", player2.hp, "-- SCORE: ", player2.score)

"""
OUTPUT:
P1: Aaron  -- HP: 1700 -- SCORE:  65
P2: Irene  -- HP: 1300 -- SCORE:  0
"""