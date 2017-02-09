import unittest
import Customer_Acc 

class Customer_Acc_TestCases(unittest.TestCase):

    def test_Customer_Acc_instance(self):
        m = Customer_Acc('Maria', 100)
        self.assertIsInstance(m, Customer_Acc, msg = 'The object should be an instance of the Customer_Acc class')

    def test_object_type(self):
        m = Customer_Acc('Maria', 100)
        self.assertTrue((type(m) is Customer_Acc), msg = 'The object should be a type of Customer Acc')


    def test_check_balance(self):
        m = Customer_Acc('Maria', 100)
        self.assertEqual(m.balance, 100, msg='Invalid Account Balance')
    
    def test_deposit(self):
        m = Customer_Acc('Maria', 100)
        n = m.deposit(100)
        self.assertEqual(n.balance, 100, msg='Check Deposit method')
                        
    def test_withdraw(self):
        m = Customer_Acc('Maria', 100)
        n = m.withdraw(10)
        self.assertEqual(n, 90, msg='Check withdraw method')
        
    def test_invalid_operation(self):
        m = Customer_Acc('Maria', 100)
        n = m.withdraw(10)
        self.assertEqual(n.withdraw(1000), "invalid transaction", msg='Invalid transaction')

     
    def test_sub_class(self):
        self.assertTrue(issubclass(Minimum_Customer_Acc_Bal, Customer_Acc), msg='Not a subclass of Customer_Acc')

    def test_Minimum_Customer_Acc_Bal_instance(self):
        f = Minimum_Customer_Acc_Bal('Faith', 100)
        self.assertIsInstance(f, Minimum_Customer_Acc_Bal, msg = 'The object should be an instance of the Customer_Acc class')

    def test_object_type(self):
        f = Minimum_Customer_Acc_Bal('Faith', 100)
        self.assertTrue((type(f) is Minimum_Customer_Acc_Bal), msg = 'The object should be a type of Customer Acc')


    def test_check_balance(self):
        f = Minimum_Customer_Acc_Bal('Faith', 100)
        self.assertEqual(f.balance, 100, msg='Invalid Account Balance')
    
    def test_deposit(self):
        f = Minimum_Customer_Acc_Bal('Faith', 100)
        n = f.deposit(100)
        self.assertEqual(n.balance, 100, msg='Check Deposit method')
                        
    def test_withdraw(self):
        f = Minimum_Customer_Acc_Bal('Faith', 100)
        n = f.withdraw(10)
        self.assertEqual(self.c_account.balance, 90, msg='Check withdraw method')

if __name__ == '__main__':
    unittest.main() 
