from textblob import TextBlob

text = TextBlob("Beautiful is better than ugly." "Explicit is better than implicit.")

# print(text.words)
# print(text.tags)
# print(text.sentences)

for sentence in text.sentences:
         print(sentence.sentiment)

 
