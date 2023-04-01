N = int(input())
S = str(input())

# i文字目がM：男性、F：女性
# 男女が交互に並んでいるかどうかを判定する
# 先頭の文字を取得
prev_cher = S[0]
for i in range(1, N):
    if S[i] == prev_cher:
        print('No')
        exit()
    #現在の文字を前の文字として更新
    prev_cher = S[i]

# ここまで来たら、男女が交互に並んでいる
print('Yes')