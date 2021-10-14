# Chapter07-1
# 파이썬 예외처리의 이해
# 예외 종류
# SyntaxError, TypeError, NameError, IndexError, ValueError, keyError....
# 문법적으로는 예외가 없지만, 코드 실행 프로세스(단계)에서 발생하는 예외도 중요
# 1. 예외는 반드시 처리
# 2. 로그는 반드시 남긴다.
# 3. 예외는 던져진다.
# 4. 예외 무시

# SyntaxError : 문법 오류
# print('error)
# print('error'))
# if True

# NameError : 참조 없음
# a = 10
# b = 15
# print(c)

# ZeroDivisionError

# print(100/0)

# IndexError

# x = [50, 70, 90]
# # print(x[1])
# # print(x[4])
# print(x.pop())
# print(x.pop())
# print(x.pop())
# print(x.pop())

# KeyError

# dic = {'name': 'Lee', 'Age': 41, 'City': 'Busan'}
# #print(dic['hobby'])
# print(dic.get('hobby')) 해당 키가 없을 시 none을 가져옴

# 예외 없는 것을 가정하고 프로그램 작성 -> 런타임 예외 발생 시 예외 처리 권장(EAFP)

# AttributeError : 모듈, 클래스에 있는 잘못된 속성 사용 예외
# import time
# print(time.time2())

# ValueError

# x = [10, 50, 90]
# x.remove(50)
# print(x)
# x.remove(200)

# FileNotFoundError

# f = open('test.txt')

# # TypeError : 자료형에 맞지 않는 연산을 수행 할 경우
# x = [1,2]
# y = (1,2)
# z = 'test'

# # print(x + y)
# # print(x + z)
# # print(y + z)

# print(x + list(y))


# 예외 처리 기본
# try : 에러가 발생할 가능성이 있는 코드 실행
# except 에러명1 : 여러개 가능
# except 에러명2 : 
# else : try 블록의 에러가 없을 경우 실행됨
# finally : 항상 실행

name = ['Kim', 'Lee', 'Park']

# 예제1
# try:
#     z = 'Kim'
#     x = name.index(z) # 0
#     print('{} Found it! {} in name' .format(z, x + 1))
# except ValueError:
#     print('Not found it! - Occurred ValueError')
# else:
#     print('Ok! else.')

# print()

# print('pass')

# 예제2 Exception 사용시 모든 예외를 잡음

# try:
#     z = 'Cho'
#     x = name.index(z) # 0
#     print('{} Found it! {} in name' .format(z, x + 1))
# except Exception:
#     print('Not found it! - Occurred ValueError')
# else:
#     print('Ok! else.')

# print()


# 예제3 {e} 로 에러의 내용을 출력해 줌

# try:
#     z = 'Cho'
#     x = name.index(z) # 0
#     print('{} Found it! {} in name' .format(z, x + 1))
# except Exception as e:
#     print(e)
#     print('Not found it! - Occurred ValueError')
# else: # 예외가 발생하지 않아야 실행
#     print('Ok! else.')
# finally: # 예외 상관없이 무조건 마지막에 실행해줌
#     print('Ok! finally!')

print()

# 예제4
# 예외 발생 : raise
# raise 키워드로 예외 직접 발생

try:
    a = 'Kim'
    if a =='Kim':
        print('Ok! Pass!')
    else:
        raise ValueError
except ValueError:
    print('Occurred! Exception!')
else:
    print('Ok! else!')
