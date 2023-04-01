import itertools
 
N = int(input())
testimonies = [[] for _ in range(N)]

# 証言を受け取る
for i in range(N):
    for j in range(int(input())):
        x, y = map(int, input().split())
        testimonies[i].append((x, y))
 
ans = 0
# 全ての正直者の組み合わせを試す
for states in itertools.product([0, 1], repeat=N):
    # 矛盾がないか確認
    for i, state in enumerate(states):
        if state == 1:
            for t in testimonies[i]:
                if t[1] != states[t[0]-1]: #矛盾したらelse節をスキップ
                    break
            else: #すべての証言が矛盾しなかったら次のstateへ
                continue
            break # 矛盾が見つかったので現在のstatasを破棄
    else: # 全ての正直者について矛盾が見つからなかったら
        ans = max(ans, sum(states))
        
print(ans)