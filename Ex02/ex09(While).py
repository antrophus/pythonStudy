print("========== while문 ==========")

#1부터 10까지의 합을 구하시오.

i = 0
total = 0
print("1 부터 10까지의 합을 구하시오")
while i<= 10:
    total += i
    i += 1
print("\n합:", total)



print("================================================================")
#6의 배수이자 14의 배수인 가장 적은 정수 찾기
print("\n6의 배수이자 14의 배수인 가장 적은 정수 찾기")
i = 1
while True:
    if i%6 == 0 and i%14 == 0:
        print("\n",i)
        break
    i = i + 1