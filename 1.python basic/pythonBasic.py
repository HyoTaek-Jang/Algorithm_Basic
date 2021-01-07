'''
시간 복잡도 : 수행시간
공간 복잡도 : 메모리 사용량
복잡도가 낮아야 좋은 알고리즘
->Big-O Notation(가장 빠르게 증가하는 항만고 려)을 사용하여 표현

알고리즘 문제 해결 과정
1. 지문 읽기
2. 요구사항, 복잡도 분석
3. 문제 해결을 위한 아이디어 찾기
4. 소스코드 설계

숫자 표현시 e를 활용하여 사용 가능 ex) 1e9 = 10000000000

실수값은 정확한 비교가 힘들 수 있음
그래서 반올림하며 비교함 round(123.1244444, 2)하면 둘째자리까지 출력함.

슬라이싱할때 [0:3] 이면 0,1,2 출력함

반복문에서 _는 반복을 위한 변수 값을 안쓸때 사용함.

문자열의 곱은 반복을 의미.
+로 문자열 연결 가능
문자열도 인덱싱과 슬라이싱 이용가능 but, 인덱스 값 변경 불가 immutable

() tuple은 값 변경 불가. but, 메모리 효율성 좋음
사용처 : 서로 다른 성질의 데이터를 묶어서 관리할떄 (학번, 성적, 이름) 
: 데이터의 나열을 해싱의 키 값으로 사용할때. 이뮤터블이라 키 값으로 사용 가능

집합
: 중복을 허용하지 않고, 순서가 없음
: 데이터의 존재여부를 위해 사용함

빠르게 입력받기 테크닉
sys.stdin.readline() 메소드 사용
입력후 엔터가 남아있어서 rstrip()을 사용해야함

# 파이썬 라이브러리
itertools: 순열과 조합 라이브러리
heapq : 힙 자료구조 제공
bisect : 이진 탐색 기능을 제공
collections : 덱, 카운터 등의 유용한 자료구조를 포함함
math : 필수적인 수학 기능을 제공

eval("~") ~문자열을 넣으면 계산해줌

Counter : 리스트처럼 반복 가능한 객체에서 내부 원소가 몇 번 등장했는지 알려줌

math.gcd(12, 24)(최대공약수)
lcm(최소공배수) 
'''
#리스트에서 특정 값을 가지는 원소를 모두 제거
a = [1,2,3,4,5,5,6,7]
b = [4,5]
lists = [c for c in a if c not in b]
print(lists)

#dictionary
data = dict()
data['fruit']= ['apple','banana']
data['price'] = 3500

if 'fruit' in data:
    print("과일있음")

print(data)
print(data.keys())
print(data.values())

#집합
data = set([1,1,1,2,3,4,5,5,5])
print(data)
# 합,차,교집합 연산가능 | - &

#Map
# datas = list(map(int,input().split()))
# print(datas)

#f-string
anwser= 7
print(f"장딥은 {anwser}입니다용")