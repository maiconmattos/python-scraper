from wikipedia import Wikipedia
from wiki2plain import Wiki2Plain

lang = 'simple'
wiki = Wikipedia(lang)

try:
    raw = wiki.article('James_Joyce')
except:
    raw = None

if raw:
    wiki2plain = Wiki2Plain(raw)
    content = wiki2plain.text

print(wiki)
print('=======================')
print(raw)
print('=======================')

print(content)    