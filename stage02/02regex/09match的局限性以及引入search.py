import re

content = 'Extra strings Hello 1234567 World_This is a Regex Demo Extra strings'

#result = re.match('Hello.*?(\d+).*?Demo', content)
# match 需要“全文匹配”，而不能是一部分。主要用来检测是否符合规则

result = re.search('Hello.*?(\d+).*?Demo', content)
print(result)
