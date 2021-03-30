# 알고리즘 디자인 기법

1. divide-and-conquer
2. greedy
3. DP

## divide-and-conquer

### merge

divide : n/2
conquer : 사이즈가 1일때까지 재귀적으로 반복, 1이면 정렬
combine : 합침

### Recurrences

- one or more base cases
- adn itself, with smaller inputs

### recurrence for divide and conquer algo

T(n) = 세타(1) base case
T(n) = aT(n/b) conquer cost + D(n) divide const + C(n) combine cost

### why recurrences?

몇몇 알고리즘은 리커런스를 쓰면 설명하기 쉬워짐

### methods of solving rec

### recursion tree

### telescoping

주어진 식은 변형하고 소거해서 우리가 원하는 nlogn(머지소트)을 만드는거임

T(n) = T(n/2) + T(n/2) + n

(T(n) = T(n/2) + T(n/2) + n)/n

... 사진 참고

### induction

base case : n = 1
inductive hyphtesis : T(n) = n log2 n
위가 맞다고 가정하고 다음 스탭이 성립함을 보이면 됨
Goal : show that T(2n) = 2n log 2 (2n)

### the master method

공식만 외우면 솔루션을 찾을 수 있는 레시피.
꼭 이게 정답이 아님.

T(n) = aT(n/b) + f(n)(머지할때 걸리는 시간 같은거.)
3가지 케이스를 외워야함.
그리고 그대로 적용하는거.

1. T(n) = aT(n/b)+f(n) 일때
   if f(n) = O(n^(logb a - 입실론(constant)))
   then T(n) = 세타(n^(logb a))
2. ...
3. ...
   강의노트 참고
