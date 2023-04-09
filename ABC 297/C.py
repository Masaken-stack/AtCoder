# 高橋君は部屋に PC を沢山置こうとしています。そこで最大何台の PC を部屋に置けるか調べるプログラムを書くことにしました。
# H個の長さWの.,tからなる文字列Sが与えられる

#操作回数の最大化を目指す時、終了時の状態を出力する
H, W = map(int, input().split())
S = [list(map(str, input())) for _ in range(H)]

# 1≤i≤H, 1≤j≤W−1 を満たす整数であって、Siのj番目の文字も j+1 番目の文字も T であるようなものを選ぶ。
# Siのj番目の文字をPで置き換え、Siの j+1 番目の文字を C で置き換える。
for i in range(1, H+1):
    for j in range(1, W):
        # Siのj番目も j+1 番目の文字も T である場合
        if S[i-1][j-1] == "T" and S[i-1][j] == "T":
            # Siのj番目の文字をPで置き換え、Siの j+1 番目の文字を C で置き換える。
            S[i-1][j-1] = "P"
            S[i-1][j] = "C"
            
print("\n".join(["".join(row) for row in S]))
