def multiples(n, m):
    result = []
    for i in range(1,m+1):
        result.append(n * i)
    return result

r1,r2,r3,r4 = multiples(3,4)
print(r1,r2,r3,r4)

r1,r2,r3,r4,r5 = multiples(2,5)
print(r1,r2,r3,r4,r5)
