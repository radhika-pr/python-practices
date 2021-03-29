#Find max number of zeroes in between 2 ones in binary representation of a given number
#eg: 1162 has bin representation 10010001010 has 00,000 and 00 in between 1s. The max number of zeroes in that is 3
def solution(N):
    A=[i for i in bin(N).split('b')[1].split('1')]
    if A[-1]:
        del A[-1]
    B= [i for i in A if i]
    if not B:
        return 0
    max =0
    for j in range(0,len(B)):
        s=B[j]
        if max < len(s):
            max = len(s)
        j+=1
    return max
    pass
