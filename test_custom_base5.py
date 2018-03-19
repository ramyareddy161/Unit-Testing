from problem2 import to_custom_base5, from_custom_base5

class TestCustomBase5():
    def __init__(self):
        self.score = 0

    def test_tocustombase5_method_1(self):
        if to_custom_base5(0) == 'a':
            self.score += 2
    
    def test_tocustombase5_method_2(self):
        if to_custom_base5(1001) == 'bdaab':
            self.score += 5

    def test_tocustombase5_method_3(self):
        if to_custom_base5(-1001) == '-bdaab':
            self.score += 5

    def test_tocustombase5_method_4(self):
        try:
            to_custom_base5(3.2)
        except TypeError:
            self.score += 3

    def test_fromcustombase5_method_1(self):
        if from_custom_base5(' bdeab ') == 1101:
            self.score += 3

    def test_fromcustombase5_method_2(self):
        if from_custom_base5(' -bdeab ') == -1101:
            self.score += 3

    def test_fromcustombase5_method_3(self):
        if from_custom_base5(' +bdeab ') == 1101:
            self.score += 3

    def test_fromcustombase5_method_4(self):
        if from_custom_base5('BDeab') == 1101:
            self.score += 3

    def test_fromcustombase5_method_5(self):
        try:
            from_custom_base5('BDhello')
        except ValueError:
            self.score += 3

    def test_fromcustombase5_method_6(self):
        try:
            from_custom_base5('bde-ab')
        except ValueError:
            self.score += 3

    def test_fromcustombase5_method_7(self):
        try:
            from_custom_base5(10)
        except TypeError:
            self.score += 2

    def get_score(self):
        return self.score
    
    def test_all(self):
        self.test_fromcustombase5_method_1()
        self.test_fromcustombase5_method_2()
        self.test_fromcustombase5_method_3()
        self.test_fromcustombase5_method_4()
        self.test_fromcustombase5_method_5()
        self.test_fromcustombase5_method_6()
        self.test_fromcustombase5_method_7()
        self.test_tocustombase5_method_1()
        self.test_tocustombase5_method_2()
        self.test_tocustombase5_method_3()
        self.test_tocustombase5_method_4()
