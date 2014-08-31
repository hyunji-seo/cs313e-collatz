#!/usr/bin/env python3

# --------------------------------
# projects/collatz/TestCollatz3.py
# Copyright (C) 2014
# Glenn P. Downing
# --------------------------------

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz3 import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        x = tuple(collatz_read(r))
        self.assertEqual(x, ([1, 10], [100, 200], [201, 210], [900, 1000]))

    # ----
    # eval
    # ----

    def test_eval (self) :
        x = tuple(collatz_eval(([1, 10], [100, 200], [201, 210], [900, 1000])))
        self.assertEqual(x, ([1, 10, 1], [100, 200, 1], [201, 210, 1], [900, 1000, 1]))

    # -----
    # print
    # -----

    def test_print (self) :
        x = tuple(collatz_print(([1, 10, 20], [100, 200, 125], [201, 210, 89], [900, 1000, 174])))
        self.assertEqual(x, ('1 10 20\n', '100 200 125\n', '201 210 89\n', '900 1000 174\n'))

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 1\n100 200 1\n201 210 1\n900 1000 1\n")

# ----
# main
# ----

main()

"""
% coverage3 run --branch TestCollatz3.py
F..F
======================================================================
FAIL: test_eval (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz3.py", line 46, in test_eval
    self.assertEqual(x, ([1, 10, 20], [100, 200, 125], [201, 210, 89], [900, 1000, 174]))
AssertionError: Tuples differ: ([1, 10, 1], [100, 200, 1], [2... != ([1, 10, 20], [100, 200, 125],...

First differing element 0:
[1, 10, 1]
[1, 10, 20]

- ([1, 10, 1], [100, 200, 1], [201, 210, 1], [900, 1000, 1])
?          ^                             ^

+ ([1, 10, 20], [100, 200, 125], [201, 210, 89], [900, 1000, 174])
?          ^^               ++              ^^                ++


======================================================================
FAIL: test_solve (__main__.TestCollatz)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "TestCollatz3.py", line 64, in test_solve
    self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
AssertionError: '1 10 1\n100 200 1\n201 210 1\n900 1000 1\n' != '1 10 20\n100 200 125\n201 210 89\n900 1000 174\n'
- 1 10 1
?      ^
+ 1 10 20
?      ^^
- 100 200 1
+ 100 200 125
?          ++
- 201 210 1
?         ^
+ 201 210 89
?         ^^
- 900 1000 1
+ 900 1000 174
?           ++


----------------------------------------------------------------------
Ran 4 tests in 0.006s

FAILED (failures=2)



% coverage3 report -m
Name           Stmts   Miss Branch BrMiss  Cover   Missing
----------------------------------------------------------
Collatz3           9      0      8      0   100%
TestCollatz3      22      1      0      0    95%   72
----------------------------------------------------------
TOTAL             31      1      8      0    97%
"""
