class User:                                       
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def change_name(self, new_name):
        self.name = new_name
        print("Your name has been changed to: ", new_name)

    def change_pin(self, new_pin):
        self.pin = new_pin
        print("Your PIN has been changed to: ", new_pin)

    def change_password(self, new_password):
        self.password = new_password
        print("Your password has been changed to: ",new_password)

class BankUser(User):                                                # SYNTAX: Subclass(Superclass)
    def __init__(self, name, pin, password):                         # Constructor method defining class intance attributes
        super().__init__(name, pin, password)                        # super() function allows the subclass BankUser have its own attributes and inherit the attributes of the User superclass
        self.balance = 0

    def show_balance(self):
        print(self.name ,"has an account balance of", str(self.balance))

    def _withdraw(self, withdraw):
        self.balance -= withdraw

    def _deposit(self, deposit):
        self.balance += deposit

    def transfer_money(self, receiving_user, amount):
            print("You are transferring $" + str(amount), "to", receiving_user.name)
            print("Authentication required")
            pincode = int(input("Enter your PIN: "))
            if pincode != self.pin:
                print("Invalid PIN. Transaction canceled.")
                return False
            print("Transfer authorized")
            print("Transferring $" + str(amount) + " to " + receiving_user.name)
            self.balance -= amount
            receiving_user.balance += amount
            return True

    def request_money(self, user, amount):
        print("You are requesting $" + str(amount), "from", user.name)
        print("User authentication is required...")
        pin = int(input("Enter " + user.name + "'s PIN: "))
        if pin != user.pin:
            print("Invalid PIN. Transaction canceled.")
            return False
        password = input("Enter your password: ")
        if password != self.password:
            print("Invalid password. Transaction canceled.")
            return False
        print("Request authorized")
        print(user.name + " sent $" + str(amount))
        user.balance -= amount
        self.balance += amount
        return True

""" Driver Code for Task 1 """
"""bankuser1 = User("Bob","1234","password")
print(bankuser1.name, bankuser1.pin, bankuser1.password)"""

""" Driver Code for Task 2 """
"""bankuser1 = User("Bob","1234","password")
print(bankuser1.name, bankuser1.pin, bankuser1.password)"""

""" Driver Code for Task 3"""
"""bankuser1 = BankUser("Bob","1234","password")
print(bankuser1.name, bankuser1.pin, bankuser1.password, bankuser1.balance)"""

""" Driver Code for Task 4"""
"""bankuser1 = BankUser("Bob","1234","password")
bankuser1.show_balance()
bankuser1._deposit(100)
bankuser1.show_balance()
bankuser1._withdraw(50)
bankuser1.show_balance()"""

""" Driver Code for Task 5"""
bankuser1 = BankUser("Bob","1234","password")
bankuser2 = BankUser("Alice","1111","alicepassword")
bankuser2._deposit(5000)
bankuser1.show_balance()
bankuser2.show_balance()
bankuser2.transfer_money(bankuser1, 500)
bankuser2.show_balance()
bankuser1.show_balance()
bankuser1.request_money(bankuser2, 250)
bankuser2.show_balance()
bankuser1.show_balance()