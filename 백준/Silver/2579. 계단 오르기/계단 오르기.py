import sys
# N 입력
N = int(input())

# 계단이 1칸이면 그냥 그거 출력
if (N == 1):
    print(int(input()))
    exit()

# 계단 배열 입력
stairs=[]
for i in range(N):
    stairs.append(int(sys.stdin.readline()))

# 계단이 2칸이면 2개 합한거 출력
if (N == 2):
    print(stairs[1] + stairs[0])
    exit()
    
# 첫 인덱스 처리
dp = [0]*(N)
dp[0] = stairs[0]
dp[1] = stairs[1] + dp[0]
dp[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
# 이후 1칸일 때, 2칸일 때 계산
# 2칸은 마음대로 할 수 있지만, 1칸은 이전에 2칸을 오른 상태에서만 가능하므로 식을 이렇게 짜야 됨
for i in range(3, N):
    one = dp[i-3] + stairs[i-1] + stairs[i]
    two = dp[i-2] + stairs[i]
    dp[i] = max(one, two)
# 계산 결과 출력
print(dp[-1])