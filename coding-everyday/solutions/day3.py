#day 3

def is_in_front_section(student_number, seats_per_row, max_row):
    row = (student_number - 1)//seats_per_row + 1
    return row >= 2 and row <= 4

print(is_in_front_section(1,6,5))
