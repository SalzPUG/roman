#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    while(number > 0):
        for key in sorted(numerals, reverse=True):
            if number >= key:
                x = number // key
                result = result + x * numerals[key]
                number = number - key * x
    return result

def arabic(roman):
    inverse = {v:k for k, v in numerals.items()}
    
    result = 0
    
    while roman:
        twos = roman[:2]
        
        if twos in inverse:
            result += inverse[twos]
            roman = roman[2:]
        else: 
            result += inverse[roman[0]]
            roman = roman[1:]
            
    return result
            
            
if __name__ == "__main__":
    import nose
    nose.main()
