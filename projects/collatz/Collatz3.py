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
    return a generator of a pair of ints, representing the beginning and end of a range, [i, j]
    """
    return ([int(v) for v in s.split()] for s in r)

# ------------
# collatz_eval
# ------------

def collatz_eval (a) :
    """
    a an iterable of a list of two ints, representing the beginning and end of a range, [i, j]
    return a generator of a list of three ints: i, j, and the max cycle length
    """
    # <your code>
    return ([i, j, 1] for i, j in a)

# -------------
# collatz_print
# -------------

def collatz_print (a) :
    """
    return an iterable of a list of three ints: i, j, and the max cycle length
    return a generator of a string of i, j, and the max cycle length
    """
    return (str(i) + " " + str(j) + " " + str(v) + "\n" for i, j, v in a)

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in collatz_print(collatz_eval(collatz_read(r))) :
        w.write(s)
