# S = input()

# ans = 0
# # ACGTが連続した文字列の個数を出力する
# for i in range(len(S)):
#     for j in range(i + 1, len(S) + 1):
#         if all(s in "ACGT" for s in S[i:j]):
#             ans = max(ans, j - i)
# print(ans)

S = input()

ans = 0
cnt = 0
for s in S:
    if s in "ACGT":
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt = 0

print(ans)