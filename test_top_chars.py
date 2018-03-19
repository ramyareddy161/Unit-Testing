from problem6 import top_chars

class TestTopChars():
    def __init__(self):
        self.score = 0

    def test_topchar_method_1(self):
        try:
            top_chars(None, 10)
        except TypeError:
        	self.score += 1

    def test_topchar_method_2(self):
        try:
            top_chars('hello', 'w')
        except TypeError:
        	self.score += 1

    def test_topchar_method_3(self):
        try:
            top_chars('hello', -1)
        except ValueError:
        	self.score += 1

    def test_topchar_method_4(self):
        if top_chars('acceeeffff', 2) == [('f', 4), ('e', 3)]:
        	self.score += 8

    def test_topchar_method_5(self):
        if top_chars('ccggggeeff', 3) == [('g', 4), ('f', 2), ('e', 2)]:
        	self.score += 8
    
    def test_topchar_method_6(self):
        if top_chars('FFggggeeff', 10) == [('g', 4), ('f', 2), ('e', 2), ('F', 2)]:
        	self.score += 6

    def get_score(self):
        return self.score

    def test_all(self):
        self.test_topchar_method_1()
        self.test_topchar_method_2()
        self.test_topchar_method_3()
        self.test_topchar_method_4()
        self.test_topchar_method_5()
        self.test_topchar_method_6()