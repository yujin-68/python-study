year = int(input("년도를 입력하세요: "))

"""
if year % 400 == 0:
    print(str(year) + "은 윤년입니다.")
elif year % 100 == 0 & year % 4 == 0:
    print(str(year) + "은 평년입니다.")
elif year % 4 == 0:
    print(str(year) + "은 윤년입니다.")
"""

is_leap_year = ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)
print (year, '년은 윤년입니까?', is_leap_year)

