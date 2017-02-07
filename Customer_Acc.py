#create a main class that will interact with a number of objects
class Customer_Acc(object):
    def __init__ (self, name, balance = 0.0):
        self.balance = balance
        self.name = name

    #define  withdraw method and deposit method in main class

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance
    
    def check_balance(self):
        return self.balance
    
    #create a class that specifies the minimum withdrawal that inherites
    #from the mainn class Customer_Acc


class Minimum_Customer_Acc_Bal(Customer_Acc):
    def __init__(self, min_balance = 20):
        Customer.__init__(self, name, balance = 0.0)
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            return "Your balance is insufficient."
        else:
            Customer_Acc.withdraw(amount)



    
