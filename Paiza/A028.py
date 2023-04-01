# A028:武器の強化
S, P = map(int, input().split())

# 強化して得られる最終的な武器の強さの最大値を出力
# 強化後の武器の強さは X × (100 + q) / 100 の値の小数点以下を切り捨てた整数値

tuyosa = S
if P >= 10:
    tuyosa = (tuyosa * (100 + P)) // 100

else:
    for i in range(1, P+1):
        tuyosa = (tuyosa * (100 + 1)) // 100
 
print(tuyosa)