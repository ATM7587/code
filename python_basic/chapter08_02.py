# Chapter08-2
# 파이썬 외장(External Function) 함수
# 실제 프로그램 개발 중 자주 사용
# 종류 : sys, pickle, shutil, temfile, time, random 등

# 예제1
from math import e
import sys
print(sys.argv) # sys : 파이썬 인터프리터 관련 정보, 기능 제공 / argv : argument (인자값 제공)

# 예제2(강제 종료)
# sys.exit() 프로그램 자체를 강제종료하는 위험한 함수

# 예제3(파이썬 패키지 위치)
print(sys.path) # 모든 패키지들의 위치를 표시해준다.

# picke : 객체 파일 쓰기
import pickle # 파이썬에서 사용할 수 있는 객체, class 등을 저장장치에 쓰고 읽을 때 사용함

# 예제4(쓰기)

f = open("test.obj", 'wb')
obj = {1:'python', 2:'study', 3:'basic'}
pickle.dump(obj, f) # 쓸 때는 dump
f.close()

# 예제5(읽기)

f = open('test.obj', 'rb')
data = pickle.load(f) # 읽을 때는 load
print(data,type(data))
f.close()

# os : 환경 변수, 디렉토리 # 윈도우나 맥에서 하는 것을 파이썬으로 할 수 있게 해줌
# mkdir, rmdir(비어 있으면 삭제), rename

# 예제6
import os
print(os.environ)
print(os.environ["VSCODE_GIT_ASKPASS_NODE"])

# 예제7(현재 경로 표시)
print(os.getcwd()) # 현재 파이썬이 실행되는 경로를 보여줌

# time : 시간 관련 처리
import time

# 예제8
print(time.time())

# 예제9(형태 변환)
print(time.localtime(time.time()))

# 예제10(간단하게 표현)
print(time.ctime())

# 예제11(형식 표현)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 예제12(시간 간격 발생)
# for i in range(5):
#     print(i)
#     time.sleep(1) # 1초 간격으로 5번 실행됨

# random : 난수 리턴
import random

# 예제13
print(random.random()) # 0 ~ 1 사이의 실수

# 예제14
print(random.randint(1, 45)) # 1부터 45까지
print(random.randrange(1,45)) # 1부터 44까지

# 예제15(섞기)
d = [1,2,3,4,5]
random.shuffle(d)
print(d)

# 예제16(무작위 선택)
c = random.choice(d)
print(c)

# 예제16(연습)
e = list(input("사람 이름을 입력해 주세요(띄어쓰기로 구분) : ").split())
c = random.choice(e)
print(f'{c}')

# webbrowser : 본인 OS의 웹 브라우저 실행

import webbrowser

webbrowser.open("http://google.com")


webbrowser.open_new("http://google.com")