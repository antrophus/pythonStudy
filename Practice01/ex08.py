'''[ex08.py] 
사용자로부터 구의 반지름을 입력받아 구의 부피를 계산하는 프로그램을 작성하세요.
'''
# V: 구의 부피, pi: 3.14, r: 반지름 
pi = 3.14
r = float(input("반지름을 입력하세요: "))
v = 4/3*pi*r**3
print(f"구의부피는: {v} 입니다.")