def solution(A, B, K):
    c1 = B//K
    c2 = A//K
    count = c1-c2
    if A%K==0:
        count+=1
    return count
