#!/usr/bin/env python3

# -------------
# UnitTests2.py
# -------------

# https://docs.python.org/3.4/library/unittest.html

from unittest import TestCase, TestLoader, TestSuite, TextTestRunner

def cycle_length (n) :
    assert n > 0
    c = 0
    while n > 1 :
        if (n % 2) == 0 :
            n = (n // 2)
        else :
            n = (3 * n) + 1
        c += 1
    assert c > 0
    return c

class UnitTests (TestCase) :
    def test_1 (self) :
        self.assertEqual(cycle_length( 1), 1)

    def test_2 (self) :
        self.assertEqual(cycle_length( 5), 6)

    def test_3 (self) :
        self.assertEqual(cycle_length(10), 7)

s = TestSuite()
s.addTest(TestLoader().loadTestsFromTestCase(UnitTests))
TextTestRunner().run(s)

"""
FFF
======================================================================
FAIL: test_1 (__main__.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests2.py", line 25, in test_1
    self.assertEqual(cycle_length( 1), 1)
  File "./UnitTests2.py", line 20, in cycle_length
    assert c > 0
AssertionError

======================================================================
FAIL: test_2 (__main__.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests2.py", line 28, in test_2
    self.assertEqual(cycle_length( 5), 6)
AssertionError: 5 != 6

======================================================================
FAIL: test_3 (__main__.UnitTests)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "./UnitTests2.py", line 31, in test_3
    self.assertEqual(cycle_length(10), 7)
AssertionError: 6 != 7

----------------------------------------------------------------------
Ran 3 tests in 0.000s

FAILED (failures=3)
"""
