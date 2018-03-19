def get_current_scores():
    scores = []
    try:
        import test_custom_base5
        test_ob = test_custom_base5.TestCustomBase5()
        test_ob.test_all()
        scores.append(test_ob.get_score())
    except ImportError:
        scores.append(0)
    try:
        import test_factorize_number
        test_ob = test_factorize_number.TestFactorizeNumber()
        test_ob.test_all()
        scores.append(test_ob.get_score())
    except ImportError:
        scores.append(0)
    try:
        import test_get_hcf
        test_ob = test_get_hcf.TestGetHcf()
        test_ob.test_all()
        scores.append(test_ob.get_score())
    except ImportError:
        scores.append(0)
    try:
        import test_get_lcm
        test_ob = test_get_lcm.TestGetLcm()
        test_ob.test_all()
        scores.append(test_ob.get_score())
    except ImportError:
        scores.append(0)
    try:
        import test_string_rotation
        test_ob = test_string_rotation.TestStringRotation()
        test_ob.test_all()
        scores.append(test_ob.get_score())
    except ImportError:
        scores.append(0)
    try:
        import test_top_chars
        test_ob = test_top_chars.TestTopChars()
        test_ob.test_all()
        scores.append(test_ob.get_score())
    except ImportError:
        scores.append(0)
    try:
        import test_top_earners
        test_ob = test_top_earners.TestTopEarners()
        test_ob.test_all()
        scores.append(test_ob.get_score())
    except ImportError:
        scores.append(0)
    return scores

# def get_scores_of_student(current_dir, submissions_dir, student, questions):
#     scores = []
#     for question in questions:
#         source = os.path.join(submissions_dir, os.path.join(student, file))
#         destination = os.path.join(current_dir, os.path.join(student, file))
#         print(source, destination)
#         os.rename(source, destination)
#         test_ob = question()
#         test_ob.test_all()
#         scores.append(test_ob.get_score())
#         os.rename(destination, source)
#     return scores


# def create_csv():
#     current_dir = r'C:\Users\Sreekar Mouli\Documents\Programs\Python programs\Unit Testing'
#     submissions_dir = r'C:\Users\Sreekar Mouli\Desktop\Submissions'
#     students = os.listdir(submissions_dir)
#     student_marks = {}
#     questions = [test_custom_base5.TestCustomBase5, test_factorize_number.TestFactorizeNumber,
#     test_get_hcf.TestGetHcf, test_get_lcm.TestGetLcm, test_string_rotation.TestStringRotation,
#     test_top_chars.TestTopChars, test_top_earners.TestTopEarners]
#     for student in students:
#         student_marks[student] = get_scores_of_student(current_dir, submissions_dir, student, questions)
#         print(student, student_marks[student])

# if __name__ == '__main__':
#     create_csv()