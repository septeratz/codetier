import sys

sudoku = []
for i in range(9):
    line = list(map(int, sys.stdin.readline().split()))
    for j in line:
        sudoku.append(j)
# 0 위치 전부 찾아서 배열에 넣음
indices = [i for i, x in enumerate(sudoku) if x == 0]
# 검사용 배열
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def dfs(n):
    # 종료 조건, 빈칸을 모두 채운 경우 출력 후 즉시 끝내도록 함
    if n == len(indices):
        for j in range(9):
            print(" ".join(map(str, sudoku[j*9:(j+1)*9])))
        sys.exit(0)

    # 이번에 탐색할 위치
    idx = indices[n]

    # 1 ~ 9 탐색
    for i in range(1, 10):
        # 그 숫자가 맞는지 확인
        if check(idx, i):
            # 맞으면 채워넣고
            sudoku[idx] = i
            # 다음 탐색
            dfs(n + 1)
            # 아니면 0으로 되돌림
            sudoku[idx] = 0

def check(idx, input_num):
    
    row = idx // 9
    col = idx %  9
    secrow = row // 3
    seccol = col // 3

    # 가로 검사
    for i1 in range(9):
        num = sudoku[row * 9 + i1]
        if num == input_num:
            return False
        
    # 세로 검사
    for i2 in range(9):
        num = sudoku[i2 * 9 + col]
        if num == input_num:
            return False
        
    # 영역 검사
    for i3 in range(9):
        num = sudoku[secrow * 27 + seccol * 3 + i3 % 3 + (i3 // 3) * 9]
        if num == input_num:
            return False
        
    # 셋 다 통과하면 True
    return True

# 탐색 시작
dfs(0)