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

prime_list = prime_num(1,10)

nations = ['Korea','China','Russia','Malaysia']

if 'Japan' in nations:
    print('Japan은 국가 목록에 있습니다.')
else:
    print('Japan은 국가 목록에 없습니다.')
