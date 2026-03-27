# 상하좌우 탐색 후, 0과 N 사이에 있고 색깔이 같으면 추가 탐색
import sys
sys.setrecursionlimit(10**6)
N = int(sys.stdin.readline())
draw = []
# 입력
for i in range(N):
    draw.append(list(sys.stdin.readline().rstrip('\n')))
# 방문 표시
visit = [[False]*N for _ in range(N)]
# 상하좌우 탐색용
mc = [0, -1, 0, 1]
mr = [1, 0, -1, 0]
# 정답 변수
answer = 0
answer_RG = 0
# 일반 탐색
def dfs(r, c, color):
    # 먼저 방문
    visit[r][c] = True
    # 상하좌우 둘러보기
    for i in range(4):
        lr = r + mr[i]
        lc = c + mc[i]
        # 좌표가 범위 내에 있고
        if (0 <= lr < N and 0 <= lc < N):
            col = draw[lr][lc]
            # 색깔이 같으면 같은 영역이므로 추가 탐색
            if not visit[lr][lc] and col == color:
                dfs(lr, lc, col)
# 모든 좌표 둘러보면서 visit이 있는 경우에만 +1
# 함수를 한 번 실행할 때마다 같은 영역까지만 탐색하므로 상관없음
for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            dfs(i, j, draw[i][j])
            answer += 1

#적록색맹 탐색 이전 R과 G 동일하게 변경, visit 다시 초기화
for i in range(N):
    for j in range(N):
        if draw[i][j] == 'G':
            draw[i][j] = 'R'
visit = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if not visit[i][j]:
            dfs(i, j, draw[i][j])
            answer_RG += 1

print(answer, answer_RG)