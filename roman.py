#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

numerals = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}

def roman(number):
    result = ""
    if number == 0:
        return result
    while(number > 0):
        for key in sorted(numerals, reverse=True):
            if number >= key:
                x = int(math.floor(number / key))
                if x == 4 or x == 90:
                    result += specials[key * x]
                else:
                    result = result + x * numerals[key]
                number = number - key * x
    return result

if __name__ == "__main__":
    import nose
    nose.main()
