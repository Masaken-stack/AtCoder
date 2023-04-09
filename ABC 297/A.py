# N回クリック
# 時刻x1とx2の間隔がD以下であればダブルクリック成立

N, D = map(int, input().split())
T = list(map(int, input().split()))

# 最初にダブルクリックを成立させた時刻
# ダブルクリックを成立させてないならば-1
double_click_time = -1
for i in range(N):
    if i == 0:
        continue
    if T[i] - T[i-1] <= D: # ダブルクリック成立
        if double_click_time == -1:
            double_click_time = T[i]
            break # 一度ダブルクリック成立したら終了
    else: # ダブルクリック成立してない
        double_click_time = -1
print(double_click_time)