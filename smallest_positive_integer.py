#Given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#Eg: given A = [1, 3, 6, 4, 1, 2], the function should return 5.
def solution(A):
    B = list(set(A))
    if 1 not in B:
        return 1
    C = [i for i in B if i>0]
    C.sort()
    for i in range(0,len(C)):
        if C[i] != i+1:
            return i+1
    return i+2
    pass
