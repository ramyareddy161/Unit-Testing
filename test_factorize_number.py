from problem17 import factorize_number
import unittest

class TestFactorizeNumber(unittest.TestCase):
    score = 0
    def setUp(self):
        pass

    def tearDown(self):
        # print('Running score: ', TestFactorizeNumber.score)
        pass

    def test_method_1(self):
        self.assertEqual(factorize_number(1), [])
        TestFactorizeNumber.score += 2

    def test_method_2(self):
        self.assertEqual(factorize_number(6010), [(2, 1), (5, 1), (601, 1)])
        TestFactorizeNumber.score += 5

    def test_method_3(self):
        self.assertEqual(factorize_number(7865228921869442), [(2, 1), (7919, 4)])
        TestFactorizeNumber.score += 10

    def test_method_4(self):
        with self.assertRaises(ValueError):
            factorize_number(-10)
        TestFactorizeNumber.score += 3

    def test_method_5(self):
        with self.assertRaises(TypeError):
            factorize_number(3.2)
        TestFactorizeNumber.score += 5

if __name__ == '__main__':
    unittest.main()
    print('Hello World')