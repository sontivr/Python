if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)
    print("type of line: {}".format(type(line)))
    marks = [v for k, v in student_marks.items() if(k == query_name)]
    print(*marks)
    print("type of marks: {}".format(type(marks)))
    print("{:.2f}".format(sum(*marks)/len(*marks)))
