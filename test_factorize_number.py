from problem17 import factorize_number

class TestFactorizeNumber():
    def __init__(self):
        self.score = 0

    def test_method_1(self):
        try:
            if factorize_number(1) == []:
                self.score += 2
        except:
            pass

    def test_method_2(self):
        try:
            if factorize_number(6010) == [(2, 1), (5, 1), (601, 1)]:
                self.score += 5
        except:
            pass

    def test_method_3(self):
        try:
            if factorize_number(7865228921869442) == [(2, 1), (7919, 4)]:
                self.score += 10
        except:
            pass

    def test_method_4(self):
        try:
            factorize_number(-10)
        except ValueError:
        	self.score += 3
        except:
            pass

    def test_method_5(self):
        try:
            factorize_number(3.2)
        except TypeError:
        	self.score += 5
        except:
            pass

    def get_score(self):
        return self.score

    def test_all(self):
        self.test_method_1()
        self.test_method_2()
        self.test_method_3()
        self.test_method_4()
        self.test_method_5()