import importlib
import problem16
importlib.reload(problem16)

class TestTopEarners():
    def __init__(self):
        self.score = 0

    def test_topearners_method_1(self):
        try:
            problem16.top_earners('referral1.txt', -1, 10)
        except ValueError:
            self.score += 2
        except:
            pass

    def test_topearner_method_2(self):
        try:
            problem16.top_earners('referral1.txt', 3, -2)
        except ValueError:
            self.score += 3
        except:
            pass

    def test_topearners_method_3(self):
        try:
            if problem16.top_earners('referral1.txt', 1, 1) == [('A', 200)]:
                self.score += 5
        except:
            pass

    def test_topearners_method_4(self):
        try:
            if problem16.top_earners('referral1.txt', 2, 2) == [('A', 300), ('B', 200)]:
                self.score += 5
        except:
            pass

    def test_topearners_method_5(self):
        try:
            if problem16.top_earners('referral1.txt', 3, 10) == [('A', 350), ('B', 300), ('P', 200), ('C', 0), ('Q', 0), ('X', 0), ('Y', 0)]:
                self.score += 10
        except:
            pass

    def get_score(self):
        return self.score

    def test_all(self):
        self.test_topearners_method_1()
        self.test_topearners_method_2()
        self.test_topearners_method_3()
        self.test_topearners_method_4()
        self.test_topearners_method_5()