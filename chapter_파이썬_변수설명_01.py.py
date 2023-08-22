#자료형과 변수
#int, flot, list, tuple, set, dict
#comment, 주석
 
#print(1)


int
print(1+2+3)

#float
# print(1.1)
# print(3.14)
# print(10*3.15)

#str
# "문자를 뜻하는 것이 str형"
# <1번>
# a = "Hello, Ptthon1"
# b = 'Hello, ' + 'Python2'

# print(type(a))
# print(len(a)) # a의 길이 출력
# print(a[1])#a의 1번째 인덱스 값, 인덱스는 0 부터 시작
# print(a[2:5]) #a의  2이상 5 미만 인덱스값 출력, 인덱스는 0부터 시작

# b[2] = a # 에러가 난다., 값이 수정불가 이므로

# <2>
# print("문자를 뜻하는 것이 str 입니다.")
# print("문자를 뜻하는 것이 str 입니다." + "같은 자료형은 이러한 형태로 가능 합니다.")
# print("문자를 뜻하는 것이 str 입니다." + 10)
# print("-" * 30) # * 만 문자와 연동 가능

# print("-" + 30) #에러가 나옴
# print("안녕")
"""
설명
"""
#list (여러가지 값을 담을수 있는것)
#  0  1  2  3  <= 인덱스 순서
# a=[1, 2, 3, 4]
# print(a)

#tuple
#print(a[0]) #index와 똑 같이 오늘 값 출력
# a = ("오늘", "내일", "모래") #괄호 모양 주의
 
# print(a[0])
# print(a[1])
# print(a[2])


#변수 ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a = 1
# b = 2
# print(a+b)

# c ="문자도 변수에 저장 가능"
# print(c)
# c ="문자도 변수에 저장 가능\n줄바꿈이 있는 경우\\n으로 표시"
# print(c)
# print("-" * 30)

# d = """여러줄의 문장을  
# 이렇게 쉽게
# 표현이 가능
# """
# 그냥" " 따옴표는 한줄로면 표현이 가능 내래오면 안됨
# print(d)

#"""

#formating

# a = "오늘"
# b = input("오늘의 날씨는 얼마야?")

# print("오늘의 날시는 30도 입니다.")
# print(f"{a}의 날시는 {b}도 입니다.")  # 간략한게 좋음
# print("{a}의 날씨는 {b}도 입니다.". format(a=a, b=b))
# print(a)

#indexing
#a = [1, 2, 3, 4, 5, 6, 7]
# print(a[0]) #0이 첫번재이므로 1이 나온다
# print(a[10]) #index 밖의 숫자가 들어오면 index error가 나온다.

#slicing
#a = [1, 2, 3, 4, 5, 6, 7, 8]
# print(a[1:3]) # 맨앞 맨뒤 빼고 중간값만 가지고 옴

# print(a[1:]) # 1부터 끝까지
# print(a[:-2]) #맨뒤에 2개 빼고

# print(a)
# a[1] = "XX"
# print(a)

# print(b)   #( ) 일때는 에러가 난다. 이게 튜블과 인덱스의 차이점
# b[1] = "XX"
# print(b)

#set 중복이 없는 집합을 사용시
# a = {1, 2, 3, 1, 2}

# a = set([1, 2, 3, 1, 2])

# print(a) # set 때문에 중복값은 없어진다.
# a.add(10) # 집합에 10을 추가 시키고 싶을때
# a.add(10) 하다라도 set이기 때문에 이미 10이 있어서 추가 안됨
# print(a) 

# a = [1, 2, 3, 1, 2]

# print(a)
# a.append(10) #그냥 10을 추가하고 싶을경우
# a.append(10) #그냥 10을 추가하고 싶을경우
# a.remove(10) #10을 삭제 하고 싶을때
# print(a)

#dictionary
# a = {'a':1, 'b':2} #key 값을 쌍으로 구성
# print(a)
# print(a['b'])

# hp_by_character = {'gengi': 200, "doomfist": 450}
# character = 'doomfist'
# print(f"{character} hp: {hp_by_character['doomfist']}")




