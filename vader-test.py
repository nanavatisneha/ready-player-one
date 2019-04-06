# -*- coding: utf-8 -*-


from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from io import open
analyzer = SentimentIntensityAnalyzer()

sentence = "This is an extremely awesome kickass sentence."

def sentiment_analyzer_scores(sentence):
    score = analyser.polarity_scores(sentence)
    print("{:-<40} {}".format(sentence, str(score)))
