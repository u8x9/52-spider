import re

content = '''Hello 1234567 World_This
is a Regex Demo
'''

#result = re.match('^He.*?(\d+).*?Demo$', content)
result = re.match('^He.*?(\d+).*?Demo$', content, re.S) # re.S 匹配包含换行符在内的所有
print(result.group(1))
