#Find min difference between numbers in an array
#eg: A=[1,2,3,4,5,6]
#differences are:
#p=1  |20-1| =19
#p=2  |18-3| =15
#p=1  |15-6| =9
#p=1  |11-10| =1
#p=1  |6-15| =9
#the min differnece is 1 
def solution(A):
    n=len(A)
    print(n)
    s= sum(A)
    s1 = A[0]
    s2 = s-s1
    m =abs(s2-s1)
    print(m)
    for i in range(1,n-1):
        s1+=A[i]
        s2-=A[i]
        diff =abs(s2-s1)
        print("diff ",diff)
        if diff < m:
            m=diff
    return m
