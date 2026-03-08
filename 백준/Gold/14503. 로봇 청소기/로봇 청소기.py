import sys

# 입력받기
N, M = map(int, sys.stdin.readline().split())
robot = list(map(int, sys.stdin.readline().split()))
tile=[]
for i in range(N):
    tile.append(list(map(int, sys.stdin.readline().split())))

# 기본 변수 설정
curx = robot[0]
cury = robot[1]
curd = robot[2]
# 회전 각도 설정
rx = [-1, 0, 1, 0] 
ry = [0, 1, 0, -1]
# 정답 변수
clean = 0

while True:
    
    # 1. 청소 (0일 때만 청소)
    if tile[curx][cury] == 0:
        tile[curx][cury] = -1
        clean += 1
    
    # 2. 청소 칸 검사
    uncFlag = False
    for i in range(4):
        if tile[curx + rx[i]][cury + ry[i]] == 0: 
            uncFlag = True
            break
    
    # 2-1. 청소해야 하는 칸 없고, 후진 가능 시 후진
    if not uncFlag:
        back_d = (curd + 2) % 4 # 고개는 돌리지 않고 뒤통수 방향만 계산
        if tile[curx + rx[back_d]][cury + ry[back_d]] == 1:
            break # 작동 멈춤 (루프 종료)
        curx += rx[back_d]
        cury += ry[back_d]

    # 3-1. 청소해야 하는 칸 있을 경우, 반시계 90도 회전
    else: 
        for i in range(4):
            curd = (curd + 3) % 4
            # 3-2. 청소 안 돼 있으면 전진, 아니면 다시 회전
            if tile[curx + rx[curd]][cury + ry[curd]] == 0:
                curx += rx[curd]
                cury += ry[curd]
                break


print(clean)
