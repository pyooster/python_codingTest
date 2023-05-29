# 택배 배달과 수거하기
def solution(cap, n, deliveries, pickups):
    def sol(target_list):
        truck = cap
        tmp = 0
        i = n-1
        return_list = []

        while i >= 0:
            if target_list[i] == 0 :
                i -= 1
                continue

            tmp = max(tmp, (i+1))
            if truck >= target_list[i]:
                truck -= target_list[i]
                target_list[i] = 0
                i -= 1
            else :
                target_list[i] -= truck
                truck = 0

            if truck == 0:    # 배달할 수 있는 양 넘음, 돌아가야함
                return_list.append(tmp)
                truck = cap
                tmp = 0

        if tmp > 0:
            return_list.append(tmp)

        return return_list

    answer = 0
    deliver_list = sorted(sol(deliveries))
    pickup_list = sorted(sol(pickups))
    
    
    while deliver_list or pickup_list :
        if deliver_list :
            if pickup_list :
                answer += (max(deliver_list.pop(), pickup_list.pop())) *2
            else :
                answer += (deliver_list.pop())*2
        elif pickup_list :
            answer += (pickup_list.pop())*2
        
    return answer
