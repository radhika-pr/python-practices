#Afrog is currently located at position X and wants to get to a position greater than or equal to Y. The small frog always jumps a fixed distance, D.
#Count the minimal number of jumps that the small frog must perform to reach its target.
#input X = Initial position, Y= last position D=minimal jump

def solution(X, Y, D):
    #find difference
    diff = Y-X
    if diff < 0:
        return -1
    #if reminder is 1 then need to make 1 extra step than difference/steps otherwise difference/steps
    if diff%D > 0:
        return (diff//D)+1
    else:
        return diff//D
    pass
