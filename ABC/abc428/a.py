S, A, B, X = map(int, input().split())

T = A + B
q = X // T
r = X % T

run_time = min(r, A)
distance = q * (S * A) + run_time * S

print(distance)
