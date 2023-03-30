# a_500 = int(input())
# b_100 = int(input())
# c_50 = int(input())
# x_total = int(input())

# count = 0
# for i in range(a_500 + 1):
#     for j in range(b_100 + 1):
#         for k in range(c_50 + 1):
#             if 500 * i + 100 * j + 50 * k == x_total:
#                 count += 1

# print(count)

## 処理速度を早くするためのアルゴリズム修正（半分になった！）
a_500 = int(input())
b_100 = int(input())
c_50 = int(input())
x_total = int(input())

count = 0
for i in range(a_500 + 1):
    for j in range(b_100 + 1):
        k = x_total - (500 * i + 100 * j)
        if k >= 0 and k // 50 <= c_50:
            count += 1

print(count)