#An array A consisting of N different integers is given. 
#The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.
#Find the missing element
def solution(A):
    N=len(A)
    #sum of n+1 integers
    s = int(((N+1)*(N+2))/2)
    #sum of integers in list
    m = sum(A)
    #difference gives missing number
    missing = s-m
    return missing
    pass
