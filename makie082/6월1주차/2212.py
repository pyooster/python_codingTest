n = int(input())
k = int(input())
sensor = list(map(int,input().split()))
sensor.sort()

dis = []

for i in range(n-1):
    dis.append(sensor[i+1]-sensor[i])

maxd = 0
for d in dis:
    if maxd < d:
        maxd = d

sorted_dis = sorted(dis)

result = 0
# 뒤에서 k-1개를 제외하고 더해줌
for sd in range(len(sorted_dis)-k+1):
    result += sorted_dis[sd]

print(result)