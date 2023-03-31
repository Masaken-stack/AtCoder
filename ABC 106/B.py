# Title: 105
def divisors_count(num):
    divisors = 0
    for i in range(1, num+1):
        if num % i == 0:
            divisors += 1
    return divisors

n = int(input())
cnt = 0
# 1からnまでの奇数のうち、約数が8個のものをカウント
for i in range(1, n+1, 2):
  if divisors_count(i) == 8:
    cnt += 1
print(cnt)