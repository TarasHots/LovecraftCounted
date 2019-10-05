import requests
import operator
from lxml import html

url = 'http://www.hplovecraft.com/writings/texts/fiction/og.aspx'

# page = requests.get(url)
# tree = html.fromstring(page.content)
#
# text = tree.xpath("//div[@align='justify']")[1]

text = 'Atop the tallest of earth’s peaks dwell the gods of earth, and suffer no man to tell that he hath looked ' \
       'upon them. Lesser peaks they once inhabited; but ever the men from the plains would scale the slopes of rock ' \
       'and snow, driving the gods to higher and higher mountains till now only the last remains. When they left' \
       ' their older peaks they took with them all signs of themselves; save once, it is said, when they left' \
       ' a carven image on the face of the mountain which they called Ngranek.'

# 1.Remove non alphanumerical characters. Keep spaces only

alpha_text = text.replace('—', '').replace('()', '').replace('.', '').replace(',', '').replace(';', '')

# 2.Count words

counts = {}

for word in alpha_text.split(' '):
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

sorted_words = sorted(counts.items(), key=operator.itemgetter(1), reverse=bool('true'))

print(sorted_words)
