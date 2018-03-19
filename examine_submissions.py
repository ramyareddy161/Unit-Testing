import test_custom_base5, test_factorize_number, test_get_hcf
import test_get_lcm, test_string_rotation, test_top_chars, test_top_earners
import os, collections

def create_csv():
    submissions_dir = r'C:\Users\Sreekar Mouli\Desktop\Submissions'
    students = os.listdir(submissions_dir)
    student_marks = collections.defaultdict(list)
    for student in students:
        source = os.path.join(submissions_dir, student)
        print(source)

if __name__ == '__main__':
    create_csv()