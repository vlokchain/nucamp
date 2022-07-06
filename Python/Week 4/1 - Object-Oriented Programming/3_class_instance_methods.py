class User:                                       # A |class| called |User|
    def __init__(self, name, email, password):    # With a constructor method and three instance attributes
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, password):          # How to define an isntance method within a class: its defined inside the class and that makes it a method instance.
        self.password = password
        print("Your password has been changed to", self.password)

user1 = User("jane", "jane@nucamp.co", "janespassword")  # This calls the |class User| to instantiate an object: |user1| variable = |User| class (|name|,|email|,|password|)
print(user1.password)                                    # Prints the password for variable |user1|
user1.change_password("bestpassword")                    # This calls the |def change_password| and changes the password of |user1| to "bestpassword"

"""
OUTPUT:
janespassword
Your password has been changed to bestpassword
"""