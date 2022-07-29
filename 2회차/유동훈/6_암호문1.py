import sys

sys.stdin = open("_암호문1.txt")

for i in range(1, 11):
    
    N = input()
    ori_crypt = input().split()
    n = int(input())
    command = input().split()
    mod_crypt = []

    cnt = 2
    for j in range(n):
        ori_str = ''.join(ori_crypt[int(command[cnt-1])])
        ori_crypt = ''.join(ori_crypt)
        mod_str = ' '.join(command[cnt+1:cnt+1+int(command[cnt])])
        mod_str = ori_str + ' ' + mod_str
        ori_crypt = ori_crypt.replace(ori_str, mod_str)

        cnt += int(command[cnt]) + 3


    print(f'#{i}', end=' ')
    for k in range(10):
        print(list(mod_crypt)[k], end=' ')