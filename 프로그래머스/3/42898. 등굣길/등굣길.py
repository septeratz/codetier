def solution(m, n, puddles):
    # 그냥 곱하기를 해버리면 얕은 복사가 되버려서 똑같은 메모리를 공유하는 배열이 늘어남
    dp = [[0]*m for _ in range(n)]
    # 구석 자리 미리 넣음
    dp[0][0] = 1
    # 물웅덩이 추가
    for i in puddles:
        dp[i[1]-1][i[0]-1] = -1
    # 시작, 물웅덩이 피해서 dp 계산
    for i in range(0, n):
        for j in range(0, m):
            if (i == 0 and j == 0) : continue
            # 물웅덩이가 나오면 0으로 바꿔버림
            if dp[i][j] == -1:
                dp[i][j] = 0
                continue
            # 0부터 시작하므로 index를 벗어날 위험이 있음, if로 미리 계산
            up = dp[i-1][j] if i > 0 else 0
            left = dp[i][j-1] if j>0 else 0
            # 더함, 주어진 숫자로 나눈 나머지 리턴
            dp[i][j] = (up + left) % 1000000007
            
    # 학교까지 가는 모든 경우의 수 리턴
    answer = dp[-1][-1]
    return answer