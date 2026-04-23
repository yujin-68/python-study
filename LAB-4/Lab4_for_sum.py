"""
n = int(input("합계를 구할 수를 입력해주세요: "))
total = 0
for i in range(1,n+1):
    total += i
print("1에서",n,"까지 합=",total)
"""

#짝수의 합
even_total = 0
for i in range(0,101,2):
    even_total += i
print("1에서 100까지 정수 중 짝수의 합: ", even_total)

#홀수의 합
odd_total = 0
for i in range(1,100,2):
    odd_total += i
print("1에서 100까지 정수 중 홀수의 합: ", odd_total)

#팩토리얼 구하기
n = int(input("수를 입력하세요: "))
fact = 1
for i in range(1,n+1):
    fact *= i
print(n,"! = ", fact)
