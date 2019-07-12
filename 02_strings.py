quote = 'sperm eggs'# single quotes

quote2 = 'doesn\'t'

print(f"sing quote {quote}, escape character {quote2}.")
quote3 = '"Yes," they said.'
quote4 = "\Yes,\" they said."
quote5 = '"Isn\'t," they said.'

print(f"{quote3}, {quote4}, {quote5}")

nextline = 'First line. \nSecond line.'
print(nextline)

repit = 3 * 'zu' + 'kile'
print(repit)
# string close next to each other automatically concatenate

conc = 'Zukile' 'Mtotso'
#this feature is useful when you wan to join strings
print(conc)

text = ('Put several parenthesis' 'to add other thing.')
print(text)

# can concatenate two string variables
#indexing a string
word = 'Python'
print(f"Getting first character of string {word[0]}")
#indexing maybe negative
#backwwarding indexing does not start from 0 or -0 since its zero
print(f"-1 index get the last position 0 of the string , {word[-1]}")
print(f"-2 index get the lsecond ast position 1 of the string , {word[-2]}")

#slicing
print(f"Slicing word[0:2] {word[0:2]}")
#the start is always included, and the end always excluded

#to make sure that s[:i] + s[i:] is always equal to s:
print(word[:2])# # character from the beginning to position 2 (excluded)
print(word[4:])#characters from position 4 (included) to the end
print(word[-2:])#characters from the second-last (included) to the end
s = 'J' + word[1:]
print(s)
s2 = word[:2] + 'py'
print(s2)
s3 = 'abcdefghijklnmopqrstuvwxyz'
print(f"The length of string i len(string) {len(s3)}")