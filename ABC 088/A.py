N = int(input())
A = int(input())
residue = N % 500
if residue <= A:
    print("Yes")
else:
    print("No")