the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall")

print('simple calculator')
#assignemnt operator '='
spam = 1
text = "#  This is not a comments."
two = 2+2
fifty = 50 - 5*6
brkets = (50- 5*6)/4
#division
eight = 8/5
#floor division
eight2 = 8//5
eight3 = 17%3
eight4 = 5 * 3 + 2
eight5 = 5 **2 #squred
#to the power
eight6 = 2 **7

print(spam)
print(text)
print(two)
print(fifty)
print(brkets)
print(eight)
print(f"Classic division / returns a float 8/5 is equal {eight}.")
print(f"Floor division discards the fractional part 8//5 is equal {eight2}.")
print(f"The % operator returns the remainder of the division 17%3 equals {eight3}.")
print(f"Result * divisor + remainder, {eight4}.")
print(f"5 squared written as 5**2 equals {eight5}.")
print(f"2 to the power of 7 written as 2 **7 answer {eight6}.")

width = 20
height = 5 * 9

bi = width * height

print(f"The (20)width * (5*9)height equals {bi}.")

#
"""when you are using Python as a desk calculator,
 it is somewhat easier to continue calculations"""

tax = 12.5 / 100
price = 100.50
tax_amount = price * tax
print(f"Tax is {tax}, price{price}, Tax Amount {tax_amount}, Rounded tax amount into 2 digit is {round(tax_amount, 2)}")