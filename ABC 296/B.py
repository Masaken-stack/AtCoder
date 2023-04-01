# B - Chessboard
# グリッドの状態を表す長さ8の 8つの文字列 S1 ,…,S8 が与えられます。
# Siは"."および"*"からなる長さ8の文字列です。
#S1,…,S8のなかに"*"はちょうど1つ存在します

input_grid = [list(input()) for _ in range(8)]

alphabet = "abcdefgh"
integer = "87654321"
grid = [[a + i for a in alphabet] for i in integer]
# 8*8のグリッドの中に"*"があるかどうかを判定する
# あれば、その位置と合致するgridを出力する
for i in range(8):
    for j in range(8):
        if input_grid[i][j] == "*":
            print(grid[i][j])
            exit()
