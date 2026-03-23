
# 굳이.. 구우우지.. DP를 써버린 풀이임.. 그냥 DFS 탐색 쓰면 금방 풀림..
# M개의 비트에 상태들을 저장하고, lsh를 이용해서 그 비트 상태를 확인해서 놓을 수 있는지 확인하는 것이 핵심
import sys

N, M = map(int, sys.stdin.readline().split())

# 가로가 더 길면 2^(M+1)만큼 루프를 도는 코드 특성상 타임아웃 가능성 존재, 짧은 쪽으로 변경
if (N < M): N, M = M, N

total = N * M
max_mask = 1 << (M + 1)
dp = [0] * max_mask
# 일단 하나 체크
dp[0] = 1


for i in range(total):
    # 효율적 관리를 위해 DP 새로 저장
    next_dp = [0] * max_mask
    r = i // M
    c = i % M
    for mask in range(max_mask):
        if dp[mask] == 0:
            continue
        # 현재 칸에 넴모를 놓지 않는 경우 과거 기록을 왼쪽으로 1칸 밀고 새 자리는 0으로 둠
        new_mask_0 = (mask << 1) & (max_mask - 1)
        next_dp[new_mask_0] += dp[mask]
        
        # 현재 칸에 넴모를 놓을 수 있는지 검사하는 용도
        can_place = True
        
        # 2x2 사각형이 만들어지는지 검사 (맨 윗줄이나 맨 왼쪽이면 아예 안 되니깐 스킵)
        if r > 0 and c > 0:
            # 왼쪽(0번), 위(M-1번), 왼쪽위(M번) 비트가 모두 1인지 확인
            if (mask & 1) and (mask & (1 << (M - 1))) and (mask & (1 << M)):
                can_place = False
                
        # 놓을 수 있다면
        if can_place:
            # 과거 기록을 왼쪽으로 1칸 밀고, 현재 자리에 1을 놓음
            new_mask_1 = ((mask << 1) | 1) & (max_mask - 1)
            next_dp[new_mask_1] += dp[mask]
            
    # 다음 칸으로 넘어가기 위해 dp 덮어쓰기
    dp = next_dp

# 마지막 칸까지 다 채운 후, 가능한 모든 상태의 가짓수를 더함
print(sum(dp))