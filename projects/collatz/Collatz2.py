#!/usr/bin/env python3

# ----------------------------
# projects/collatz/Collatz2.py
# Copyright (C) 2014
# Glenn P. Downing
# ----------------------------

# ------------
# collatz_read
# ------------

def collatz_read (r) :
    """
    read two ints
    r a reader
    return a generator of a list of two ints, representing the beginning and end of a range, [i, j]
    """
    return ([int(v) for v in s.split()] for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length in the range [i, j]
    """
    # <your code>
    return 1

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
    for a in collatz_read(r) :
        i, j = a
        v = collatz_eval(i, j)
        collatz_print(w, i, j, v)
