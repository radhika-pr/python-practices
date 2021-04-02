#A small frog wants to get to the other side of a river. The frog is initially located on one bank of the river (position 0) and wants to get to the opposite bank (position X+1). Leaves fall from a tree onto the surface of the river.

#You are given an array A consisting of N integers representing the falling leaves. A[K] represents the position where one leaf falls at time K, measured in seconds.
#Goal is to measure earliest time frog will take to reach other side.
#eg: A[1,3,1,2,3] X=3 then A[0:3] as 1,2 and 3 The position it satisfies is index 3
def solution(X, A):
    steps = set([i for i in range(1, X + 1)])
    froggy_steps = set()

    for index, leaf in enumerate(A):
        froggy_steps.add(leaf)
        if froggy_steps == steps:
            return index
    return -1
