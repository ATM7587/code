# Chapter03-4
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형(순서o, 중복o, 수정x, 삭제x) / 불변

# 선언

a = ()
b = (1) # 끝이 , 로 끝나야 튜플로 인식됨. 아닌 경우에는 int 등의 자료형으로 설정
c = (11, 12, 13, 14)
d = (100, 1000, 'Ace', 'Base', 'Captain')
e = (100, 1000, ('Ace', 'Base', 'Captain'))

# 인덱싱
print('>>>>>>>>>')
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d -', d[-1])
print('e -', e[-1])
print('e - ', list(e[-1][1]))

# 수정 X
# d[0] = 1500

# 슬라이싱
print('>>>>>>')
print('d - ', d[0:3])
print('d - ', d[2:])
print('e - ', e[2][1:3])

# 튜플 연산
print('>>>>>>')
print('c + d', c + d)
print('c * 3', c * 3)

# 튜플 함수
a = (5, 2, 3, 1, 4)
print('a - ', a)
print('a - ', a.index(3))
print('a - ', a.count(2))

# 팩킹 & 언팩킹

# 팩킹
t = ('foo', 'bar', 'baz', 'qux')

print(t)
print(t[0])
print(t[-1])

# 언팩킹1
(x1, x2, x3, x4) = t # 묶여있던 튜플의 값을 각각의 원소에 할당함

print(x1)
print(x2)
print(type(x3))
print(type(x4))

print(x1, x2, x3, x4)

# 팩킹 & 언팩킹
t2 = (1, 2, 3)
t3 = (4,)
x1, x2, x3 = t2 # 갯수가 맞아야만 언팩킹이 가능함
x4, x5, x6 = 4, 5, 6

print(t2)
print(t3)
print(x1, x2, x3)
print(x4, x5, x6)