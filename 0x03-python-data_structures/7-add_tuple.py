#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sumA = 0
    sumB = 0
    t1 = tuple_a + (0, 0)
    t2 = tuple_b + (0, 0)

    sumA += t1[0] + t2[0]
    sumB += t1[1] + t2[1]

    return (sumA, sumB)
