import math

def erastothene_sieve(n):
    """ Print n-first prime numbers """
    A = [True] * n
    A[0] = A[1] = False
    for i, elem in enumerate(A):
        if elem:
            print(i)
            for j in range(i * i, n, i):
                A[j] = False


def erastothene_sieve_gen():
    init_list = [2, 3]
    while True:
        for i in range(init_list[0], init_list[-1] ** 2):
            if all(i % elem for elem in init_list):
                init_list.append(i)
                yield i

