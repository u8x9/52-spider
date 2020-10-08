import re

content = '(谷歌) www.google.com'
result = re.match('\(谷歌\) www\.google\.com', content)
print(result)
