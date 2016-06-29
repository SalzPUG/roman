#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import *

from roman import roman, arabic

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

def test_arabic_I():
    assert_equals(arabic('I'), 1)
    
def test_roundtrip():
    assert_equals(arabic(roman(1)), 1)
    
def test_arabic_XL():
    assert_equals(arabic('XL'), 40)
    
def test_arabic_CM():
    assert_equals(arabic('CM'), 900)
    
def test_arabic_M():
    assert_equals(arabic('M'), 1000)
    
def test_arabic_MDX():
    assert_equals(arabic('MDX'), 1510)
   
def test_arabic_MCDXCIX():
    assert_equals(arabic('MCDXCIX'), 1499)
   
def test_arabic_MMIX():
    assert_equals(arabic('MMIX'), 2009)
    
def test_arabicCCCXXXVIII():
    assert_equals(arabic('CCCXXXVIII'), 338)

def test_arabicCCCLXXXVIII():
    assert_equals(arabic('CCCLXXXVIII'), 388)

def test_arabicCCCLXXXIX():
    assert_equals(arabic('CCCLXXXIX'), 389)

def test_roundtrip_49():
    assert_equals(arabic(roman(49)), 49)

def test_roundtrip_XLIX():
    assert_equals(roman(arabic('XLIX')), 'XLIX')


