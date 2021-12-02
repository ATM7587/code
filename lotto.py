import random

order  = list(input("사람 이름을 입력해 주세요(띄어쓰기로 구분) : ").split())

print(f'{order}')

random.shuffle(order)

print(f'{order}')