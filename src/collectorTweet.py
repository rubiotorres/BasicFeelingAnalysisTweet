from datetime import datetime, timedelta
import tweepy
from src.UsrGlobal.UserGlobal import *
from src.feelingAnalysis import *
from src.dataAnalysis import *


class tweet():
    def __init__(self, 
                p_q,
                p_itens = 100,
                p_lang = "pt"):
        self.p_itens = p_itens
        self.p_lang = p_lang
        self.p_q = p_q

    @property
    def searchwords(self):
        return self._p_q

    @searchwords.setter
    def searchparam(self,param):
        if(str(param)<=0):
            raise ValueError("Error: Parameters are required")
        self._p_q = param

    def search(self,numberDays):
        date = ((datetime.today()- timedelta(days = numberDays)).strftime("%Y-%m-%d"))
        print(f"\nLooking for {self.p_itens} twitters about the word {self.p_q}, {numberDays} days ago, wait ...")
        auth = tweepy.OAuthHandler(Consumer_key, Consumer_key_secret)
        auth.set_access_token(Access_token, Access_token_secret)
        api = tweepy.API(auth,wait_on_rate_limit=True)
        return tweepy.Cursor(api.search,q=self.p_q, since = date,lang=self.p_lang).items(self.p_itens)
    
    def feelingAnalizer(self, numberDays):
        if self.p_lang == "pt":
            dataAnalysis(branAlyser(self.search(numberDays)))