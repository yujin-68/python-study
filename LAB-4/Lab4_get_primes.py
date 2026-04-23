n = int(input("숫자를 입력하세요: "))

is_prime = True

for i in range(2,n+1):
    if n % i == 0 and n != i:
        print(n,"은",i,"로 나누어 떨어집니다.")
        is_prime = False
        break
    else:
        is_prime = True

print(n,"은 소수 인가요? :", is_prime)
