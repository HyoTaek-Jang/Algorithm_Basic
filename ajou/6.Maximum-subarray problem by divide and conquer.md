# Maximum subarray problem

문제를 받으면 인풋이랑 아웃풋을 명확하게 해라

input : A[1..n] of numbers (some of the numbers are negative)
output : 연속된 subarray, sum이 가장 큰 부분집합을 찾는거임!

Naive approach : 그냥 단순히 어떻게 풀 수 있는지 생각하는거. 이러면 한계점을 찾을 수 있음. 개선사항이랄까. 같은 계산을 많이하면 줄일 방법을 생각하고 그런거지~
n^2으로 각 인덱스마다 끝까지 돌 수 있음

divide and conquer로 nlogn으로 개선할 수 있음.
이 알고리즘을 쓰면 어떤 스탭이 필요할지 생각을 해야함. 어떻게 적용시킬지
문제를 나누고 - 하나가 될떄까지 - 그리고 solving하고 -conquer - combine

subproblem : A[low...high] low=1, high=n
divide : two subarr, 최대한 사이즈 비슷하게. 그래서 미드잡고 반반씩 나눔

- conquer : 나눈거에서 맥시엄 서브어레이를 찾는. 솔루션을 구하는 과정 -> 미드를 기준으로 크로스 되는 경우도 고려해야함.

      1. left half
      2. right half
      3. mid cross
      이중에서 젤 큰 놈을 가져감

  combine : 미드값 넘어가면서 멕시멈 섬어레이가 나오는 경우가 있을 수 있음. 그걸 잊지마~ [i..mid] [mid+1...j] 이런식

initial call : Find Max Subarr(A,1,n)(배열, left, right)
미드 값을 찾아서 디바이드하고
재귀적으로 자기자신을 콜하면서 lefthalf, righthalf를 넣어서 ㅇㅇ이 문제는 cross도 넣어주고 conquer를 함
baseCase는 원소가 1개인 경우

divide conquer 이기에 size가 power of 2라고 가정
T(n) 러닝타임

baseCase = T(n) = 세타(1)
recursive case : n>1
dividing 세타(1)
sub problem 길이를 반으로 나누고 각각 함수를 돌림 2T(n/2)
combine은 cross부분을 포함함 그건 세타(n)임. 미드기준으로 왼쪽으로 가고, 오른쪽으로 가고 ㅇㅇ
마지막으로 세개 값 비교 세타(1)ㅇㅇ

따라서!!!!!!!!!!
T(n) = 세타(1) + 2T(n/2) + 세타(n) + 세타(1)
= 2T(n/2) + 세타(n)

이건 멀지 소트의 리커런스랑 같음
따라서! nlogn!

아까 N^2 걸리는 naive보다 훨 낫쥬!
