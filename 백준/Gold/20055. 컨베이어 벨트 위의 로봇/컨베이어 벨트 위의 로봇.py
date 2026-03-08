import sys
from collections import deque

N, K = map(int, sys.stdin.readline().split())
belt = deque(list(map(int, sys.stdin.readline().split())))
robot = deque([0] * N)
result = 0
count = belt.count(0)

while count < K:
    result += 1
    # 회전
    belt.rotate(1)
    robot.rotate(1)
    # 마지막 로봇 하차
    robot[N-1] = 0

    # 로봇 전진
    for i in range(N-1, 0, -1):
       if belt[i] > 0 and robot[i] == 0 and robot[i-1] == 1:
            robot[i] = 1
            robot[i-1] = 0
            belt[i] -= 1
    # 마지막 로봇 하차
    robot[N-1] = 0
    
    # 로봇 올려놓기
    if belt[0] > 0 and robot[0] == 0:
        robot[0] = 1
        belt[0] -= 1
    
    # 내구도 체크
    count = belt.count(0)
    
print(result)
      

