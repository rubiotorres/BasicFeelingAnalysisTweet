from textblob import TextBlob
from googletrans import Translator
from unidecode import unidecode

def branAlyser(p_tweets):
    v_numPos = 0
    v_numNeg = 0
    v_total = 0

    for i_tweet in p_tweets:
        i_textPT = unidecode(i_tweet.text)
        i_textEN = Translator().translate(i_textPT)
        i_sentiment = TextBlob(i_textEN.text)
        v_total += 1
        if i_sentiment.polarity > 0: 
            v_numPos += 1 
        elif i_sentiment.polarity < 0: 
            v_numNeg += 1

    v_mediaPos = v_numPos/v_total
    v_mediaNeg = v_numNeg/v_total
    print('Percentage of positive comments: '+str(v_mediaPos))
    print('Percentage of negative comments: '+str(v_mediaNeg))
    print('Total of comments: '+str(v_mediaNeg + v_mediaPos))
