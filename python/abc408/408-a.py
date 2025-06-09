n, s = map(int, input().split())
a = list(map(int, input().split()))

ans ="Yes"
s = s+ 0.5


for i in range(n):
    if i==0:
        if a[i] - 0>= s:
            ans ="No"
            break
    else:
        if a[i] - a[i-1]>= s:
            ans ="No"
            break

print(ans)

