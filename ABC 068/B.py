n = int(input())
# max関数にkey引数を渡して、最大値を求める
# 1からnまでの数値をリストにしてそれぞれの数値を2進数に変換した(bin())後、
# 逆順([::-1])にして、最初に出てくる1の位置を求める
max_num = max(range(1, n+1), key=lambda i: bin(i)[::-1].find('1'))
print(max_num)