import sys
sys.stdin = open('input.txt')

t = int(input())

dp = [1] * 100

for i in range(2, 100):
    dp[i] += dp[i - 2]

for i in range(3, 100):
    dp[i] += dp[i - 3]

for _ in range(t):
    n = int(input())
    print(dp[n])