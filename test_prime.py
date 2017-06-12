import unittest

from prime_number import getPrime  

def test_output_positive_numers_only(self):
    getResult=getPrime(10)
    for i in getResult:
        self.assertTrue(i>0)                
if  __name__=='__main__':
    unittest.main()


   