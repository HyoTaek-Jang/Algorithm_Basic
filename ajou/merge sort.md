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
