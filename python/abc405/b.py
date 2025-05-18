n, m = map(int, input().split())
a = list(map(int, input().split()))

result =  True

nowLength = n
trialCount= 0

while(result):
    for i in range(m):
        if i+1 not in a:
            print(trialCount)
            exit()
    del a[-1]
    trialCount+=1
