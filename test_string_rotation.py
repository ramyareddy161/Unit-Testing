class TestStringRotation():
    def __init__(self, get_right_rotations):
        self.score = 0
        self.get_right_rotations = get_right_rotations

    def test_get_right_rotations_method_1(self):
        if self.get_right_rotations(None, None) == -1:
        	self.score += 1
    
    def test_get_right_rotations_method_2(self):
        if self.get_right_rotations(None, 'abcd') == -1:
        	self.score += 1

    def test_get_right_rotations_method_3(self):
        if self.get_right_rotations('abcd', 'acbd') == -1:
        	self.score += 4

    def test_get_right_rotations_method_4(self):
        if self.get_right_rotations('abcd', 'cdab') == 2:
        	self.score += 5
    
    def test_get_right_rotations_method_5(self):
        if self.get_right_rotations('aeiou', 'aeiou') == 0:
        	self.score += 4

    def get_score(self):
        return self.score

    def test_all(self):
        self.test_get_right_rotations_method_1()
        self.test_get_right_rotations_method_2()
        self.test_get_right_rotations_method_3()
        self.test_get_right_rotations_method_4()
        self.test_get_right_rotations_method_5()