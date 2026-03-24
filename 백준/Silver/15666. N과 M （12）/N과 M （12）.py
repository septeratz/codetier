import sys
N, M = map(int, sys.stdin.readline().split())
# 중복 제거를 위해 set 사용
nset = set(map(int, sys.stdin.readline().split()))
nlist = list(nset)
# 오름차순 정렬
nlist.sort()
# dfs에 쓸 배열 선언
answer = []

def dfs(start):
    # answer 배열이 끝까지 찼을 경우 출력
    if len(answer) == M:
        print(' '.join(map(str, answer)))
        return
    # nlist의 시작 부분부터 끝까지 검사. 이렇게 할 경우 크기 비교 부분이 아예 없어도 됨
    for i in range(start, len(nlist)):
        # 우선 1개 추가
        answer.append(nlist[i])
        # 이후 재귀로 탐색
        dfs(i)
        # 백트래킹(출력 마무리 후 정리)
        answer.pop()
# 탐색 시작
dfs(0)

    

    