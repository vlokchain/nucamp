# TYPE CASTING (TYPE CONVERSION)

"""
Other languages like JavaScript perform automatic type conversion.
Python does not perform automatic type conversion. You must convert types yourself.
"""

# str(arg):    will return as a string
# int(arg):    will return as integer (must contain a number)
# float(arg):  will return a float (must contain a number)

total_cash = 0
user_input = input("Enter amount to transfer: ")
total_cash = total_cash + float(user_input)
print("Total cash is now: ")
print(total_cash)
