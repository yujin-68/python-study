def circle_area_circum(radius):
    area = 3.14 * radius**2
    circum = 2 * 3.14 * radius
    return area, circum

area, circum = circle_area_circum(10)
print(f'반지름 10인 원의 면적은 {area}, 원의 둘레는 {circum:2f}')
    
