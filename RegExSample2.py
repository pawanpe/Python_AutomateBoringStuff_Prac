import re

n = re.compile(r'this \w+')
print(n.findall('this string becomes that string'))

print(n.sub('one', 'this string becomes tht string')) # substitute

re.compile(r''' # divide the pattern in multiple lines
\d\d\d
-
\d\d\d
-
\d\d\d\d''', re.VERBOSE | re.IGNORECASE) # re.IGNORECASE, re.DOTALL, re.VERBOSE