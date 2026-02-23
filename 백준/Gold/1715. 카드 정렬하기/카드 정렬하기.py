"""
최소 힙을 사용해서 greedy를 이용해 풀어야 됨
DP로 풀 경우엔 입력값이 너무 커서 루프 돌다가 timeout당함
최소 힙 특성상 배열 정렬이 딱히 필요가 없고, 매우 빠르게 정렬이 가능하므로 그대로 쓰면 됨
2개 pop, 이후 pop한 것들 더해서 다시 push

"""
import sys
import heapq

# 입력받기
N = int(sys.stdin.readline())
cardlist = []
result = 0
for i in range(N):
    cardlist.append(int(sys.stdin.readline()))

# 최소 힙으로 만듦
heapq.heapify(cardlist)

# 힙 이용 계산 코드, 2개 pop 이후 더한 값을 push
while (len(cardlist) > 1):
    a = heapq.heappop(cardlist)
    b = heapq.heappop(cardlist)
    result += a + b
    heapq.heappush(cardlist, a+b)
    
# 최종 결과 출력
print(result)