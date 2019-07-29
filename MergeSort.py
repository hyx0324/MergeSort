import numpy as np


def merge(A, p, q, r):
    n1 = q - p + 1
    n2 = r - q
    L = A[p: p+n1]
    R = A[q+1: q+n2+1]

    i = 0
    j = 0

    for k in range(p, r+1):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1

            if i == len(L):
                for n in range(j, len(R)):
                    A[k+1] = R[n]
                    k += 1
                break

        else:
            A[k] = R[j]
            j += 1

            if j == len(R):
                for n in range(i, len(L)):
                    A[k+1] = L[n]
                    k += 1
                break
    return(A)


def merge_sort(A, p, r):
    if p < r:
        q = int((p+r)/2)
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)

    return(A)


a = list(np.random.randint(100, size=15))
print("Unsorted list: ")
print(a)

b = merge_sort(a, 0, len(a)-1)
print("Sorted list: ")
print(b)