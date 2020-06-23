from textblob import TextBlob
from googletrans import Translator
from unidecode import unidecode
import pandas as pd


def brantranslate(p_ptxt):
    v_textPT = unidecode(p_ptxt)
    v_texten = Translator().translate(v_textPT)
    return v_texten


def branAlyser(p_tweets):
    print("\nAnalyzing this nation's feelings ...")

    v_data = {
        "NegativePoints": 0,
        "PositivePoints": 0,
        "TotalPoints": 0,
        "UndecidedPoints": [],
        "TotalAuthors": [],
        "TotalPolarity": [],
        "TotalSource": [],
        "TotalText": [],
    }

    for i_tweet in p_tweets:

        i_textEN = brantranslate(i_tweet.text)
        i_sentiment = TextBlob(i_textEN.text)
        
        if not i_sentiment.polarity == 0:
            v_data["TotalAuthors"].append(unidecode(i_tweet.author.name))
            v_data["TotalPolarity"].append(i_sentiment.polarity)
            v_data["TotalSource"].append(i_tweet.source)
            v_data["TotalText"].append(i_tweet.text)    

    return pd.DataFrame({
        'Name': v_data["TotalAuthors"],
        'Polarity': v_data["TotalPolarity"],
        'Sent from...': v_data["TotalSource"],
        'Message': v_data["TotalText"]
    })
