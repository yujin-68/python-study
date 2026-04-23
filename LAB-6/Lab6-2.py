
def prime_num(a,b):
    prime_list = []
    for n in range(a, b+1):
        if n < 2:
            continue
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_list.append(n)
    return prime_list

prime_list = prime_num(2,10)
print('prime_list의 첫 원소 :', prime_list[0])
print('prime_list의 마지막 원소 :', prime_list[len(prime_list)-1])
print('prime_list의 마지막 원소 :', prime_list[-1])
