N,M = map(int,input().split())

# K[i][0]はスイッチの数
# K[i][1]からK[i][K[i][0]]はスイッチの番号
K = []
for i in range(M):
    row = list(map(int,input().split()))
    K.append(row)

# pは0または1
P = list(map(int,input().split()))

ans = 0
# スイッチのON/OFFの組み合わせを全て調べる
for i in range(2**N):
    # スイッチのON/OFFの状態を格納するリスト
    switch = [0] * N
    for j in range(N):
        # iの２進数表現においてj桁目が1ならスイッチをONにする
        if ((i >> j) & 1):
            switch[j] = 1
    
    # 電球が点灯するかどうかの判定
    flag = True
    for j in range(M):
        on_cnt = 0
        for k in range(1, K[j][0]+1):
            # スイッチがONならon_cntをインクリメント
            if switch[K[j][k]-1] == 1:
                on_cnt += 1
        # 電球が点灯しないならflagをFalseにしてbreak
        if on_cnt % 2 != P[j]:
            flag = False
            break

    # 電球が全て点灯するならansをインクリメント
    if flag:
        ans += 1

print(ans)