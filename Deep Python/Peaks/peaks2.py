N = int(input())
A = list(map(int, input().split()))


def peak2(N, A):
    max = 0 
    
    for i in range(N):
        if A[i] > A[max]:
            max = i 
    
    return max




print(peak2(N,A))
