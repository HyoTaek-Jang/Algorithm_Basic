'''
문자 클래스 [abc]
하면 안에 일치하는 문자가 있으면 매치
예를 들어서 'before'는 b가 있기에 매치
[a-c] = [abc]

Dot(.)
.은 줄바꿈을 제외한 모든 문자와 매치
a.b -> aab와 매치
abc는 ab사이에 문자가 없기에 매치되지 않는다.

반복 (*)
ca*t
ct는 a가 0번 반복이기에 매치

반복(+)
ca+t
이건 0번은 매치되지 않음.

반복({m,n},?)
ca{2}t
cat는 a가 1번이라 안됨
무조건 두번

ca{2,5}는 a가 2-5번

ab?c
는 b가 0,1회 일때 매치
? == {0,1}

파이썬에서 정규 표현식을 지원하는 re 모듈

import re

p(패턴) = re.compile('정규표현식')

m = p.match(' 비교대상')
매치되면 값 주고 매치가 안되면 None

s = p.search('비교대상')
매치와 다르게 첫번째가 일치하지 않아도 일치하는 구문이 있으면 매치 객체를 리턴함.

m = p.findall('대상')
일치하는 걸 리스트로 만들어줌

m = p.finditer('대상')
일치하는 애를 이터레이터(순환 할 수 잇는) 객체로 반환함.

match객체
.gruop() 매치된 문자열을 리턴
.start() 매치된 문자열의 시작 위치를 리턴
.end() 끝위치 리턴
.span() 시작과 끝에 해당되는 튜플을 리턴

옵션
DOTALL, S
컴파일 할 때 dot 사용할때, /n도 포함할 수 있게 함
p = re.compile('a.b', re.DOTALL or re.S

IGNORECASE, I
re.I 하면 대소문자 무시함.

정규표현식 안에서
^ : 맨처음
\s : 공백,
\w 알파벳, 숫자, _ 중 한 문자

re.M 멀티라인 옵션
각 줄마다 정규표현식에 걸리게 함.

VERBOSE, X
정규표현식이 길때 나눠서 쓸 수 있게해줌
re.VERBOSE

백슬래시를 쓰려면 \\ 두개써야함.
row string
r'문자열'하면 안에는 무조건 문자열
r'\bclass\b' -> 앞뒤에 공백이 있는 class

메타문자
| or을 의미함.

re.search('표현식', '비교문자') 쓰면 한번에 가능

$는 맨 끝을 의미.

\b 공백을 의미.

(ABC)+ 하면 ABC 반복되는 애를 찾음.

그루핑된 문자열에 이름 붙이기
(?P<name>\w+)
이면 이 그룹에 name이라는 이름이 붙음
m.gruop('name)으로 찾을 수 있음
정규 표현식을 \1 이나 \name 이렇게 재활용 가능'

특정부분까지 읽고 앞에 자르기?
(?=문자) 문자까지 자름.
'.+(?=ㅣ)'에서 :는 검색에 포함되나 결과에는 포함이 안됨

(?!)
 (?!~~~)는 포함 안되게

 문자열 바꾸기 sub
 정규 표현식 만들고
 p.sub로 바꿀 수 잇음
 p.sub('바꿀 대상'), '비교대상')
 비교대상에 검색된 애를 바꿈

 반복할 표현식이 있을때
 ex) <.*>이면 젤 크게 묶은게 <>면 잡히는데
 <.*?> 이면 최소한으로 잡아줌
 반복된 매타문자 뒤에 ?를 붙임
'''

import re

p = re.compile(r'[.]{2,}')
m = p.sub('.','...asdfasf..asdfas.asdf')

print(m)