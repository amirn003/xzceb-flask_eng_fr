import unittest
from machinetranslation import english_to_french, french_to_english

class TestE2f(unittest.TestCase): 
    def teste2f(self): 
        self.assertEqual(english_to_french("Null"), "Null")
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        

class TestF2e(unittest.TestCase): 
    def testf2e(self): 
        self.assertEqual(french_to_english("Null"), "Null") 
        self.assertEqual(french_to_english("Bonjour"), "Hello") 


unittest.main()