def solution(triangle):
    dp = [0 for _ in range(len(triangle))]
    lsum = rsum = 0
    lsum = dp[0] = triangle[0][0] + triangle[1][0]
    rsum = dp[1] = triangle[0][0] + triangle[1][1]
    for i in range(len(triangle)):
        if (i<2): continue
        temp = [0 for _ in range(i)]
        for j in range(1, len(triangle[i])-1):
            temp[j] = max(dp[j-1] + triangle[i][j], dp[j] + triangle[i][j])
        dp[0] = lsum = lsum + triangle[i][0]
        dp[i] = rsum = rsum + triangle[i][i]
        for j in range(1, len(triangle[i])-1):
            dp[j] = temp[j]
    answer = max(dp)
    return answer