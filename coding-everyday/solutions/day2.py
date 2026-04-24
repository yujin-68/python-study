#day 2

def find_row_number(student_number):
    row_num = (student_number - 1) // 4 + 1
    colum_num = (student_number - 1) % 4 + 1
    print('{0}번째 줄의 {1}번째 자리에 앉습니다.'.format(row_num,colum_num))
