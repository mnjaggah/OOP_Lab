import unittest
import Customer_Acc 

class Customer_Acc_TestCases(unittest.TestCase):
    def setUp(self):
        self.m = Customer_Acc("Maria", 100)

    def test_Customer_Acc_instance(self):
        self.assertIsInstance(m, Customer_Acc, msg = 'The object should be an instance of the Customer_Acc class')

    def test_object_type(self):
        m = Customer_Acc('Maria', 100)
        self.assertTrue((type(m) is Customer_Acc), msg = 'The object should be a type of Customer Acc')


    def test_check_balance(self):
        self.assertEqual(self.m.balance, 100, msg='Invalid Account Balance')
    
    def test_deposit(self):
        self.m.deposit(50)
        self.assertEqual(self.m.balance, 150, msg='Check the Deposit method')
                        
    def test_withdraw(self):
        self.m.withdraw(90)
        self.assertEqual(self.m.balance, 60, msg='Check withdraw method')
     
    def test_sub_class(self):
        self.assertTrue(issubclass(Minimum_Customer_Acc_Bal, Customer_Acc), msg='Not a subclass of Customer_Acc')

if __name__ == '__main__':
    unittest.main() 
