# TO ACCESS CODE FROM A DIFFERENT FILE AND RELATE TO PRESENT CODE AS IN THIS FILE THERE ARE 2 METHODS

# METHOD 1:
# To use any functions or variables from the module from the |import| you must prepend the module name using dot notation

import first_module

first_module.greet("Albert Einstein")
print("My favorite ice cream flavor is", first_module.flavor)

# METHOD 2:

from first_module import greet, flavor

greet("Albert Einstein")
print("My favorite ice cream flavor is", flavor)