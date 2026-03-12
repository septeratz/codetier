import sys

# 입력받기
N = int(sys.stdin.readline())
nlist = []
for i in range(N):
    nlist.append(list(map(int, sys.stdin.readline().split())))

# 첫 입력값 설정
x1, y1 = nlist[0][0], nlist[0][1]
result = 0.0
# 신발끈 공식
for i in range(1, N):
    x2, y2 = nlist[i][0], nlist[i][1]
    result += x1 * y2
    result -= x2 * y1
    x1, y1 = x2, y2
# 마지막 부분 처리
result += x1 * nlist[0][1]
result -= nlist[0][0] * y1
# 절대값 처리, 2로 나눔
result = abs(result)
result /= 2
# 두번째 자리에서 반올림
print(f"{result:.1f}") 