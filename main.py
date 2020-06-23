from src.collectorTweet import *
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    newtt = tweet("#bolsonaro",100,"pt")
    newtt.feelingAnalizer(30)
