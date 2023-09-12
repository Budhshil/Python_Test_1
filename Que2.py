# Student Report

def calculate_final_grades(N, M, marks):
    # Calculate the average marks for each subject
    subject_averages = [sum(marks[i][j] for i in range(N)) / N for j in range(M)]

    # Find the subject with the lowest average
    lowest_avg_subject = min(enumerate(subject_averages), key=lambda x: x[1])[0]

    # Calculate final grades for each student
    final_grades = []
    for i in range(N):
        total_marks = sum(marks[i])
        adjusted_total = total_marks - marks[i][lowest_avg_subject]
        final_grades.append(adjusted_total)

    return final_grades
