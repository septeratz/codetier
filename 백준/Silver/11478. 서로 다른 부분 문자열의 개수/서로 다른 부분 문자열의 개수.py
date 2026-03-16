# set 활용, 중복 제거는 set가 해주니깐 1개, 2개, ... , n개로 나누는 부분만 구현
istr = str(input()).split()[0]
inset = set()
# 1, 2, 3, ... 개 단위 계산
for i in range(1, len(istr) + 1):
    # 실질적으로 나누는 부분, index에 안 걸리게 i-1 계산해서 넣음
    for j in range(len(istr) - (i-1)):
        inset.add(istr[j:j+i])

print(len(inset))