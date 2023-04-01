import itertools

def dfs(v, visited):
    # 深さ優先探索
    visited[v] = True
    if all(visited):
        return 1

    cnt = 0
    for u in graph[v]:
        if not visited[u]:
            cnt += dfs(u, visited[:])
    return cnt

if __name__ == '__main__':
    # メインルーチン
    N, M = map(int, input().split())
    graph = [[] for _ in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        # 無向グラフの隣接リストを作成
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    # 頂点1から深さ優先探索を開始し、
    # 訪問済みの頂点をvisitedに記録する
    ans = 0
    visited = [False] * N # 訪問済み頂点の初期化 
    visited[0] = True # 頂点1を訪問済みにする
    for v in graph[0]:
        # 頂点vから深さ優先探索を行う
        ans += dfs(v, visited[:])

    print(ans)

