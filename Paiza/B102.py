import copy

# "#"は黒, "."は白
H, W, N = map(int, input().split())
input_list = [input().strip() for i in range(H)]
grid = [list(row) for row in input_list]
operation = str(input())

# 上下左右４つの要素について
# 膨張:1画素でも黒い画素があれば黒に置き換える処理
# 収縮:1画素でも白い画素があれば白に置き換える処理
# operationの文字列で処理を分岐
grid_copy = copy.deepcopy(grid)
for op in operation:
    # 膨張(Dilation)の場合
    if op == "D":
        for h in range(H):
            for w in range(W):
                # 黒い画素があれば
                if grid[h][w] == "#":
                    # 下, 上, 左, 右の画素を黒に置き換える
                    if h - 1 >= 0:
                        grid_copy[h - 1][w] = "#"
                    if h + 1 < H:
                        grid_copy[h + 1][w] = "#"
                    if w - 1 >= 0:
                        grid_copy[h][w - 1] = "#"
                    if w + 1 < W:
                        grid_copy[h][w + 1] = "#"
        # grid_copyをgridに深いコピー
        grid = copy.deepcopy(grid_copy)
    # 収縮(Erosion)の場合
    elif op == "E":
        for h in range(H):
            for w in range(W):
                if grid[h][w] == ".":
                    if h - 1 >= 0:
                        grid_copy[h - 1][w] = "."
                    if h + 1 < H:
                        grid_copy[h + 1][w] = "."
                    if w - 1 >= 0:
                        grid_copy[h][w - 1] = "."
                    if w + 1 < W:
                        grid_copy[h][w + 1] = "."
        # grid_copyをgridにコピー
        grid = copy.deepcopy(grid_copy)
# 出力
print(*[''.join(map(str, row)) for row in grid], sep='\n')