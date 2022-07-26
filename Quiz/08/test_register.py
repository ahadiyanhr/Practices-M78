import unittest

from register_class import Register



class TestRegister(unittest.TestCase):
    
    def test_first_name(self):
        reg1 = Register('Hamid', 'Reza', 20, '09120720171', '0690108958', 'email@email.com')
        reg1.input_first_name('Saeed')
        self.assertEqual(reg1.first_name, 'Saeed')
        
    def test_last_name(self):
        reg2 = Register('Hamid', 'Reza', 20, '09120720171', '0690108958', 'email@email.com')
        reg2.input_last_name('Ahamad')
        self.assertEqual(reg2.last_name, 'Ahamad')
    
    def test_age(self):
        reg1 = Register('Hamid', 'Reza', 20, '09120720171', '0690108958', 'email@email.com')
        reg1.input_age(12)
        self.assertEqual(reg1.age, 12)
    
    def test_phone_number(self):
        reg1 = Register('Hamid', 'Reza', 20, '09120720171', '0690108958', 'email@email.com')
        reg1.input_phone('09120720171')
        self.assertEqual(reg1.phone_number, '09120720171')
    
    def test_id(self):
        reg1 = Register('Hamid', 'Reza', 20, '09120720171', '0690108958', 'email@email.com')
        reg1.input_id('0690108958')
        self.assertEqual(reg1.id, '0690108958')
        
    

if __name__ == '__main__':
    unittest.main()