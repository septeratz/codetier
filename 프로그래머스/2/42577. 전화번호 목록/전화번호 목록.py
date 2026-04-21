def solution(phone_book):
    phone_book.sort()
    return not any(phone_book[i+1].startswith(phone_book[i]) for i in range(len(phone_book)-1))