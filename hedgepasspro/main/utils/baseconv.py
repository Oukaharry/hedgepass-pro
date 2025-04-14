# main/utils/baseconv.py
"""
Base converter taken from Django 3.2 (removed in Django 4.0+)
"""
import math

class BaseConverter:
    decimal_digits = '0123456789'
    
    def __init__(self, digits):
        self.digits = digits
    
    def encode(self, i):
        if i < 0:
            raise ValueError("Negative base not allowed")
        if i == 0:
            return self.digits[0]
        base = len(self.digits)
        digits = []
        while i:
            digits.append(self.digits[i % base])
            i = i // base
        return ''.join(reversed(digits))
    
    def decode(self, s):
        base = len(self.digits)
        return sum(
            self.digits.index(digit) * (base ** idx)
            for idx, digit in enumerate(reversed(s.upper())))