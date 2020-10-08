import re

c1 = '2019-12-15 12:00'
c2 = '2019-12-17 12:55'
c3 = '2019-12-22 13:21'

pattern = re.compile('\d{2}:\d{2}')
r1 = re.sub(pattern, '', c1)
r2 = re.sub(pattern, '', c2)
r3 = re.sub(pattern, '', c3)

print(r1, r2, r3)
