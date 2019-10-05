import requests
import collections
from lxml import html

url = 'http://www.hplovecraft.com/writings/texts/fiction/og.aspx'

page = requests.get(url)
tree = html.fromstring(page.content)

# Contains div with text mixed with tags

main_text = tree.xpath("//div[@align='justify']")[1]

actually_text = main_text.text

for child in main_text.getchildren():
    if child.tag == 'br':
        continue
    elif child.tag == 'img':
        actually_text += ' ' + child.tail
    elif child.tag == 'i':
        actually_text += ' ' + child.text

# Clean a bit

text = actually_text.strip().replace('\r\n', ' ')

# 1.Remove non alphanumerical characters. Keep spaces only

alpha_text = text.replace('—', '').replace('()', '').replace('.', '').replace(',', '').replace(';', '').split(' ')

# 2.Count words

counter = collections.Counter(alpha_text)

print(counter.most_common(10))
