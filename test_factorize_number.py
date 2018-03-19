class TestFactorizeNumber():
    def __init__(self, factorize_number):
        self.score = 0
        self.factorize_number = factorize_number

    def test_method_1(self):
        if self.factorize_number(1) == []:
        	self.score += 2

    def test_method_2(self):
        if self.factorize_number(6010) == [(2, 1), (5, 1), (601, 1)]:
        	self.score += 5

    def test_method_3(self):
        if self.factorize_number(7865228921869442) == [(2, 1), (7919, 4)]:
        	self.score += 10

    def test_method_4(self):
        try:
            self.factorize_number(-10)
        except ValueError:
        	self.score += 3

    def test_method_5(self):
        try:
            self.factorize_number(3.2)
        except TypeError:
        	self.score += 5