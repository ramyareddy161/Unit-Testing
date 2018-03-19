import test_custom_base5, test_factorize_number, test_get_hcf
import test_get_lcm, test_string_rotation, test_top_chars, test_top_earners
import os, collections

def get_scores_of_student(current_dir, submissions_dir, student):
    files = {
        'problem1.py': test_string_rotation.TestStringRotation
    }
    scores = []
    for file in files:
        source = os.path.join(submissions_dir, os.path.join(student, file))
        destination = os.path.join(current_dir, os.path.join(student, file))
        print(source, destination)
        os.rename(source, destination)
        scores.append(files[file]())
        os.rename(destination, source)


def create_csv():
    current_dir = r'C:\Users\Sreekar Mouli\Documents\Programs\Python programs\Unit Testing'
    submissions_dir = r'C:\Users\Sreekar Mouli\Desktop\Submissions'
    students = os.listdir(submissions_dir)
    student_marks = collections.defaultdict(list)
    for student in students:
        get_scores_of_student(current_dir, submissions_dir, student)

if __name__ == '__main__':
    create_csv()