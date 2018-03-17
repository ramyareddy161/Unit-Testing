import unittest
from problem19 import get_hcf

class TestGetHcf(unittest.TestCase):
    score = 0
    def tearDown(self):
        print('Running Total: ', TestGetHcf.score)
    def test_gethcf_method_1(self):
        self.assertEqual(get_hcf([], [(2, 5)]), [])
        TestGetHcf.score += 2
    
    def test_gethcf_method_2(self):
        self.assertEqual(get_hcf([], []), [])
        TestGetHcf.score += 3

    def test_gethcf_method_3(self):
        self.assertEqual(get_hcf([(2, 3), (3, 3), (11, 1)], [(5, 2)]), [])
        TestGetHcf.score += 5

    def test_gethcf_method_4(self):
        self.assertEqual(get_hcf([(2, 3), (5, 3), (17, 2)], [(2, 1), (3, 5), (5, 2), (19, 1)]), [(2, 1), (5, 2)])
        TestGetHcf.score += 5

    def test_gethcf_method_5(self):
        self.assertEqual(get_hcf([(2, 1), (11, 3), (19, 2), (7919, 4)], [(2, 2), (7, 1), (19, 1), (2687, 4)]), [(2, 1), (19, 1)])
        TestGetHcf.score += 10

if __name__ == '__main__':
    unittest.main()