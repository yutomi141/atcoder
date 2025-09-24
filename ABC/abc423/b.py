N = int(input())
L = list(map(int, input().split()))

left = -1
right = -1

if 1 in L:
    left = L.index(1)

    right = len(L) - 1 - L[::-1].index(1)
    
print(right - left )