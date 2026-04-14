# 첫 입력을 기준으로 삼아야 하므로 pivot 배열 사용, 그걸 기준으로 삼음
# 이후 다음 입력에서 pivot 기준으로 game 이중 배열에 투입
# pivot 기준 내라면 그 index의 배열에 넣고, 기준 외라면 다음 pivot으로 검사, 그렇게 계속 검사해서
# pivot 끝까지 갔는데도 안 나오면 새로운 pivot 사용
import sys
P, M = map(int, sys.stdin.readline().split())
game = []
pivot = []
for i in range(P):
    level, name = sys.stdin.readline().split()
    level = int(level)
    # 놓은 거 체크용
    placed = False
    for k, j in enumerate(pivot):
        if j - 10 <= level <= j + 10 and len(game[k]) < M:
            game[k].append((name, level))
            placed = True
            break
    # 안 놓여졌으면 새로 놓음
    if not placed:
        pivot.append(level)
        game.append([(name, level)])
# 출력
for i in game:
    # name 기준 정렬
    i.sort(key = lambda x: x[0])
    # 다 채워지면 started
    if len(i) == M:
        print("Started!")
        for n, l in i:
            print(f"{l} {n}")
    # 아니면 waiting
    else:
        print("Waiting!")
        for n, l in i:
            print(f"{l} {n}")