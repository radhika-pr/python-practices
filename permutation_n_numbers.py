#draft
def solution(A):
    B=list(set(A))
    N= len(B)
    s =N*(N+1)//2
    add =sum(B)
    if s==add:
        return 1
    else:
        return 0     
    pass
