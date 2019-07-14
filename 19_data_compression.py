import zlib
print("Data Compression")
s = b'abcdefghigklnmnopqrstuvwxyz'
print(len(s))
t = zlib.compress(s)
print(len(t))
print(zlib.decompress(t))

print(zlib.crc32(s))

print("Performance Measurement")

from timeit import Timer

print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())

print(Timer('a,b = b,a', 'a=1; b=2').timeit())

print("Quality Control")

def average(values):
    #Computes the arithmetic mean of a list of numbers.
    #print(average([20, 30, 70]))
    return sum(values)/len(values)
import doctest
doctest.testmod()
print(doctest.testmod())

import unittest

class TestStasFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20,30,70]), 40.0)
        self.assertEqual(round(average([1,5,7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20,30,70)
unittest.main()## Calling from the command line invokes all tests# Calling from the command line invokes all tests