import unittest

from classes.fizzbuzz import FizzBuzz

class TestFizzBuzz(unittest.TestCase):
    
    def setUp(self) -> None:
        self.classe = FizzBuzz()
    
    def tearDown(self) -> None:
        pass
    
    def testFizzBuzz(self):
        result = [1,2,"fizz",4,"buzz","fizz",7,8,"fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]
        result2 = [1,2,"fizz",4,"buzz"]
        
        self.assertTrue(isinstance(self.classe.fizzBuzz(), list), "le retour n'est pas une instance")
        self.assertEqual(len(self.classe.fizzBuzz()), 15, "la liste n'a pas une taille de 15")
        self.assertEqual(self.classe.fizzBuzz(5), result2, "la liste ne contient pas les bons éléments")
        self.assertEqual(self.classe.fizzBuzz(), result, "la liste ne contient pas les bons éléments")


if __name__ == "__main__":
    unittest.main()