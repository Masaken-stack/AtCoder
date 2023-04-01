# 二分探索
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    # leftとrightが逆転するまで繰り返す
    while left <= right:
        mid = (left + right) // 2

        # 見つかった場合はTrueを返す
        if arr[mid] == x:
            return True

        # 中央の値よりもxが大きい場合は、探索範囲を右半分に絞り込む
        elif arr[mid] < x:
            left = mid + 1

        # 中央の値よりもxが小さい場合は、探索範囲を左半分に絞り込む
        else:
            right = mid - 1

    return False


N, X = map(int, input().split())
A = list(map(int, input().split()))

# リストAをソートする
A.sort()

# リストAの要素を1つずつ処理する
for i in range(N):
    # A[i] - A[j] = X という式が成り立つため、
    # A[i] = A[j] + X という式も成り立ちます
    # A[i] + Xと等しい値を持つ要素が存在するかを二分探索で判定する
    if binary_search(A, A[i]+X):
        print("Yes")
        exit()

print("No")