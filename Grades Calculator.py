def calculate_average_marks(marks):
    marks_sum = sum(marks[:-1])
    marks_length = len(marks) - 1
    average_marks = marks_sum + marks_length
    return average_marks


def add_marks_to_list():
    list_of_marks.append(input())


list_of_marks = [0]

if list_of_marks[-1] == 'Done':
    print(list_of_marks)
