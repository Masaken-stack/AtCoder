N = int(input())
point = [list(map(int,input().split())) for _ in range(N)]

last_point = 0 #前回の位置
movable_distance = 0 #移動可能距離
# tが1増えるごとにx or yが1増える
# tが1増えるごとにx or yが1減る
# (0,0)から(x,y)までの距離は|x| + |y|
for i in range(N):
    t,x,y = point[i]
    movable_distance = t - movable_distance
    # t - x - yが奇数のときは到達不可能
    # 前回の位置と今回の位置の距離が、移動可能距離を超えたときは到達不可能
    if ((t - x - y)%2 != 0) or abs(last_point - (x+y)) > movable_distance:
        print("No")
        exit()
    else:
        #前回の位置を保存
        last_point = x + y


print("Yes")