"""
입력
첫 번째 줄에 게임을 하는 사람의 수 N (1 <= N <= 100,000), 
현재 차례인 사람의 번호 M (1 <= M <= N), 부른 두부의 모 수를 나타내는 정수 
K (-100,000 <= K <= 100,000)가 주어진다.

출력
첫째 줄에 다음 차례인 사람의 번호를 출력하라.
"""
import sys
N, M, K = map(int, sys.stdin.readline().split())
nlist = [i+1 for i in range(N)]
mlist = [0] * N
# M 기준으로 요소 회전
for i in range(N):
    mlist[i-M] = nlist[i]
# 구하려는 인덱스 작업, 범위에 맞게 수정
k = K-3-1
while (k >= N):
    k -= N
while (k < -N):
    k += N
# 출력
print(mlist[k])