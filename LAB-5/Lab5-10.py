#가변인자의 활용
def sum_nums(*numbers):
    total = 0
    average = 0
    print(f"{len(numbers)}개의 인자", numbers)
    for i in numbers:
        total += i
    average = total / len(numbers)
    print(f'합계: {total}, 평균: {average}')

def min_nums(*numbers):
    min_num = numbers[0]
    for n in numbers:
        print(f'n={n}, min_num={min_num}')
        if n < min_num:
            min_num = n
    print(f"최솟값은 {min_num}")
