# INPUT FUNCTION: instructs Python to pause and read data from user
# Always passes data as string data type


name = input("What is your name")
print("Hello " + name + "!")
print(type(name))

"""
OUTPUT:
What is your name? 23
Hello 23!
<class 'str'>
"""
# USING INPUT TO BREAK OUT OF INFINITE LOOP

while True:
    print("1. Number One")
    print("2. Number Two")
    print("3. Number Three")
    option = input("Pick an option: ")
    if option == "1":
        print("You chose 1")
    elif option == "2":
        print("You chose 2")
    elif option == "3":
        print("Leaving the loop!")
        break
    else:
        print("Invalid command")
print("You have left the loop")

"""
OUTPUT:
1. Number One
2. Number Two
3. Number Three
Pick an option: 1
You chose 1
1. Number One
2. Number Two
3. Number Three
Pick an option: 2
You chose 2
1. Number One
2. Number Two
3. Number Three
Pick an option: abc
Invalid command
1. Number One
2. Number Two
3. Number Three
Pick an option: 3
Leaving the loop!
You have left the loop
"""