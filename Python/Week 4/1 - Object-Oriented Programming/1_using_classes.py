# CLASS w/ ATTRIBUTE
# EXAMPLE #1 OF CLASS WITH A SINGLE ATTRIBUTE:

class Player:     # First letter after keyword |class| is capitalized
    max_hp = 300  # A class attribute set to: max hit points = 300

"""
NOTE:
The purpose of a class is to make objects.
The fancy term for this is called "instantiating an object."

OUTPUT FOR EXAMPLE #1:
300
300
"""

# OBJECT INSTANTIATION
class Player:
    max_hp = 300

player1 = Player()      # Declare name of variable where we want to store the object then we assign the class name as its value followed by the argument (if any/must beoutside codeblock/no indentation)
print(player1.max_hp)   # Accessing methods and attributes via dot notation: player1 = variable + max_hp = attribute
player2 = Player()
print(player2.max_hp)