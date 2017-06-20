#!/usr/bin/env python
"""

Minimal Example
===============
Generating a square wordcloud from the US Constitution using default arguments.


Credit
=========================
Full Credit to:: Andreas Mueller
   https://github.com/amueller
   https://github.com/amueller/word_cloud/
   https://github.com/amueller/word_cloud/blob/master/examples/simple.py
"""


from os import path
from wordcloud import WordCloud

d = path.dirname(__file__)

# Read the whole text.

text = open(path.join(d, 'GTO_descriptions.txt')).read()
#with open(path, 'rb') as f:
 #   text = f.read()

# Generate a word cloud image
wordcloud = WordCloud().generate(text)

# Display the generated image:
# the matplotlib way:
import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()
