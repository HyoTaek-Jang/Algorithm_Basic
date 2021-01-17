'''
그리디 알고리즘 : 현재 상황에서 당장 좋은 것만 고르는 방법
문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력
그리디 해법 : 현재에서 좋은 것만 선택해도 최적인지 확인을 해야함.

일반적으로 그리디는 최적의 해를 보장할 수 없다.
'''

'''
거스름 돈 아이디어:
최적의 해를 구하기 위해선, 가장 큰 화폐 단위부터 돈을 거슬러 주면 된다.
큰 단위가 작읜 단위의 배수이기에 가능하다. 
'''

def makeOne(target, value):
    count = 0
    while(target !=1):
        if(target%value==0):
            target /= value
            count+=1
            continue
        target -= 1
        count += 1
    print(count)

def makeOneSol(target, value):
    result = 0
    while True:
        N = (target//value)*value
        result += (target-N)
        target = N
        if (target<value):
            break
        target /= value
        result += 1
    result += (target-1)
    print(result)

makeOne(25,3)
makeOneSol(25,3)

def moreBigger(datas):

    list = [int(a) for a in str(datas)]
    list.sort()
    value = 0
    for data in list:
        if(value <= 1 or data <= 1):
            value += data
            continue
        value *= data
    print(value)

moreBigger('567')

# 백준 1439번 뒤집기
def reverseCard():
    card = input()
    cardList = []
    compList = []
    for i in str(card):
        if not cardList:
            cardList.append(i)
        else:
            if(cardList[0] == i):
                cardList.append(i)
            else:
                compList.append(''.join(cardList))
                cardList.clear()
                cardList.append(i)
    compList.append(''.join(cardList))

    num_1 = 0
    num_0 = 0
    for data in compList:
        if data[0] == '1':
            num_1 += 1
        else:
            num_0 += 1
    print(num_0 if num_1>num_0 else num_1)
    '''
    str = input()

    count_zero = 0
    count_one = 0
    num = -1
    next = 0
    
    for i in range(0, len(str)):
        next = int(str[i])
        if num != next:
            if next == 0:
                count_zero += 1
            else:
                count_one += 1
        num = next
    
    print(min(count_zero, count_one))
    '''

reverseCard()