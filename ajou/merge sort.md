# divide and conquer approach

재귀적으로!

- insertion sort used an incremental approach to sorting
  정렬된 값이 점점 늘어남

- divide and conquer approach
  Divide : 문제를 작게 나눔. 반씩 나눔
  Conquer : 재귀적으로 같은 함수를 반복하며 서브 문제를 풀어나가는과정, 반복해서 반으로 나누고 또 나눔.
  결국 재귀적으로 콜해서 사이즈가 1되면 그때 다시 incremental하게 다시 정렬
  combine : 풀었던 문제를 다시 합치는 과정. conquer로 정렬된 두 배열을 합치는 과정

- merge sort
  consists of recursive calls

  - kye subroutine : MERGE!!
    두 배열을 맨 앞 인덱스부터 비교하고 작은걸 넣고 인덱스 올리는 방법을 반복!
    총 n번 걸림

초기조건
: 결과리스트가 아무것도 없는 상태. 가장 작은 것을 포함한다고 말할 수 있다!
유지조건
: 레프트, 라이트도 이미 정렬이 되있기에 둘이 비교해서 작은 값이 제일 작은 값이라 할 수 있다!~
종료조건
: k = r+1 이면 종료. 물론 정렬이 됐을거임~

### merge-sort

1. 리스트의 길이가 2^n이라고 가정 - 트리로 분석하려고
2. 리스트는 정렬되지 않은 수들.
3. 반으로 쪼개서 계속 쪼갬
4. 결국 원소가 1개가 되면 merge로 정렬을 만듬.

리컬시브한 알고리즘을 recurrence equation 이라고 부름

constant time이 소요된다 세타(1)로 표현

divide and conquer 알고리즘 런타임 분석
divide 걸리는 시간
: D(n)
combine 걸리는 시간
: C(n)

T(n) = 세타(1) if n<=c
= k(재귀콜 몇번?)T(n/m(나눠지는수 머지는 2)) + D(n) + C(n)

머지소트
base case
n=1 이면 이미 정렬이 됐기에 세타(1)

divide
D(n) = 세타(1) 그냥 미드값 구해서 나누면 되기에!

conquer
새로운 인풋은 반이니까 n/2 인데 이게 두개임 2T(n/2)

combine
서로 인덱스 비교해서 쭉 결과리스트에 넣음 즉 n번 돔.
C(n) = 세타(n)

따라서 머지소트는!
T(n) = 세타(1) if n = 1
T(n) = 2T(n/2) + 세타(1) + 세타(n) if n > 1

세타(1)을 무시하면

T(n) = c if n = 1
T(n) = 2T(n/2) + c(n) if n >1

인풋이 n = 2^k이라고 가정했기에 log2n만큼 시간이 필요함.
정확하게 말하면 log2n+1임 처음 불러오는 과정이 필요하니까!

리컬전 트리
T(n)에서 T(n/2) \* 2로 나뉨 그때 T(n)은 cn으로 됨 왜냐하면 컴바인하니까!
이런 식으로 나누면서 내려감 1이 될떄까지!
그때, 처음 cn이 2씩 계속 나눠서 내려가면 height = logN이 됨
리프노드의 개수는 n개임
각 층마다 cn이 걸리는데 높이가 logn임 그래서 총 걸리는 시간이 cnlogn

위에서 정의한 리컬시브 콜이 log2n+1이니까
토탈 코스트는 cn(log2n+1)임, 근데 c는 무시하니까 nlogn + n임. 근데 최대만 고려하니까 nlogn

타이트 바운드임 머지소트는! 항상 평균적으로 성능이 조음!
