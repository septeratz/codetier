def solution(phone_book):
    # 정렬하면 어차피 오름차순으로, 사전순으로 정렬되므로
    # 바로 뒷쪽이랑만 검사하면 됨 
    k = phone_book
    k.sort()
    for i in range(len(k) - 1):
        if k[i+1].startswith(k[i]): return False
    return True