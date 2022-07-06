# WHAT IS INHERITANCE?
"""
1. The concept of class inheritance is that a new class can be defined by extending an existing class
2. An existing class is called: parent class or superclass
3. A new class created based on the existing class is called: child class or subclass
4. A subclass can inherit some or all of the attributes and methods of the superclass
5. The benefits of inheritance are that we can reuse code and reduce complexity of a program
"""

# CLASS INHERITANCE SYNTAX:

class Parent:
    def __init__():
    # parent methods and attributes are defined here

class Child(Parent):
    # parent methods and attributes are inherited
    # child methods and attributes are defined here

# INHERITANCE EXAMPLE:
# We have a |Human| class and we want to add a |Wizard| class that can do everything the |Human| class can but more.

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self, direction):
        print(self.name, "walks to the", direction)
    
    def talk(self, speech):
        print(self.name, "says", speech)
    
class Wizard(Human):
    def cast_spell(self, spell):
        print(self.name, "casts", spell)

# Instead of creating |Wizard| class from scratch we inherit the parent methods and attributes from the |Human| class >
# by creating a |Superclass(Subclass)| relationship between the |Human| class and the |Wizard| class >
# the |Wizard| class is now a subclass of the |Human| superclass
# Objects created from the |Human| class can walk and talk
# Objects created from the |Wizard| class can walk(), talk() and cast_spells() instance methods().

# HOW TO OVERRIDE THE |init| METHOD OF THE PARENT/SUPERCLASS:
"""
1. We can also define an |init| method in a child class to give it its own attributes
2. If we do the |init| method will override the |init| method of the parent/superclass.
3. This means the child class will no longer have acces to the attributes of the parent/supeclass.
"""

class Parent:
    def __init__():

class Child(Parent):
    def __init__():

# THE |super()| FUNCTION SYNTAX RESOLVES THE OVERRIDE BY CALLING THE METHOD OF THE PARENT/SUPERCLASS:


class Parent:
    def __init__():

class Child(Parent):
    def __init__():
    super().__init__() # Calls the |__init__()| method of parent/superclass.

# This allows the child/subclass to have its own attributes and still inherit attributes from the parent

# A |super()| FUNCTION EXAMPLE:
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self, direction):
        print(self.name, "walks to the", direction)
    
    def talk(self, speech):
        print(self.name, "says", speech)
    
class Wizard(Human):
    def __init__(self, name, age, spell_points): # define |__init__| in |Wizard| to add instance of attribute |spell_points|. Now |name| and |age| attributes from |Human| class are no longer initialized.
        super().__init__(name, age)              # To resolve this use |super()| to call the |__init__| method() from the superclass |Human|
        self.spell_points = spell_points

    def cast_spell(self, spell):
        print(self.name, "casts", spell)
