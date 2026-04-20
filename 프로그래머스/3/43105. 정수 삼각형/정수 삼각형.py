def solution(triangle):
    # DP 배열, 미리 0으로 채워넣음
    dp = [0 for _ in range(len(triangle))]
    # 왼쪽 끝, 오른쪽 끝 계산용, 필요없을수도 있음
    lsum = rsum = 0
    lsum = dp[0] = triangle[0][0] + triangle[1][0]
    rsum = dp[1] = triangle[0][0] + triangle[1][1]
    # dp 개시, 앞 2개는 미리 계산했으니 넘어감
    for i in range(2, len(triangle)):
        # dp 계산용 temp 배열
        temp = [0 for _ in range(i)]
        # j-1 + j가 큰지, j + j가 큰지 비교해서 큰 걸로 넣음
        for j in range(1, len(triangle[i])-1):
            temp[j] = max(dp[j-1] + triangle[i][j], dp[j] + triangle[i][j])
        # 왼쪽 끝, 오른쪽 끝 계산
        dp[0] = lsum = lsum + triangle[i][0]
        dp[i] = rsum = rsum + triangle[i][i]
        # 계산 결과 dp에 반영
        for j in range(1, len(triangle[i])-1):
            dp[j] = temp[j]
    # 가장 큰 dp값 리턴
    answer = max(dp)
    return answer