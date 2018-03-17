import unittest
from problem6 import top_chars

class TestTopChars(unittest.TestCase):
    score = 0
    def tearDown(self):
        print('Running Total: ', TestTopChars.score)

    def test_topchar_method_1(self):
        with self.assertRaises(TypeError):
            top_chars(None, 10)
        TestTopChars.score += 1

    def test_topchar_method_2(self):
        with self.assertRaises(TypeError):
            top_chars('hello', 'w')
        TestTopChars.score += 1

    def test_topchar_method_3(self):
        with self.assertRaises(ValueError):
            top_chars('hello', -1)
        TestTopChars.score += 1

    def test_topchar_method_4(self):
        self.assertEqual(top_chars('acceeeffff', 2), [('f', 4), ('e', 3)])
        TestTopChars.score += 8

    def test_topchar_method_4(self):
        self.assertEqual(top_chars('ccggggeeff', 3), [('g', 4), ('f', 2), ('e', 2)])
        TestTopChars.score += 8
    
    def test_topchar_method_4(self):
        self.assertEqual(top_chars('FFggggeeff', 10), [('g', 4), ('f', 2), ('e', 2), ('F', 2)])
        TestTopChars.score += 6

if __name__ == '__main__':
    unittest.main()