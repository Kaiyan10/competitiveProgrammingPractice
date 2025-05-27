N = int(input())
A = list(map(int, input().split()))

ans = 0

row_length = 0
for i in range(N):
    row_length += A[i]

diff = 0
for i in range(N):
    diff += A[i]*A[i]


ans =((row_length*row_length)-diff) //2
print(ans)