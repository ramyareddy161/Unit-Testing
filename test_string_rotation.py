from problem1 import get_right_rotations

class TestStringRotation():
    def __init__(self):
        self.score = 0

    def test_get_right_rotations_method_1(self):
        if get_right_rotations(None, None) == -1:
        	self.score += 1
    
    def test_get_right_rotations_method_2(self):
        if get_right_rotations(None, 'abcd') == -1:
        	self.score += 1

    def test_get_right_rotations_method_3(self):
        if get_right_rotations('abcd', 'acbd') == -1:
        	self.score += 4

    def test_get_right_rotations_method_4(self):
        if get_right_rotations('abcd', 'cdab') == 2:
        	self.score += 5
    
    def test_get_right_rotations_method_5(self):
        if get_right_rotations('aeiou', 'aeiou') == 0:
        	self.score += 4

    def get_score(self):
        return self.score

    def test_all(self):
        self.test_get_right_rotations_method_1()
        self.test_get_right_rotations_method_2()
        self.test_get_right_rotations_method_3()
        self.test_get_right_rotations_method_4()
        self.test_get_right_rotations_method_5()