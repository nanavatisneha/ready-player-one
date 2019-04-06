from bs4 import BeautifulSoup
from textblob import TextBlob
import requests
import re
import random

text()

def url_to_string(url):
    res = requests.get(url)
    html = res.text
    soup = BeautifulSoup(html, 'html5lib')
    for script in soup(["script", "style", 'aside']):
        script.extract()
    return " ".join(re.split(r'[\n\t]+', soup.get_text()))
jose = url_to_string('http://www.espn.com/espn/feature/story/_/id/25145480/jose-mourinho-last-stand')
# article = nlp(jose)
article = TextBlob(jose)

# # // ner detection for the article
# for ent in article.ents:
#     print(ent.text, ent.label_)

# # // sentence spliting and polarity detection
# for sentence in article.sentences:
#          print(sentence.sentiment)

nouns = list()
for word, tag in article.tags:
    if tag == 'NN': nouns.append(word.lemmatize())
print("This text is about...")
for item in random.sample(nouns,10):
    word = text(item)
    print(word.pluralize)
