import sys
import heapq
N, M = map(int, sys.stdin.readline().split())
# 끝점, 소 개수 입력받기
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
# 1에서 2~N까지 가는 거리 계산용, 처음은 INF로 둠
INF = 10**9
dist = [INF] * (N+1)

def dijkstra(start):
    q = []
    # 노드 삽입
    heapq.heappush(q, (0, start)) 
    dist[start] = 0
    
    while q:
        cows, now = heapq.heappop(q)
        # 이미 처리된 적이 있는 노드라면 넘어감
        if dist[now] < cows:
            continue
            
        # 인접 노드 확인
        for next_node, weight in graph[now]:
            # 비용 계산, 비교 후 더 싸면 삽입
            cost = cows + weight
            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(q, (cost, next_node))

# 1번 출발
dijkstra(1)

# N번까지 최소 거리 출력
print(dist[N])