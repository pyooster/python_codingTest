# 이모티콘 할인행사
from itertools import product

def solution(users, emoticons):
    emotiPlus = 0
    totalPaid = 0
    discounts = product([10,20,30,40],repeat=len(emoticons))
    
    for discount in discounts:  # 경우의 수
        buyPlus = 0
        buyTotal = 0

        for user in users:
            paid = 0
            
            for i in range(len(emoticons)):
                if(discount[i] >= user[0]): # 할인이 사용자의 기준보다 높거나 같음(산다)
                    paid += emoticons[i] * (1 - discount[i]/100)                 
            
            if(paid >= user[1]):    # 지불한 값이 가진 돈보다 크면
                buyPlus += 1
            else:   # 전체 구매비용 추가
                buyTotal += paid

        if(emotiPlus < buyPlus):    # 이모티콘 플러스 가입횟수가 더 많아짐, 갱신
            emotiPlus = buyPlus
            totalPaid = buyTotal
            
        elif (emotiPlus == buyPlus):  # 플러스 가입횟수 같을때, 돈 더 많이 벌었으면 갱신
            if buyTotal > totalPaid :
                totalPaid = buyTotal
    
    return [emotiPlus, totalPaid]
