#!/usr/bin/python3
""" Minimum Operations """


def minOperations(n):
    """ method that calculates the fewest number of operations needed
        @param n:
        @return:
    """
    if n <= 1:
        return 0

    operations = [0] * (n + 1)

    for i in range(2, n + 1):
        operations[i] = float('inf')  # Initialize with a large value
        for j in range(1, i):
            if i % j == 0:
                operations[i] = min(operations[i], operations[j] + i // j)

    return operations[n]
