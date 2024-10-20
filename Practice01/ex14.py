'''[ex14.py]  
다음 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 
아래와 같이 출력하는 프로그램을 작성하세요.
[ 1, 3, 5, 8, 9, 11, 15, 19, 18, 20, 30, 33, 31 ]
'''

numbers = [1, 3, 5, 8, 9, 11, 15, 19, 18, 20, 30, 33, 31]

count = 0
total = 0

for num in numbers:
    if num % 3 == 0:
        count = count + 1
        total = total + num

print(f"주어진 배열에서 3의 배수의 개수 => {count}")
print(f"주어진 배열에서 3의 배수의 합 => {total}")