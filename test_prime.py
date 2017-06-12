import unittest

from prime_number import getPrime  

def test_output_positive_numers_only(self):
    getResult=getPrime(10)
    for i in getResult:
        self.assertTrue(i>0)   
def test_if_value_is_integer(self):
        with self.assertRaises(TypeError):
            getPrime('success')      
def test_if_all_the_values_are_prime(self):
        result =getPrime(10)
        self.assertEqual(result,[2,3,5,7],msg="value is not a prime number")                           
if  __name__=='__main__':
    unittest.main()


   