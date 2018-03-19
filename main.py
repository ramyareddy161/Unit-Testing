import os
import get_current_scores
import file_io

if __name__ == '__main__':
    current_dir = r'C:\Users\Sreekar Mouli\Documents\Programs\Python programs\Unit Testing'
    submissions_dir = r'C:\Users\Sreekar Mouli\Desktop\Submissions'
    students = os.listdir(submissions_dir)
    student_marks = {}
    with open('marks.csv', 'wt') as f:
        f.write('Student,Custom Base 5,Factorize number,HCF,LCM,String rotation,Top chars,Top earners,Total\n')
        for student in students:
            student_dir = os.path.join(submissions_dir, student)
            files = os.listdir(student_dir)
            for file in files:
                file_io.copy_file(student_dir, current_dir, file)
            scores = get_current_scores.get_current_scores()
            student_marks[student] = scores
            for file in files:
                file_io.delete_file(current_dir, file)
            total = sum(scores)
            scores = ','.join(list(map(str, scores)))
            f.write(','.join([student, scores]) + ',' + str(total) + '\n')
    print('Done')