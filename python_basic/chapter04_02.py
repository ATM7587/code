# Chapter04-2
# 파이썬 반복문
# For 실습

# 코딩의 핵심
# for in <collection>
#   <loop body>

for v1 in range(100): # 0 ~ 9
    print('v1 is :', v1)

print()

for v2 in range(1,11): # 1 ~ 10
    print('v2 is :', v2)

print()

for v3 in range(1, 11, 2):
    print('v3 is :', v3)

# 1 ~ 1000까지의 합
sum1 = 0

for v in range(1, 1001):
    sum1 += v

print(sum1)

print()
sum1 = 0

for v in range(1, 1001):
    sum1 += v
    if v % 100 == 0:
        print('1 + 2 + 3 + ... + ', v, '=', sum1)

print('1 ~ 1000 sum : ', sum(range(1,1001)))

print(type(range(1,11))) # 연속적인 데이터를 담는 리스트를 생성해줌

sum1 = 0

for v in range(4,1001,4):
    print(v)
    sum1 += v

print(sum1)

print('1~1000에서 4의 배수의 합 :', sum(range(4,1001,4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim', 'Park', 'Cho', 'Lee', 'Choi', 'Yoo']

for n in names:
    print('You are : ', n)


# 예제2
lotto_numbers = [11, 19, 21, 28, 36, 37]

for n in lotto_numbers:
    print("Current number : ", n)

print()

# 예제3
word = "Beautiful"

for s in word:
    print('word : ', s)

print()
# 예제4
my_info = dict(
    name = 'Lee',
    Age = 33,
    City = 'Seoul'
)

for key in my_info:
    print('key :', my_info[key])

for v in my_info.values():
    print('value :', v)


# 예제5
name = 'FineAppLE'
name2 = ''
for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())


# break (조건이 만족되었을 때 반복문을 종료함)

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 46, 38]

for num in numbers:
    if num == 34:
        print('Found : 34!')
        break
    else:
        print('Not found : ', num)


# continue

lt = ["1", 2, 5, True, 4.3, complex(4)]

for v in lt:
    if type(v) is bool:
        continue
    else:
        print("current type:", v, type(v))
        print("multiply by 2", v, v * 2)


# for - else

numbers = [14, 3, 4, 7, 10, 24, 17, 2, 33, 15, 34, 46, 38]

for num in numbers:
    if num == 46:
        num = 46
        print("Found : ", num)
        break
else:
    print('Not Found :', num)


# 구구단 출력

for i in range(2, 10):
    for j in range(1, 10):
        print('{:4d}'.format(i *j), end='')
    print()

# 변환 예쩨
name2 = 'Aceman'

print('Reversed', reversed(name2))
print('List', list(reversed(name2)))
print('Tuple', tuple(reversed(name2)))
print('Set', set(reversed(name2))) # 순서x