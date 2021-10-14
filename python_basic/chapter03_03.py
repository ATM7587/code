# Chapter03-3
# 파이썬 리스트
# 자료구조에서 중요
# 리스트 자료형(순서o, 중복o, 수정o, 삭제o)

# 선언
a = []
print(type(a))
b = list()
c = [70, 75, 80, 85] # len
d = [1000, 10000, 'Ace', 'Base', 'Captain']
e = [1000, 10000, ['Ace', 'Base', 'Captain']]
f = [21.42, 'footbar', 3, 4, False, 3.14159]

# 인덱싱 (원하는 데이터를 꺼내오는 과정)
print('>>>>>>>')
print('d - ', type(d), d)
print('d - ', d[1])
print('d - ', d[0] + d[1] + d[1])
print('d - ', d[-1])
print('e - ', e[-1][1])
print('e - ', list(e[-1][1]))

# 슬라이싱
print(">>>>>>>>>>>>")
print('d -', d[0:3])
print('d - ', d[2:])
print('e - ', e[-1][1:3])

# 리스트 연산
print(">>>>>>>>>>>>")
print('c+d = ', c + d)
print('c * 3', c * 3) # 순서는 유지한채로 리스트를 반복함
print("'Test' + c[0]", 'Test' + str(c[0]))

# 값 비교
print(c == c[:3] + c[3:])
print(c)
print(c[:3] + c[3:])
print()

# Identity(id)

temp = c
print(temp, c)
print(id(temp))
print(id(c))

# 리스트 수정, 삭제
print(">>>>>>>>>>>>")
c[0] = 4
print('c - ', c)
c[1:2] = ['a', 'b', 'c'] # 리스트와 리스트의 연산이라서 원소들이 바로 들어감 / 리스트 형태로 넣고 싶으면 이중괄호로 묶어야 함
print('c - ', c)
c[1] = ['a', 'b', 'c']
c[1] =  ['a', 'b', 'c']
print('c - ', c)
c[1:3] = []
print('c - ', c)
del c[2] # 삭제 / 삭제 한 후에는 그 뒤의 원소들이 빈 자리를 채워줌
print('c - ', c)
del c[2] # 삭제
print('c - ', c)

# 리스트 함수
print(">>>>>>>>>>>>")
a = [5, 2, 3, 1, 4]

print('a - ', a)
a.append(10) # 가장 오른쪽에 10을 추가함
print('a - ', a)
a.reverse() # 역순으로 바꿈
print('a - ', a)
a.sort() # 오름차순으로 정렬
print('a - ', a)
print('a - ', a.index(3), a[3])
a.insert(2,7) # 2번자리에 7을 추가함
a.sort()
print('a - ', a)
print('>>>>>>>>>>')
a.remove(10) # del은 위치를 지정해서 제거하는 예약어 / remove는 값을 지정하여 제거하는 함수
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.pop())
print('a - ', a)
print('a - ', a.count(4))
ex = [8,9]
a.extend(ex)
print('a - ', a)

# 삭제 : remove, pop, del

# 반복문 활용
while a:
    print(a.pop())
    #data = a.pop()
    #print(data)