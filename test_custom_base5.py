class TestCustomBase5():
    def __init__(self, to_custom_base5, from_custom_base5):
        self.score = 0
        self.to_custom_base5 = to_custom_base5
        self.from_custom_base5 = from_custom_base5

    def test_tocustombase5_method_1(self):
        if self.to_custom_base5(0) == 'a':
            self.score += 2
    
    def test_tocustombase5_method_2(self):
        if self.to_custom_base5(1001) == 'bdaab':
            self.score += 5

    def test_tocustombase5_method_3(self):
        if self.to_custom_base5(-1001) == '-bdaab':
            self.score += 5

    def test_tocustombase5_method_4(self):
        try:
            self.to_custom_base5(3.2)
        except TypeError:
            self.score += 3

    def test_fromcustombase5_method_1(self):
        if self.from_custom_base5(' bdeab ') == 1101:
            self.score += 3

    def test_fromcustombase5_method_2(self):
        if self.from_custom_base5(' -bdeab ') == -1101:
            self.score += 3

    def test_fromcustombase5_method_3(self):
        if self.from_custom_base5(' +bdeab ') == 1101:
            self.score += 3

    def test_fromcustombase5_method_4(self):
        if self.from_custom_base5('BDeab') == 1101:
            self.score += 3

    def test_fromcustombase5_method_5(self):
        try:
            self.from_custom_base5('BDhello')
        except ValueError:
            self.score += 3

    def test_fromcustombase5_method_6(self):
        try:
            self.from_custom_base5('bde-ab')
        except ValueError:
            self.score += 3

    def test_fromcustombase5_method_7(self):
        try:
            self.from_custom_base5(10)
        except TypeError:
            self.score += 2