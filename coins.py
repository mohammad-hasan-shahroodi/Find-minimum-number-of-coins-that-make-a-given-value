money = int(input())
coins = [int(i) for i in input().split()]
s = [float("INF")]*(money+1)
s[0] = 0
for i in range(1,money+1):
    for j in coins:
        if j <= i :
            k = i - j
            if s[k]+1 < s[i]:
                s[i]=s[k]+1
print(s)    
