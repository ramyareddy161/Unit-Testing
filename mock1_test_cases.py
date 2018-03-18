#
#   Each test case has a 'score' varaible which represent the points
#   that will be alloted if the test cases passes
#

# !! FACTORIZE NUMBER !!
def test_method_1():
    assert factorize_number(1) == []
    score = 2

def test_method_2():
    assert factorize_number(6010) == [(2, 1), (5, 1), (601, 1)]
    score = 5

def test_method_3():
    assert factorize_number(7865228921869442) == [(2, 1), (7919, 4)]
    score = 10

def test_method_4():
    try:
        result = factorize_number(-10)
        assert False
    except ValueError:
        assert True
    score = 3

def test_method_5():
    try:
        result = factorize_number(3.2)
        assert False
    except TypeError:
        assert True
    score = 5

# !! GET LCM !!
def test_getlcm_method_1():
    assert get_lcm([], [(2, 5)]) == [(2, 5)]
    score = 2

def test_getlcm_method_2():
    assert get_lcm([], []) == []
    score = 3

def test_getlcm_method_3():
    assert get_lcm([(2, 1), (5, 2), (7, 2)], [(2, 2), (3, 1), (17, 2)]) == [(2, 2), (3, 1), (5, 2), (7, 2), (17, 2)]
    score = 5

def test_getlcm_method_4():
    assert get_lcm([(2, 1), (19, 1), (7919, 4)], [(2, 2), (17, 1), (2687, 4)]) == [(2, 2), (17, 1), (19, 1), (2687, 4), (7919, 4)]
    score = 15

# !! GET HCF !!
def test_gethcf_method_1():
    assert get_hcf([], [(2, 5)]) == []
    score = 2

def test_gethcf_method_2():
    assert get_hcf([], []) == []
    score = 3

def test_gethcf_method_3():
    assert get_hcf([(2, 3), (3, 3), (11, 1)], [(5, 2)]) == []
    score = 5

def test_gethcf_method_4():
    assert get_hcf([(2, 3), (5, 3), (17, 2)], [(2, 1), (3, 5), (5, 2), (19, 1)]) == [(2, 1), (5, 2)]
    score = 5

def test_gethcf_method_5():
    assert get_hcf([(2, 1), (11, 3), (19, 2), (7919, 4)], [(2, 2), (7, 1), (19, 1), (2687, 4)]) == [(2, 1), (19, 1)]
    score = 10

# !! TOP EARNERS !!
def test_topearners_method_1():
    assert (top_earners())
    score = 2

def test_topearners_method_2():
    assert (top_earners())
    score = 3

def test_topearners_method_3():
    assert (top_earners())
    score = 5

def test_topearners_method_4():
    assert (top_earners())
    score = 5

# !! CUSTOM BASE 5 !!
def test_tocustombase5_method_1():
    assert to_custom_base5(0) == 'a'
    score = 2

def test_tocustombase5_method_2():
    assert to_custom_base5(1001) ==  'bdaab'
    score = 5

def test_tocustombase5_method_3():
    assert to_custom_base5(-1001) ==  '-bdaab'
    score = 5

def test_tocustombase5_method_4():
    with self.assertRaises(TypeError):
        result = to_custom_base5(3.2)
    score = 3

def test_fromcustombase5_method_1():
    assert from_custom_base5(' bdeab ') ==  1101
    score = 3

def test_fromcustombase5_method_2():
    assert from_custom_base5(' -bdeab ') ==  -1101
    score = 3

def test_fromcustombase5_method_3():
    assert from_custom_base5(' +bdeab ') ==  1101
    score = 3

def test_fromcustombase5_method_4():
    assert from_custom_base5('BDeab') ==  1101
    score = 3

def test_fromcustombase5_method_5():
    try:
        from_custom_base5('BDhello')
        assert False
    except ValueError:
        assert True
    score = 3

def test_fromcustombase5_method_6():
    try:
        from_custom_base5('bde-ab')
        assert False
    except ValueError:
        assert True
    score = 3

def test_fromcustombase5_method_7():
    try:
        from_custom_base5(10)
        assert False
    except ValueError:
        assert True
    score = 2

# !! TOP CHARS !!
def test_topchar_method_1():
    try:
        top_chars(None, 10)
        assert False
    except TypeError:
        assert True
    score = 1

def test_topchar_method_2():
    try:
        top_chars('hello', 'w')
        assert False
    except TypeError:
        assert True
    score = 1

def test_topchar_method_3():
    try:
        top_chars('hello', -1)
        assert False
    except ValueError:
        assert True
    score = 1

def test_topchar_method_4():
    assert top_chars('acceeeffff', 2) == [('f', 4), ('e', 3)]
    score = 8

def test_topchar_method_4():
    assert  top_chars('ccggggeeff', 3) == [('g', 4), ('f', 2), ('e' == 2)]
    score = 8

def test_topchar_method_4():
    assert top_chars('FFggggeeff', 10) == [('g', 4), ('f', 2), ('e', 2), ('F', 2)]
    score = 6

# !! STRING ROTATION !!
def test_get_right_rotations_method_1():
    assert get_right_rotations(None, None) == -1
    score = 1

def test_get_right_rotations_method_2():
    assert get_right_rotations(None, 'abcd') == -1
    score = 1

def test_get_right_rotations_method_3():
    assert get_right_rotations('abcd', 'acbd') == -1
    score = 4

def test_get_right_rotations_method_4():
    assert get_right_rotations('abcd', 'cdab') == 2
    score = 5

def test_get_right_rotations_method_5():
    assert get_right_rotations('aeiou', 'aeiou') == 0
    score = 4