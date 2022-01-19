import unittest

from classes.calcul import Calcul

class TestCalcul(unittest.TestCase):
    
    def testDemo(self):
        self.assertEqual( 1,1, "2 n'egale pas 1")
        
    def testAdd(self):
        calcul = Calcul()
        self.assertEqual(calcul.add(3,2), 5, "add ne renvoie pas 5")
        self.assertEqual(calcul.add(45,5), 50, "ne fait pas l'addition")
        self.assertRaises(TypeError, calcul.add("m", 4))
        self.assertIsInstance(calcul, Calcul)
        
