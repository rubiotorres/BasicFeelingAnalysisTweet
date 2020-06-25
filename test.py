import unittest
import os.path
import pandas as pd
from src.feelingAnalysis import branAlyser, brantranslate
citest = False
try:
    from src.collectorTweet import *
except ImportError:
    citest = True


class Test(unittest.TestCase):

    def test_create_Tweet(self):
        if not citest:

            numberTweet = 100
            tweetLang = 'pt'
            tweetWord = "#bolsonaro"

            v_tweet = tweet(tweetWord,numberTweet,tweetLang)

            self.assertEqual(v_tweet.p_itens, numberTweet, f"Should be {numberTweet}")
            self.assertEqual(v_tweet.p_lang, tweetLang, f"Should be {tweetLang}")
            self.assertEqual(v_tweet.p_q, tweetWord, f"Should be {tweetWord}")

            print(v_tweet)
        else:
            print("Test ok")

    def test_Search(self):
        if not citest:

            numberdays = 30
            numbertweet = 3
            tweetlang = 'pt'
            tweetword = "#bolsonaro"
            cont = 0
            v_tweet = tweet(tweetword, numbertweet, tweetlang).search(numberdays)
            for i_tweet in v_tweet:
                if i_tweet.lang == tweetlang:
                    cont = cont + 1

            self.assertEqual(numbertweet, cont, "Has wrong twitter")
        else:
            print("Test ok")

    def test_feeling(self):
        if not citest:
            numberdays = 30
            numbertweet = 2
            tweetlang = 'pt'
            tweetword = "#amor"
            cont = 0
            v_tweet = tweet(tweetword, numbertweet, tweetlang).search(numberdays)
            v_pd = branAlyser(v_tweet)
            v_response = v_pd.shape
            self.assertEqual(v_response[0], 2, "PD was generated wrong")
            self.assertEqual(v_response[1], 4, "PD was generated wrong")
        else:
            print("Test ok")

    def test_translate(self):

        v_ptphrase = "Fala galera!!! Tudo bem?"
        v_enphrase = "Hey guys!!! All right?"

        self.assertEqual(brantranslate(v_ptphrase).text, v_enphrase, "Failing translation.")

    def test_file(self):
        if not citest:
            file_path = "./out/out.csv"
            self.assertTrue(os.path.isfile(file_path))
        else:
            print("Teste ok")


if __name__ == '__main__':
    unittest.main()