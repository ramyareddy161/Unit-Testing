import importlib
import problem19
importlib.reload(problem19)

class TestGetHcf():
    def __init__(self):
        self.score = 0

    def test_gethcf_method_1(self):
        try:
            if problem19.get_hcf([], [(2, 5)]) == []:
                self.score += 2
        except:
            pass
    
    def test_gethcf_method_2(self):
        try:
            if problem19.get_hcf([], []) == []:
                self.score += 3
        except:
            pass

    def test_gethcf_method_3(self):
        try:
            if problem19.get_hcf([(2, 3), (3, 3), (11, 1)], [(5, 2)]) == []:
                self.score += 5
        except:
            pass

    def test_gethcf_method_4(self):
        try:
            if problem19.get_hcf([(2, 3), (5, 3), (17, 2)], [(2, 1), (3, 5), (5, 2), (19, 1)]) == [(2, 1), (5, 2)]:
                self.score += 5
        except:
            pass

    def test_gethcf_method_5(self):
        try:
            if problem19.get_hcf([(2, 1), (11, 3), (19, 2), (7919, 4)], [(2, 2), (7, 1), (19, 1), (2687, 4)]) == [(2, 1), (19, 1)]:
                self.score += 10
        except:
            pass

    def get_score(self):
        return self.score

    def test_all(self):
        self.test_gethcf_method_1()
        self.test_gethcf_method_2()
        self.test_gethcf_method_3()
        self.test_gethcf_method_4()
        self.test_gethcf_method_5()