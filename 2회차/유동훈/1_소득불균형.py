import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    income = list(map(int,input().split()))
    
    cnt = 0
    for j in income:
        if j <= sum(income)/N:
            cnt += 1

    print(f'#{i} {cnt}')