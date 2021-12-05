from programma import *

import unittest

class TestIpotenusa(unittest.TestCase):

    def test_primo_cateto_stringa(self):
        ''' se viene passata una stringa al primo parametro ci si aspetta una eccezione CatetiError '''
        with self.assertRaises(CatetoError):
            ipotenusa('cinque', 3)

    def test_secondo_cateto_stringa(self):
        ''' se viene passata una stringa al primo parametro ci si aspetta una eccezione CatetiError '''
        with self.assertRaises(CatetoError):
            ipotenusa(3,'cinque')

    def test_cateti_interi(self):
        ''' ipotenusa(3, 4): ci si aspetta il valore 5.0 '''
        self.assertEqual(ipotenusa(3, 4), 5.0)

    def test_cateti_float(self):
        ''' ipotenusa(3.0, 4.0): ci si aspetta il valore 5.0 '''
        self.assertEqual(ipotenusa(3.0, 4.0), 5.0)

    def test_cateti_misti1(self):
        ''' ipotenusa(3.0, 4): ci si aspetta il valore 5.0 '''
        self.assertEqual(ipotenusa(3.0, 4), 5.0)

    def test_cateti_misti2(self):
        ''' ipotenusa(3, 4.0): ci si aspetta il valore 5.0 '''
        self.assertEqual(ipotenusa(3, 4.0), 5.0)

if __name__ == '__main__':
    unittest.main()
