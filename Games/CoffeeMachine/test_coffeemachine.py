import unittest

from coffeemachine import CoffeeMachine, drinks


class TestCoffeeMachine(unittest.TestCase):
    def setUp(self):
        self.cm1 = CoffeeMachine(100, 100, 100, 50, 20)
        self.cm2 = CoffeeMachine(100, 100, 100, 50, 20)
        self.cm3 = CoffeeMachine(200, 150, 60, 100, 80)
 
    def test_equal(self):
       self.assertEqual(self.cm1, self.cm2)
    
    def test_notEqual(self):
       self.assertNotEqual(self.cm1, self.cm3)

    def test_makeDrink(self):
        self.cm1.makeDrink("latte")
        self.assertNotEqual(self.cm1, self.cm2)

    def test_drinkAvailable(self):
        self.assertTrue(self.cm1.checkDrinkExists("latte"))
        
    def test_drinkNotAvailable(self):
        self.assertFalse(self.cm1.checkDrinkExists("o-saft"))