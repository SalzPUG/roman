#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from roman import roman

def test_roman_1():
    assert_equals(roman(1), 'I')
    
def test_roman_5():
    assert_equals(roman(5), 'V')

def test_roman_10():
    assert_equals(roman(10), 'X')
    
def test_roman_50():
    assert_equals(roman(50), 'L')
    
def test_roman_110():
    assert_equals(roman(110), 'CX')
    
def test_roman_0():
    assert_equals(roman(0), "")
    
def test_roman_1510():
    assert_equals(roman(1510), "MDX")
    
def test_roman_4():
    assert_equals(roman(4), "IV")
    
def test_roman_9():
    assert_equals(roman(9), "IX")
    
def test_roman_44():
    assert_equals(roman(44), 'XLIV')
    
def test_roman_99():
    assert_equals(roman(99), 'XCIX')

def test_roman_49():
    assert_equals(roman(49), 'XLIX')

def test_roman_34():
    assert_equals(roman(34), 'XXXIV')

def test_roman_39():
    assert_equals(roman(39), 'XXXIX')
    
def test_roman_1999():
    assert_equals(roman(1999), 'MCMXCIX')

def test_roman_1499():
    assert_equals(roman(1499), 'MCDXCIX')



