import reprlib

#The reprlib module provides a version of repr() customized
# for abbreviated displays of large or deeply nested containers:
print("Output Formatting")
sets = set('supercalifragilisticexpialidocious')
print(reprlib.repr(sets))

import pprint
# The pprint module offers more sophisticated control over--
# printing both built-in and user defined objects-
# in a way that is readable by the interpreter.

t = [[[['black', 'cyan'], 'white',['green', 'red']], [['magenta','yellow'], 'blue']]]


print(pprint.pprint(t, width=30))

import textwrap

doc = "The wrap() method is just like fill() except that it returns a list of strings instead of one big string with newlines to separate the wrapped lines."

print(textwrap.fill(doc, width=55))
import locale
"""The locale module accesses a database of culture 
specific data formats. The grouping attribute of locale’s
 format function provides a direct way of formatting numbers with group separators:

"""

#print(locale.setlocale(locale.LC_ALL, 'English_United States.1252'))#locale.Error: unsupported locale setting

conv = locale.localeconv()

print(conv)
x = 1234567.8#locale.format_string()
print(locale.format_string("%d", x,grouping=True))

print(locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], x), grouping=True))
print(locale.format_string("%s%.*f", (conv['currency_symbol'],conv['frac_digits'], x), grouping=True))