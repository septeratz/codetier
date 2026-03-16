# 정규 표현 사용
import re
strin = str(input())
# '<'으로 시작하고, '>'으로 끝나며, 그 안에 어떠한 글자라도(빈 글자라고 해도) 있다면 그걸 구분자로 삼아서
# 입력받은 문자열을 분리시킴. ()로 묶은 건 그렇게 해야 구분자가 사라지지 않기 때문
tag1 = re.split(r'(<.*?>)',strin)
# tag를 제외해서 들어가야 하므로 1개 걸러 1개씩 검사
for i in range(0, len(tag1), 2):
    # tag가 연속해서 나올 경우 빈 문자열임, 그런 경우 그냥 넘어감
    if tag1[i] == '': 
        continue
    # 띄어쓰기 기준으로 나눔
    tag2 = (tag1[i].split())
    # 나눠진 부분 뒤집어서 다시 입력
    for j in range(len(tag2)):
        tag2[j] = tag2[j][::-1]
    tempstr = ' '.join(tag2)
    
    tag1[i] = tempstr
# 결과물 출력
print("".join(tag1))