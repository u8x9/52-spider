html = '''
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
</div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
wrap = doc('.wrap')
wrap.find('p').remove()
print(wrap.text())
