class TestGetLcm():
    def __init__(self, get_lcm):
        self.score = 0
        self.get_lcm = get_lcm

    def test_getlcm_method_1(self):
        if self.get_lcm([], [(2, 5)]) == [(2, 5)]:
            self.score += 2
    
    def test_getlcm_method_2(self):
        if self.get_lcm([], []) == []:
            self.score += 3

    def test_getlcm_method_3(self):
        if self.get_lcm([(2, 1), (5, 2), (7, 2)], [(2, 2), (3, 1), (17, 2)]) == [(2, 2), (3, 1), (5, 2), (7, 2), (17, 2)]:
            self.score += 5

    def test_getlcm_method_4(self):
        if self.get_lcm([(2, 1), (19, 1), (7919, 4)], [(2, 2), (17, 1), (2687, 4)]) == [(2, 2), (17, 1), (19, 1), (2687, 4), (7919, 4)]:
            self.score += 15

    def get_score(self):
        return self.score

    def test_all(self):
        self.test_getlcm_method_1()
        self.test_getlcm_method_2()
        self.test_getlcm_method_3()
        self.test_getlcm_method_4()