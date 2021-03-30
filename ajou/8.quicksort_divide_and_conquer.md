# Quick sort

1. divide : 파티셔닝 함. 2개로! 나뉘는 방법이 퀵소트의 키포인트임! 피벗 잡는게 아주 중요함
   left array는 피벗보다 작거나 같게, right는 피벗보다 크게!
2. conquer : 리컬시브하게 자신을 콜함.
3. combine : trival, conquer하면서 정렬이 되기에 그냥 붙이면 됨

키포인트 : 파티셔닝을 어찌 할건가! 파티셔닝에선 피벗을 정하는게 가장 중요함.
피벗을 잘정해서 최대한 반절로 나누는게 좋지

처음 피벗은 레프트 사이드 값으로 선택.
그리고 값을 보면서 자신보다 크면 우측 사이드, 작으면 좌측 사이드에 넣음
레프트 라이트가 1이 될때까지

그리고 나중에 다 합쳐!!

A[p..r]
divide : A[p..q-1] : 피벗보다 작음, A[q+1..r] 피벗보다 큼, 이렇게 두개로 나눔. A[q]는 피벗. 파티셔닝을 하는건 피벗을 찾기위해!

conquer : 나눈걸 리컬시브하게 다시 콜

combine : 이미 정렬이 되서 걍 합침

퀵소트는 피벗을 뭐로할지 명확히 명시해야함
중간에 피벗이 바뀌진 않음

```
partition(A,p,r)
x=A[r]
i = p-1
for j = p to r-1
    if A[j] <= x
        i = i+1
        exchange A[i] with A[j]
exchange A[i+1] with A[r]
return i+1
```

i가 작은 값의 경계
그럼 i+1이 피벗위치가 됨
그러면 다음 나눌땐 [1~i] [i+2~r] 까지로 나누면 됨

## coreectness

### loop invariant

initialization : 레프트는 empty, right도 empty, A[r] 은 피벗이 맞음. 둘다 empty라 소트가 되있다?
우리가 원하는건 레프트는 피벗보다 작거나 같고 라이트는 피벗보다 커야함. 근데 값이 없으니까 맞음!?

maintenance : 스왑하면 유지되고 안해도 유지됨! 피벗보다 작거나 같아도 ㄱㅊ, 커도 ㄱㅊ

termination : j=r 되면 종료! 포문이 r-1까지라서

runtime for partition
결국 포문이 중요함 나머진 컨스턴스 타임이라. n번 도니까 세타(n)!

performance of quicksort
성능은 파티셔닝에 달려있음

밸런스가 잘 나눠있으면 머지소트만큼 좋음
근데 안나눠지면 최대 n^2까지 감

best case : 피벗이 중앙값이면 밸런스하게 피벗이 중앙에 위치해서 젤조음
T(n) = 2T(n/2) + 세타(n) = nlgn

worst case : 밸런스가 안잡혔을때, 최대값이나 최소값이면 조짐
T(n) = T(n-1) + T(0) + 세타(n) = T(n-1) + 세타(n) = 세타(n^2)

# big o을 증명하는거...? 긍까 베스트일때 왜 nlgn이고 워스트가 n^2인지!
