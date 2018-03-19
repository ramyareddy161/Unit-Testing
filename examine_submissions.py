import os
import importlib
import test_custom_base5, test_factorize_number, test_get_hcf
import test_get_lcm, test_string_rotation, test_top_chars, test_top_earners

def create_csv():
    root_dir = r'.\submissions'
    students = [student for student in os.listdir(root_dir)]
    print(students)
    for student in students:
        sub_dir_addr = os.path.join(root_dir, student)
        module = 'submissions.' + student
        


if __name__ == '__main__':
    create_csv()
