#You are given N counters, initially set to 0, and you have two possible operations on them:
#increase(X) − counter X is increased by 1,
#max counter − all counters are set to the maximum value of any counter.
#A non-empty array A of M integers is given. This array represents consecutive operations:
#if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
#if A[K] = N + 1 then operation K is max counter.
def solution(N, A):
    count = [0]*N
    for i in A:
        if i <= N:
            count[i-1]+=1
        else:
            count =[max(count)]*N
    return count
    pass
  
#Faster solution

def fast_solution(N, A):
    counters = [0] * N
    max_counter = 0
    last_update = 0

    for K,X in enumerate(A): 
        if 1 <= X <= N:
            counters[X-1] = max(counters[X-1], last_update)
            counters[X-1] += 1
            max_counter = max(counters[X-1], max_counter)
        elif A[K] == (N + 1):
            last_update = max_counter
        print(last_update)
    for i in range(0,N):
        counters[i] = max(counters[i], last_update)

    return counters
