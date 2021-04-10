#A DNA sequence can be represented as a string consisting of the letters A, C, G and T with weightage 1,2,3,4 resp.
#Find min value in a given range where lower range represented in array P and upper range represented in array Q
#eg: DNA sequence S = "CAGCCTA" P = [2,5,0] Q=[4,5,6] Find an array such that
# Result array finds min of DNA sequence between positions P[K] and Q[K] eg: P[0]=2 Q[0]=4 min between S[0:5] = 2 (includes G and C in which C hs min value)

def solution(S, P, Q):
    M= len(P)
    add = [0]*(M)
    for m in range(M):
        u=Q[m]+1
        if 'A' in S[P[m]:u]:
            add[m]+=1
        elif 'C' in S[P[m]:u]:
            add[m]+=2
        elif 'G' in S[P[m]:u]:
            add[m]+=3
        elif 'T' in S[P[m]:u]:
            add[m]+=4
    return add
