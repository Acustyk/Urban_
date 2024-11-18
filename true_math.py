from math import inf

def divide(first: int, second: int):
    # деление first на second с проверкой
    if second == 0 :
        return inf
    else:
        return first/second