
# 두 노드 간 가장 긴 길이를 계산(end), mid를 그 길이와 1(최소, start)의 절반으로 잡음
# 이후 첫 노드부터 mid보다 긴 거리에 있는 노드들로 연결
# 그게 공유기 수보다 부족하면 mid를 절반으로 줄여서(end를 mid로) 다시 계산
# 그게 공유기 수보다 크면 길이를 1.5배로 늘려서(start를 mid + 1로) 다시 계산

def check_node(mid):
    count = 0
    node_start, node_end = 0, 1
    # mid보다 긴 길이의 노드만 연결
    while node_end < N:
        if nodes[node_end] - nodes[node_start] >= mid:
            # 연결 성공, count 증가
            count += 1
            node_start = node_end
        # 연결 실패, count 증가 안함
        node_end += 1 
        
    if (C - 1 <= count): return True
    else: return False


import sys

# 입력받기
N, C = map(int, sys.stdin.readline().split())
nodes=[]
for i in range(N):
    nodes.append(int(sys.stdin.readline()))

# 오름차순 정렬
nodes.sort()

# 초기 값 세팅
start = 1
end = nodes[-1] - nodes[0]
result = 1

# 결과값 찾는 루프
while (start <= end):
    mid = (start + end) // 2
    if check_node(mid):
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)