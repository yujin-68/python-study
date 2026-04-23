
answer = None

"""
while answer != "그만":
    answer = input("가위,바위,보 중 하나를 입력하세요./끝내고싶을 시 그만: ")
    print(answer)
"""

while answer not in ['가위','바위','보']:
    answer = input("가위, 바위, 보 중 하나를 입력하세요 >")
    print(answer)
