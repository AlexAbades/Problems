N = int(input())
A = list(map(int, input().split()))


def peak1(N, A):
    if A[0] >= A[1]:
        return 0
    for i in range(1, N-2):
        if A[i-1] <= A[i] and A[i] >= A[i+1]:
            return i
    if A[N-2] <= A[N-1]:
        return N-1


print(peak1(N,A))