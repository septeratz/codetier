
from collections import deque
import sys
# 입력받기
N = int(sys.stdin.readline())
for i in range(N):
    # 변수 설정, 입력받기
    count = 1
    temp = list(map(int, sys.stdin.readline().split()))
    qlist = list(map(int, sys.stdin.readline().split()))
    qin = temp[1]
    # queue 설정
    queue = deque([(val, idx) for idx, val in enumerate(qlist)])

    while queue:
        # 가장 중요도 높은 문서의 위치 찾아서 그 문서 기준으로 큐 재배치
        max_list = max(queue, key=lambda x: x[0])
        max_idx = list(queue).index(max_list)
        
        queue.rotate(-max_idx)

        # 그 문서 출력
        queue.popleft()

        # 그 문서가 원래 찾던 문서인지 확인, 맞으면 다음 입력으로 넘어감
        if qin == max_list[1]: 
            print(count)
            break
        # 아니면 count++ 후 다음 루프 진행
        count += 1
        