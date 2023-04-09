s = input()

b_indexes = [i for i, c in enumerate(s) if c == "B"]
if any(i % 2 == j % 2 for i in b_indexes for j in b_indexes if i < j):
    print("No")
    exit()

r_indexes = [i for i, c in enumerate(s) if c == "R"]
if len(r_indexes) < 2 or "K" not in s:
    print("No")
    exit()
    
k_index = s.index("K")
if not any(r_indexes[0] < k_index < r_indexes[1] for i in range(len(r_indexes) - 1)):
    print("No")
    exit()

print("Yes")