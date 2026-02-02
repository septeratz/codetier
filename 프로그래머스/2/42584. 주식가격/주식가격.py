def solution(prices):
    
    # 정답 배열 밑작업
    n = len(prices)
    answer = [0] * n
    
    # 배열 순차 탐색, 탐색할 때 사용할 스택과 숫자 
    stack = []
    for i in range(n):
        
        # stack이 비어있지 않고, 가격이 떨어진 경우
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top
        
        # stack에 가격 index 추가
        stack.append(i)
        
    # 마지막까지 안 떨어진 가격 처리
    while stack:
        top = stack.pop()
        answer[top] = (n-1) - top
        
            
    return answer