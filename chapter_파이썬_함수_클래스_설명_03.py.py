#함수, 클래스

# def function_name(a, b): #def:함수를 정의 한다는 용어 만들어 보면
#     return a + b
#def sum(a, b): #f(a, b) = a + b 와 같은 의미
#    return a + b

#print(sum(2, 3)) # print(sum(a=2, b=3)) 적어도 된다.

########################################################################
# a와 b의 값들을 살펴보기 위해
#def sum(a, b): 
#    print(f"a: {a}")
#    print(f"b: {b}")
#    return a + b
    
#print(sum(b=3, a=2)) # a, b 파라미터를 지정되면 위치는 바뀌어도 상관없다.

########################################################################
# a와 b의 값들을 살펴보기 위해
#def sum(a, b): 
#    print(f"a: {a}")
#    print(f"b: {b}")
#    return a + b
    
#print(sum()) # a, b에 대한 값이 없기 때문에 에러가 난다 함수는 받으시 정해진 값을 넣어야 한다.

########################################################################
# default value: a와 b의 값을 사전에 지정
# def sum(a=1, b=2): 
#     print(f"a: {a}")
#     print(f"b: {b}")
#     return a + b
    
# print(sum()) #값이 없을때
# print(sum(3)) #값이 3일때 a가 3이므로 5
# print(sum(3, 4)) #값이 3일때 a가 3, b가 4이므로 7
# print(sum(b=3)) # b가 3이므로 4가 된다.

########################################################################
#주의 사항
#def sum(a, b=2): # 앞 파라메터 값은 삭제가 가능하나 
# def sum(a, b=2): 
#     print(f"a: {a}")
#     print(f"b: {b}")
#     return a + b
    
# print(sum(a=3))

#def sum(a=1, b): # 뒤 파라메터 값은 삭제가 불가능하다. 에러가 난다.
# def sum(a=1, b): 
#     print(f"a: {a}")
#     print(f"b: {b}")
#     return a + b
    
# print(sum(b=3))

########################################################################

#시험점수 평균 구하는 함수만들기
# score = [70, 85, 90, 100]

# total = 0
# for n in score:
#     total += n

# avg = total / len(score)
# print(f"avg: {avg}")

########################################################################
#파이썬 자체 sum함수와 len함수를 이용하여 좀 더 간결하게 만들기
# score = [70, 85, 90, 100]

# total = sum(score) / len(score)
# print(f"avg: {total}")

########################################################################
# 3명의 평균을 내고자 할때
# person_a_score = [70, 85, 90, 100]
# person_b_score = [40, 60, 90, 80]
# person_c_score = [50, 60, 0, 47]

# total = sum(person_a_score) / len(person_a_score)
# print(f"avg: {total}")

# total = sum(person_b_score) / len(person_b_score)
# print(f"avg: {total}")

# total = sum(person_c_score) / len(person_c_score)
# print(f"avg: {total}")

########################################################################
# 3명의 평균을 함수로 만들어 단순화
# person_a_score = [70, 85, 90, 100]
# person_b_score = [40, 60, 90, 80]
# person_c_score = [50, 60, 0, 47]

# def cal_avg(socre):
#     total=sum(socre) / len(socre)
#     print(f"avg: {total}")
#     return total

# cal_avg(person_a_score)
# cal_avg(person_b_score)
# cal_avg(person_c_score)

########################################################################
# 좀 더 활용
# person_a_score = [70, 85, 90, 100]
# person_b_score = [40, 60, 90, 80]
# person_c_score = [50, 60, 0, 47]

# def cal_avg(socre):
#     total=sum(socre) / len(socre)
#     print(f"avg: {total}")
#     return total

# person_numbers_list = [person_a_score, person_b_score, person_c_score]

# for score in person_numbers_list:
#     cal_avg(score)


########################################################################
# calss(클래스란?)

# class ClassName:
#     def __init__(self, parameters) -> None:
#         pass  
        
#     def some_function(self): 
#         pass 

########################################################################
# bank account 를 이용한 calss의 이해
#accounts_number 와 balance라는 속성을 가지고 deposit과 withdraw 이용하여 입금과 출급을 
# 할 수 있는 객체
class BankAccount:
    def __init__(self, accounts_number, balance=0):
        self.accounts_number = accounts_number
        self.balance = balance
        
    def deposit(self, amount):
        pass #지금은 아니고 추후 입력 할 것이다는 의미

    def withdraw(self, amount):
        pass

account = BankAccount("123-456-789", 10000) #이때 account가 인스턴스 account번호"123-456-789"
# 예금(balance: 10000) 를 가지고 있는 객체, 요기 값들이 위헤  
# def __init__(self, accounts_number, balance=0): 에서 accounts_number, balance에 채워짐

print(f"accounts_number: {account.accounts_number}")

# account.deposit(5000)
# account.withdraw(12000)
# account.withdraw(5000)

############################################################################

# class BankAccount:
#     def __init__(self, accounts_number, balance=0):
#         self.accounts_number = accounts_number
#         self.balance = balance
        
#     def deposit(self, amount):
#         print(f"{amount}원을 입금했습니다.")

#     def withdraw(self, amount):
#         print(f"{amount}원을 출금했습니다.")

# account = BankAccount("123-456-789", 10000) 

# print(f"accounts_number: {account.accounts_number}")

# account.deposit(5000)
# account.withdraw(12000)
# account.withdraw(5000)

################################################################################

# class BankAccount:
#     def __init__(self, accounts_number, balance=0):
#         self.accounts_number = accounts_number
#         self.balance = balance
        
#     def deposit(self, amount):
#         print(f"{amount}원을 입금했습니다.")

#     def withdraw(self, amount):
#         print(f"{amount}원을 출금했습니다.")
# person_a_account = BankAccount("123-456-789", 10000) 
# print(f"accounts_number: {person_a_account.accounts_number}")

# person_a_account.deposit(5000)
# person_a_account.withdraw(12000)
# person_a_account.withdraw(5000)

# person_b_account = BankAccount("445-999-000", 5000) 
# print(f"accounts_number: {person_b_account.accounts_number}")
# person_b_account.deposit(6000)
# person_b_account.withdraw(10000)
# person_b_account.withdraw(7000)

################################################################################
#마지막 BankAccount 버전

# class BankAccount:
#     def __init__(self, accounts_number, balance=0):
#         self.accounts_number = accounts_number
#         self.balance = balance
        
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount}원을 입금했습니다. 현재 잔액은 {self.balance}원 입니다.")

#     def withdraw(self, amount):
#         if self.balance >= amount:
#             self.balance -= amount
#             print(f"{amount}원을 출금했습니다. 현재 잔액은 {self.balance}원 입니다.")
#         else:
#             print(f"잔액이 부족합니다. 현재 잔액은 {self.balance}원 입니다.")

# person_a_account = BankAccount("123-456-789", 10000) 

# person_a_account.deposit(5000)
# person_a_account.withdraw(12000)
# person_a_account.withdraw(5000)

# print(f"accounts_number: {person_a_account.accounts_number}")
# print(f"balance: {person_a_account.balance}")

# print("*" * 30)

# person_b_account = BankAccount("445-999-000", 5000) 

# person_b_account.deposit(6000)
# person_b_account.withdraw(10000)
# person_b_account.withdraw(7000)

# print(f"accounts_number: {person_b_account.accounts_number}")
# print(f"accounts_number: {person_b_account.balance}")