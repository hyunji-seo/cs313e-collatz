#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ---------------------------


# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r a reader
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    s = r.readline()
    if s == "" :
        return []
    a = s.split()
    return [int(v) for v in a]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    ---my code---
    make a global cache
    assert range of i, j
    if i > j, swap
    Optimization - shorten the range by accounting for mapped numbers
    Find max cycle function
    Create a temporary value
    Create a counter variable to keep count of cycle length
    while n  > 1, separate n by even/ordered -- implement optimization for odd numbers
    Add to cache
    assert cycle length > 0
    Return max cycle
    """
    # <your code>

    global cache
    cache = {1:1}

    assert i > 0 and i < 1000000
    assert j > 0 and j < 1000000

    # ordered pairs
    if i > j:
        i, j = j, i

    # Optimization 2
    if i < (j//2) + 1:
        m = (j//2) + 1
    else:
        m = i

    # find max cycle length
    for n in range(m, j + 1):
        # temp = temporary value
        temp = n
        # cycle length function
        # c = cycle length
        c = 1
        while n > 1 :
            if (n % 2) == 0 :
                c += 1
                n = (n // 2)
            else:
                # Optimization 1
                c += 2
                n = n + (n//2) + 1
        # add to cache
        cache[temp] = c
        v = (temp)
    assert c > 0
    # max cycle
    return max(cache.values())




# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    while True :
        a = collatz_read(r)
        if not a :
            return
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
#!/usr/bin/env python3


# ------------------------------
# projects/collatz/RunCollatz.py
# Copyright (C) 2014
# Glenn P. Downing
# ------------------------------

# -------
# imports
# -------

import sys

# ----
# main
# ----

collatz_solve(sys.stdin, sys.stdout)

"""
% cat RunCollatz.in
1 10
100 200
201 210
900 1000



% RunCollatz.py < RunCollatz.in > RunCollatz.out



% cat RunCollatz.out
1 10 1
100 200 1
201 210 1
900 1000 1



% pydoc3 -w Collatz
"""
