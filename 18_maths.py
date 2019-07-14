import math

print("Mathematics")
print()
thingy = math.cos(math.pi/4)

print(thingy)
print(math.log(1024,2))

import random
list_items = ['apple', 'applet', 'pearl', 'bababa']
random_selection = random.choice(list_items)

print(random_selection)
sampling = random.sample(range(100), 10)# sampling without replacement
print(sampling)


print(random.random())

random.randrange(6)
print(random.randrange(6))
import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
mean_value = statistics.mean(data)

print(mean_value)

median_value = statistics.median(data)
print(median_value)

variance = statistics.variance(data)
print(variance)

average = sum(data)/len(data)

print(average)

print("Internet Access")
# Two of the simplest are urllib.request 
#1 for retrieving data from URLs

#2 smtplib for sending mail:
from urllib.request import urlopen

with urlopen('https://docs.python.org/3/library/urllib.request.html#module-urllib.request') as response:
    for line in response:
        line = line.decode('utf-8')## Decoding the binary data to text.
        if 'EST' in line or 'EDT' in line:
            print(line)

import smtplib
"""
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org'),
server.quit()

To: jcaesar@example.org
From: soothsayer@example.org
"""

print(" Dates and Times")
from datetime import date
now = date.today()
print(now)

date(2003, 12, 2)

print(date(2003, 12, 2))

print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# dates support calendar arithmetic
birthday = date(1991,4,2)
age = now-birthday
print(f"I am {age}'s old'")
days_old = age.days
print(((days_old/31)/12))

from dateutil.relativedelta import relativedelta

rdelta = relativedelta(now, birthday)
print(f"Age in years {rdelta.years}")



