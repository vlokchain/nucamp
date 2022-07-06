# LOCAL SCOPE

# Variables decalred inside a function only exist inside that function
# When a function call ends the varaible is erased from the memory
# When a function is called again it is declared again

def Seattle():
    dogs = 500
    print("Seatlle has", dogs, "dogs.")

def Bellevue():
    dogs = 900
    print("Bellevue has", dogs, "dogs.")

# GLOBAL VARIABLE

x = 1
# x can be accessed here
def myFn():
    y = 2
# x and y can be accessed here

# MODIFYING GLOBAL VARIABLES

my_string = "global"

def main():
    my_string = "local"

main()
print(my_string)

"""
OUTPUT:
global
"""

# TO MODIFY THE GLOBAL VARIABLE TYPE:

my_string = "global"

def main():
    global my_string
    my_string = "local"

main()
print(my_string)