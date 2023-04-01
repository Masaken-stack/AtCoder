import itertools

N = int(input())
point = [tuple(map(int,input().split())) for _ in range(N)]

sum_range = 0
# 経路の順列を全探索
for route in itertools.permutations(point):
    tmp_range = 0
    for i in range(N-1): # 経路の距離を計算
        tmp_range += ((route[i][0]-route[i+1][0])**2 + (route[i][1]-route[i+1][1])**2)**0.5
    sum_range += tmp_range

# 経路の順列の数で割る
print(sum_range/len(list(itertools.permutations(route))))


