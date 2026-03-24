

def dfs(day, man):
    global answer
    # 500 이하 나오면 즉시 종료
    if man < 500:
        return
    # N까지 갔으면 성공, 1 추가
    if day == N:
        answer += 1
        return
    # DFS 탐색
    for i in range(N):
        # 방문 노드 확인
        if not visited[i]:
            
            visited[i] = True
            
            dfs(day + 1, man + nlist[i] - K)
            # 탐색 후 방문 체크 해제
            visited[i] = False

import sys

N, K = map(int, sys.stdin.readline().split())
nlist = list(map(int, sys.stdin.readline().split()))


visited = [False] * N
answer = 0

dfs(0, 500)

print(answer)