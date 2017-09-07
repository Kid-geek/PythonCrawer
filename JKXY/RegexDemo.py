import re

str='abcdef'
a=re.search('abc(.*?)f',str)
print(a.group(0))
