"""
문제
수강신청의 마스터 김종혜 선생님에게 새로운 과제가 주어졌다. 

김종혜 선생님한테는 Si에 시작해서 Ti에 끝나는 N개의 수업이 주어지는데, 
최소의 강의실을 사용해서 모든 수업을 가능하게 해야 한다. 

참고로, 수업이 끝난 직후에 다음 수업을 시작할 수 있다. 
(즉, Ti ≤ Sj 일 경우 i 수업과 j 수업은 같이 들을 수 있다.)

수강신청 대충한 게 찔리면, 선생님을 도와드리자!

입력
첫 번째 줄에 N이 주어진다. (1 ≤ N ≤ 200,000)

이후 N개의 줄에 Si, Ti가 주어진다. (0 ≤ Si < Ti ≤ 109)

출력
강의실의 개수를 출력하라.

스케줄링 문제, greedy와 heapq(효율적인 비교를 위해 사용)를 사용하여 구현
새 task의 start 시각과 기존 task의 end 시각을 비교하여 start >= end인 경우 pop, 아닌 경우 그냥 push

"""

import sys
import heapq

# 입력받기
N = int(sys.stdin.readline())
nlist = []
for i in range(N):
    nlist.append(list(map(int, sys.stdin.readline().split())))

# start 기준으로 정렬
nlist.sort()

# heapq로 만듦
heaplist = []
heapq.heapify(heaplist)

# 첫 task 뽑아냄
heapq.heappush(heaplist, nlist.pop(0)[1])

# nlist가 빌 때까지 계속 pop하면서 하나씩 계산
while (nlist):
    task = nlist.pop(0)
    if (task[0] >= heaplist[0]):
        heapq.heappop(heaplist) 
    heapq.heappush(heaplist, task[1])

# heaplist의 길이가 스레드(강의실)의 수
print(len(heaplist))

