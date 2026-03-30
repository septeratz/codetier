import sys
# N은 총 끝점 수, M은 총 간선 수
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
# 네트워크 배열 사용, 두 배열을 서로 이어주는 형태로 입력
net = [[] for _ in range(N+1)]
# 모든 네트워크를 돌면서 해당 입력 라인의 정점들이 이미 존재하는 네트워크에 있는지 확인
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)
# 방문 노드 체크, count 선언
visited = [False] * (N+1)
count = 0
def dfs(num):
    global count
    visited[num] = True
    for i in net[num]:
        if not visited[i]:
            count += 1
            dfs(i)


dfs(1)
print(count)