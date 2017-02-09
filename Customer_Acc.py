#create a main class that will interact with a number of objects
class Customer_Acc(object):
    def __init__ (self, name, balance):
        self.balance = balance
        self.name = name

    #define  withdraw method and deposit method in main class

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            return "Warning!You are in debt",self.balance
        else:
            return self.balance
    
    def check_balance(self):
        return self.balance
    
    #create a class that specifies the minimum withdrawal that inherites
    #from the main class Customer_Acc


class Minimum_Customer_Acc_Bal(Customer_Acc):
    def __init__(self, name, balance):
        Customer_Acc.__init__(self, name, balance)
        self.min_balance = balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            return "You cannot withdraw!Your balance is insufficient."
        else:
            Customer_Acc.withdraw(amount)



    
