
import sys

# 입력받기
N = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))

# DP list 초기화
dp = [[0] * N for _ in range(N)]

# 길이가 1인 경우
for i in range(N):
    dp[i][i] = 1

# 길이가 2인 경우, 글자만 같으면 회문
for i in range(N-1):
    if nlist[i] == nlist[i+1]:
        dp[i][i+1] = 1

# 길이가 3 이상인 경우, dp 사용
for leng in range(2, N):
    for start in range(N - leng):
        end = start + leng
        # nlist의 양 끝 부분이 같고, 그 안쪽이 pal이면 그 바깥도 pal 
        if dp[start+1][end-1] == 1 and nlist[start] == nlist[end]:
            dp[start][end] = 1

# 입력 로직 처리 
M = int(sys.stdin.readline())
for i in range(M):
    s, e = map(int, sys.stdin.readline().split())
    # index + 1로 들어가므로 -1 처리
    print(dp[s-1][e-1])