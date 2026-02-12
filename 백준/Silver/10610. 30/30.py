#30으로 나누어 떨어지는 수 만들기
"""
보면 숫자에서 요소별로 빼와서 그걸 왔다갔다해서 바꾸는건데
그리고 30의 배수이면 끝이 무조건 0이 되어야하는데 그럼 숫자중에 0 없으면 
-1 출력하게 하면되는거고옮기기 위해서는 각각을 어케해야 옮길수 있지?
"""
n = input()
ans = 0
if "0" not in n:
    print(-1)
else:
    for i in range(len(n)):
        ans += int(n[i])
    if ans % 3 == 0:
        arr = list(n)
        arr.sort(reverse = True)
        print(''.join(arr))
    else:
        print(-1)