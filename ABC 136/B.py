N = int(input())

cnt = 0
#桁数が奇数であるものをカウントする
for i in range(1, N + 1):
    if len(str(i)) % 2 == 1:
        cnt += 1
print(cnt)