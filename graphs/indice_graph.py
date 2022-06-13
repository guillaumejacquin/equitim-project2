from ast import Return
from asyncio import exceptions
from tkinter import EXCEPTION
from pandas_datareader import data
import pandas as pd
import plotly.express as px
from pandas.tseries.offsets import Day, BDay
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd


def indice_simple_tickers(tickers, Class, Name):
    bdays=BDay()
    df = pd.read_excel (r'../database/database_indice.xlsx', sheet_name=tickers[0])
    print (df)

def indice_multiple_tickers(tickers, Class, Name):
    pass


def indice_main(Class, Name):
    try:
        tickers = Class.Yahoo #vraie
        if (len(tickers) == 1):
            indice_simple_tickers(tickers, Class, Name)
        
        elif (len(tickers) > 1):
            indice_multiple_tickers(tickers, Class, Name)

        else: 
            print("error")
    except Exception:
        print("Error sous hacent")

    for ticker in Class.Yahoo_value_name:
        Class.legende_tickers += "\n" + ticker