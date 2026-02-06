
import sys
# 입력받기
N = int(sys.stdin.readline())
# 한 줄 입력받고, 공백 기준 분리, int로 변환 후 리스트로 변환
scores = list(map(int, sys.stdin.readline().split()))

# 평균 계산용 변수
maxx = 0
ssum = 0

# 최고 점수 찾음
for i in scores:
    if maxx < i: maxx = i

# 점수 변환 및 평균 계산용으로 합계 계산
for i in range(N):
    scores[i] = scores[i] * 100 / maxx
    ssum += scores[i]

# 변환된 점수 평균 계산
print(ssum / N)

