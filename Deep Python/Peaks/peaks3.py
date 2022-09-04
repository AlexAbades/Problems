j = int(input())
A = list(map(int, input().split()))
i = 0 


def peak3(A, i, j):
    m = int((i+j)/2)

    if m == i:
        if A[m] >= A[m-1]:
            return m 
    elif m == j:
        if A[m] >= A[m+1]:
            return m 
    if A[m] >= A[m-1] and A[m] >= A[m+1]:
        return m
    elif A[m-1] > A[m]:
        return peak3(A, i, m-1)
    elif A[m] < A[m+1]:
        return peak3(A, m+1, j)




print(peak3(A, i, j))