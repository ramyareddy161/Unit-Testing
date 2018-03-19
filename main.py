import os
import get_current_scores
import move_files

if __name__ == '__main__':
    current_dir = r'C:\Users\Sreekar Mouli\Documents\Programs\Python programs\Unit Testing'
    submissions_dir = r'C:\Users\Sreekar Mouli\Desktop\Submissions'
    students = os.listdir(submissions_dir)
    student_marks = {}
    for student in students:
        student_dir = os.path.join(submissions_dir, student)
        files = os.listdir(student_dir)
        for file in files:
            move_files.move_files(student_dir, current_dir, file)
        scores = get_current_scores.get_current_scores()
        student_marks[student] = scores
        for file in files:
            move_files.move_files(current_dir, student_dir, file)
        print(student, student_marks[student])
    print('Done')