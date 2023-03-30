import re
S = input()

# 正規表現パターン
pattern = re.compile(r"^(dream|dreamer|erase|eraser)+$")

if re.match(pattern, S):
    print("YES")
else:
    print("NO")
