import math


def price(t, base_time, base_price, over_time, over_price):
    if t <= base_time:
        return base_price
    over_times = math.ceil((t - base_time) / over_time)
    return base_price + over_times * over_price


def solution(fees, records):
    in_out = {}
    parking_times = {}
    for record in records:
        t, car, inout = record.split()
        a, b = t.split(':')
        time = 60 * int(a) + int(b)
        if inout == 'IN':
            in_out[car] = time
            if car in parking_times:
                pass
            else:
                parking_times[car] = 0
        else:
            parking_times[car] += time - in_out[car]
            in_out.pop(car)
    for car in in_out:
        parking_times[car] += (60 * 23 + 59 - in_out[car])

    temp = {}
    for car in parking_times:
        temp[car] = price(parking_times[car], fees[0], fees[1], fees[2], fees[3])
    answer = []
    temp = list(sorted(temp.items()))
    for car, prices in temp:
        answer.append(prices)
    return answer


print(solution([180, 5000, 10, 600],["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))