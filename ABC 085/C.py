N,Y = list(map(int,input().split()))

ans = [-1,-1,-1]
for yen_10000_count in range(N+1):
    for yen_5000_count in range(N+1-yen_10000_count):
        yen_1000_count = N - yen_10000_count - yen_5000_count
        if 10000*yen_10000_count + 5000*yen_5000_count + 1000*yen_1000_count == Y:
            ans = [yen_10000_count,yen_5000_count,yen_1000_count]
            break

print(*ans)