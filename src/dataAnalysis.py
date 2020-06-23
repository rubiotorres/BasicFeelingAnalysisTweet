import pandas as pd
import numpy as np
from textblob import TextBlob
from unidecode import unidecode
import matplotlib.pyplot as plt
from googletrans import Translator


def getAverage(p_data):
    return p_data['Polarity'].mean()

def getPositive(p_data):
    p_data.query('Polarity > 0').to_csv('./out/out.csv')
    p_data.query('Polarity > 0').plot(kind='bar',x='Name',y='Polarity')
    plt.savefig('./out/Positive.png')
    return {
        'Amount': p_data.query('Polarity > 0').shape[0],
        'Max': p_data.query('Polarity > 0')['Polarity'].max(),
        'Min': p_data.query('Polarity > 0')['Polarity'].min(),
        'Average': p_data.query('Polarity > 0')['Polarity'].mean()
    }

def getNegative(p_data):
    p_data.query('Polarity < 0').to_csv('./out/out.csv')
    p_data.query('Polarity < 0').plot(kind='bar',x='Name',y='Polarity')
    plt.savefig('./out/Negative.png')
    return {
        'Amount': p_data.query('Polarity < 0').shape[0],
        'Max': p_data.query('Polarity < 0')['Polarity'].max(),
        'Min': p_data.query('Polarity < 0')['Polarity'].min(),
        'Average': p_data.query('Polarity < 0')['Polarity'].mean()
    }

def dataAnalysis(p_data):
    print("Analyzing the data, please wait ...")
    v_average = getAverage(p_data)
    p_data.to_csv('./out/out.csv')
    p_data.plot(kind='bar',x='Name',y='Polarity')
    print("Printing general data")
    plt.savefig('./out/general.png')
    print(f"\n{p_data.shape[0]} analyzed data.\nWith the average {v_average}, we see that twitter " 
    + ("are supporting"if v_average > 0 else "are hating") 
    + " the situation of this research.")
    print("Positive numbers : ") 
    print(getPositive(p_data))
    print("Negative Number: ")
    print(getNegative(p_data))

    

