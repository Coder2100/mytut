import os
print("10.1. Operating System Interface")
os.getcwd()

print(f"The current directory is {os.getcwd()}")

print(dir(os))

import shutil
shutil_library = shutil.copyfile('data.db', 'archive.db')

print(shutil_library)

#move_files = shutil.move('/built/executables', 'installdir')

print("10.2. File Wildcards")
import glob
tut_files = list(glob.glob('*.py'))
total_files = len(tut_files)

print(glob.glob('*.py'))
print(f"There {total_files} python files on this tutorial")

print("10.3. Command Line Arguments¶")

import sys
print(f"Displays current file{sys.argv}")

print("Error Output Redirection and Program Termination")

print(sys.stderr.write('Warning, log file not found starting a new one\n'))

print("The most direct way to terminate a script is to use sys.exit()")

print("10.5. String Pattern Matching...RegEx")

import re
find_all = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(find_all)
#print((re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')))

sub_search = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(sub_search)

replace_string = 'Sanuse Mtotso'.replace('Sabelo', 'Ntobeko')
print(f"Young and seniors {replace_string}")

