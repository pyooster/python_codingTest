# 어떤 차량이 입차된 후에 출차된 내역이 없다면, 23:59 에 출차된 것으로 간주
# fees -> (기본 시간, 기본 요금, 단위 시간, 단위 요금)
# records > (시각, 차량번호, 내역)
# 차량 번호가 작은 자동차부터 청구할 주차 요금을 차례대로 담아 return
from collections import defaultdict


def solution(fees, records):
    car_cost = defaultdict(list)
    default_time, default_cost, unit_time, unit_cost = fees

    for record in records:
        time, car_num, io = record.split(" ")
        car_cost[car_num].append(time)

    for key in car_cost.keys():
        if len(car_cost[key]) % 2 == 1:
            car_cost[key].append('23:59')

    # key 값 기준 정렬
    # sorted 함수 -> list 를 리턴함..
    # dict 으로 다시 변환하면 됨
    car_cost = dict(sorted(car_cost.items()))
    print(car_cost)

    car_time_sum = []
    for key in car_cost.keys():
        # print(key)
        sum_hh = 0
        sum_mm = 0
        for i in range(0, len(car_cost[key]) - 1, 2):
            in_hh, in_mm = car_cost[key][i].split(":")
            out_hh, out_mm = car_cost[key][i + 1].split(":")
            sum_hh += int(out_hh) - int(in_hh)
            sum_mm += int(out_mm) - int(in_mm)

        car_time_sum.append(sum_hh * 60 + sum_mm)

    print(car_time_sum)
    answer = []
    for car_time in car_time_sum:
        cost = 0
        if car_time > default_time:
            cost += default_cost
            add_time = car_time - default_time
            if add_time % unit_time > 0:
                cost += ((add_time // unit_time) + 1) * unit_cost
            else:
                cost += (add_time // unit_time) * unit_cost
        else:
            cost = default_cost

        answer.append(cost)

    return answer