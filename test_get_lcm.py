import unittest
from problem18 import get_lcm

class TestGetLcm(unittest.TestCase):
    score = 0
    def setUp(self):
        pass

    def tearDown(self):
        print('Running score: ', TestGetLcm.score)

    def test_getlcm_method_1(self):
        self.assertEqual(get_lcm([], [(2, 5)]), [(2, 5)])
        TestGetLcm.score += 2
    
    def test_getlcm_method_2(self):
        self.assertEqual(get_lcm([], []), [])
        TestGetLcm.score += 3

    def test_getlcm_method_3(self):
        self.assertEqual(get_lcm([(2, 1), (5, 2), (7, 2)], [(2, 2), (3, 1), (17, 2)]), [(2, 2), (3, 1), (5, 2), (7, 2), (17, 2)])
        TestGetLcm.score += 5

    def test_getlcm_method_4(self):
        self.assertEqual(get_lcm([(2, 1), (19, 1), (7919, 4)], [(2, 2), (17, 1), (2687, 4)]), [(2, 2), (17, 1), (19, 1), (2687, 4), (7919, 4)])
        TestGetLcm.score += 15

if __name__ == '__main__':
    unittest.main()