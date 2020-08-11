import random
# open dictionary (370104 lines) (9 in fox)
raw = open('fox.txt') # will replace with 'words_alpha'
for data in raw:
    data = data.lower()
    data = data.split()

cdata = data

words = random.sample(cdata, k=3)
num1 = random.randint(0, 1000)
num1 = str(num1)


def nstring(input, seperator):
    final = seperator.join(input)
    return final

seperator = '-'
pstring = nstring(words, seperator)
pstring = pstring.title()
#(pstring, num1)

pstring = str(pstring)
password = pstring + num1
password = password.strip()
print(password)
