#Given a list , find number which do not have any pair.
#Eg: given array [9,3,9,9,27,3,9,2,3] the 2s,3s and 9s have a pair but the 7 do not. Hence result is 7
def solution(A):
    n=len(A)
    #prechecks
    if n not in range(1,1000000) :
        return -1
    if not all(i in range(1,1000000) for i in A):
        return -1
    count = [i for i in A if A.count(i)%2 !=0]
    return count[0]
    pass
