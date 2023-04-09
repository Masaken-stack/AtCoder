A, B = map(int, input().split())
count = 0
while True:
  if A < B:
    tmp = A
    A = B
    B = tmp
  if B<=0:
    break
  count += A//B
  A = A%B
print(count-1)