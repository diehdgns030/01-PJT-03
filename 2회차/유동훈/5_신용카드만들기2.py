import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
start = [3, 4, 5, 6, 9]

for i in range(1, T+1):
    numbers = input()
    numbers = numbers.replace('-', '')

    if len(numbers) == 16 and int(numbers[0]) in start:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')
