# 초기 코드가 타임아웃으로 인해 실패. 재귀를 없애는 형식으로 다시 짬

def n_queens(row):
    global result
    # 종료 조건 - 마지막 row까지 도달
    if row == N:
        result += 1
        
        return
    
    for col in range(N):
        # row행에 있는 퀸이, col이랑 겹치거나, 0부터 row-1행까지의 퀸들과 같은 열이거나, 대각선에 있는지 확인
        if (check_col[col] or check_right[col + row] or check_left[row - col + N - 1]):
            # 겹치면 다음 col로 넘어감
            continue
        # 방문 표시
        check_col[col] = True
        check_left[row - col + N - 1] = True # 왼쪽 대각선 체크
        check_right[col + row] = True # 오른쪽 대각선 체크
        # 다음 행 검사
        n_queens(row + 1)
        # 백트래킹 시 사용하도록 다시 초기화
        check_col[col] = False
        check_left[row - col + N - 1] = False
        check_right[col + row] = False

    
# 입력받기
N = int(input())
# 하나만 있는 경우 그냥 1개만 놓아도 되니깐 따로 처리
if N==1: 
    print(1)
    exit()
# 결과에 쓸 배열과 변수 선언
check_col = [False]*N
check_left = [False]*(N*2 - 1)
check_right = [False]*(N*2 - 1)
result = 0
# 시작
n_queens(0)
# 결과 출력
print(result)