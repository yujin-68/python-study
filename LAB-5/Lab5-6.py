#근의 공식
def root(a,b,c):
    r = (b**2 - 4*a*c)**0.5
    x1 = (-b + r)/2*a
    x2 = (-b - r)/2*a
    print(f'x = {x1} or {x2}')

#삼각형 면적
def print_area(a,b):
    area = (a*b)/2
    print(f'밑변 {a}, 높이 {b}인 삼각형의 면적은: {area}')
