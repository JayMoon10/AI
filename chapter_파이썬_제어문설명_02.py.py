#if, for, while

# if 2 > 1: #(2>1) 로 해도 무방함  2<1 로 하면 값이 안나온다는 것도 설명
#     print("here")
##설명: print("here") 제어문 다음에는 반드시 들여쓰기를 하지 않으면 에러가 나므로 스페이스바 또는 탭키를 이용하여 반드시 들여쓰기를 해야한다.

####################################################

# condition = 2 > 1  띄어쓰기 조심
# print(condition)
## 답은 Ture가 나온다.

####################################################

# condition = 2 < 1
# print(condition)
## 답은 False가 나온다.
#print(type(condition)) #condition 변수의 type을 알수 있다.

####################################################

# condition = 2 > 1

# if True:    #강제적으로 true값을 지정
#      print("here")

####################################################

# condition = True #else 설명
# if condition:
#     print("here")
# else:
#     print("there")
    
# condition = False
# if condition:
#     print("here")
# else:
#     print("there")

####################################################

# n=10 #else 설명, '=='설명, elseif 설명
# if n == 10:
#     print("top")
# elif n==5:
#     print("middle")
# else:
#     print('bottom')
####################################################

# raw_input = input("숫자를 입력하세요")
# print(f"{type(raw_input)}, {raw_input}")
# guess = int(raw_input) #연산을 위해 문자형 10을 숫자형 10으로 변환

# target = 5 # 타겟 값이 5로 정해져 있을 경우
# if guess == target:
#      print("빙고 정답입니다.")
# elif guess < target:
#      print("target은 좀 더 큰 숫자 입니다.")
# elif guess > target:
#      print("target은 좀 더 작은 숫자 입니다.")

###################################################

# #random 함수를 이용해서 실행
# import random    #target값을 랜덤으로 가져오기 위해서
# raw_input = input("숫자를 입력하세요")
# guess = int(raw_input) 

# target = random.randint(1, 5) # random 함수를 이용하여 1에서 5사이에 숫자를 랜덤으로 뽑아라
# if guess == target:
#     print("빙고 정답입니다.")
# elif guess < target:
#     print("target은 좀 더 큰 숫자 입니다.")
# elif guess > target:
#     print("target은 좀 더 작은 숫자 입니다.")

######################################################

# for 문

# for i in range(10): #안녕 10번 출력하기
#     print("안녕")

######################################################
# print(range(10)) # 0부터 10까지라고 보여준다
# print(list(range(10))) # list형으로 [0부터 9까지] 보여준다. 

## 따라서 아래 2개의 for문은 같은 의미를 가진다. 하지만 1번째가 더 효율적이다.

# for i in range(10): 
#     print("안녕")

# for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print("안녕")
    
#####################################################
## 변수 i를 사용시
# for i in range(10): #0부터 9까지 보여준다.
#     print(i)

# for i in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:
#     print(i)

#####################################################
#0부터 9까지의 합
# a = 0
# for i in range(10):
#     a = a + i 
# print(a)

# a = 0
# for i in range(10):
#     a += i #a = a + i 와 같은 의미 
# print(a)

#####################################################

# while문

# #a가 10보다 작을때 까지 돌려라
# a=0
# while a < 10:
#     a += 1
#     print(a)

#####################################################
#a = 0  #터미널창에 값이 무한루프에 빠진다 이때 끌때는 ctrl + c
#while True: 
#    a += 1
#    print(a)

#####################################################
# a = 0  #위에 문제를 해결하기 위해서
# while True: 
#     a += 1
#     print(a)
#     if a > 10:
#         break    #for 나 while문을 조건을 만족하면 정지 시키는 명령어

#####################################################

# #개선본을 만들어 보면

# import random    #target값을 랜덤으로 가져오기 위해서

# target = random.randint(1, 10)

# for i in range(10):   #for문 현재 10번을 돌기로 하였기 때문에 정답을 맞추어도 계속 물어본다. 따라서 bnreak문을 쓴다
#     guess = int(input("숫자를 입력하세요"))
#     if guess == target:
#         print("빙고 정답입니다.")
#     elif guess < target:
#         print("target은 좀 더 큰 숫자 입니다.")
#     elif guess > target:
#         print("target은 좀 더 작은 숫자 입니다.")

#####################################################
#최종 완성본
#import random    #target값을 랜덤으로 가져오기 위해서

#target = random.randint(1, 10)

#for i in range(10):   #for문에 break문 입력
#        guess = int(input("숫자를 입력하세요"))
#    if guess == target:
#        print("빙고 정답입니다.")
#        break
#    elif guess < target:
#        print("target은 좀 더 큰 숫자 입니다.")
#    elif guess > target:
#        print("target은 좀 더 작은 숫자 입니다.")    

#####################################################
# while을 이용하여 10번을 넘어가더 라도 계속 답을 맞출때까지 실행하는 방법
#import random    #target값을 랜덤으로 가져오기 위해서

#target = random.randint(1, 10)

#while True:   #for문에 break문 입력
#    guess = int(input("숫자를 입력하세요"))
#    if guess == target:
#       print("빙고 정답입니다.")
#       break
#    elif guess < target:
#       print("target은 좀 더 큰 숫자 입니다.")
#    elif guess > target:
#       print("target은 좀 더 작은 숫자 입니다.")    


