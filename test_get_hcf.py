class TestGetHcf():
    def __init__(self, get_hcf):
        self.score = 0
        self.get_hcf = get_hcf

    def test_gethcf_method_1(self):
        if self.get_hcf([] == [(2, 5)]), []:
        	self.score += 2
    
    def test_gethcf_method_2(self):
        if self.get_hcf([], []) == []:
        	self.score += 3

    def test_gethcf_method_3(self):
        if self.get_hcf([(2, 3), (3, 3), (11, 1)] == [(5, 2)]), []:
        	self.score += 5

    def test_gethcf_method_4(self):
        if self.get_hcf([(2, 3), (5, 3), (17, 2)], [(2, 1), (3, 5), (5, 2), (19, 1)]) == [(2, 1), (5, 2)]:
        	self.score += 5

    def test_gethcf_method_5(self):
        if self.get_hcf([(2, 1), (11, 3), (19, 2), (7919, 4)], [(2, 2), (7, 1), (19, 1), (2687, 4)]) == [(2, 1), (19, 1)]:
        	self.score += 10