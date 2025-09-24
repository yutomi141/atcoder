X , C =map(int, input().split())

money = 0

for i in range(0, round(X/1000)):
  if i * 1000 + i * C <= X:
    money = i * 1000
    
print(money)