from ast import Return
from asyncio import exceptions
from tkinter import EXCEPTION
from matplotlib import ticker
from pandas_datareader import data
import pandas as pd
import plotly.express as px
from pandas.tseries.offsets import Day, BDay
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta
import pandas as pd

def get_value_array(yearstoadd, start_date , df):
    bdays=BDay()
    start = start_date - relativedelta(years=yearstoadd)

    is_business_day = bdays.is_on_offset(start)

    while is_business_day != True:
            start = start + datetime.timedelta(days=1)
            is_business_day = bdays.is_on_offset(start)
    

    while 1 == 1:
        try:
            value_year = df.loc[start]

            break
        except Exception:
            start = start + datetime.timedelta(days=1)
    last_value = (df.iloc[-2])
    # print(last_value)
   
    operation = (last_value / value_year -1)

    result = round(operation * 100, 2)

    return result
    
def indice_simple_tickers(tickers, Class, Name):
    bdays=BDay()
    df = pd.read_excel (r'database/database_indice.xlsx', sheet_name=tickers[0])
    df = df.iloc[1: , :]

    fig = px.line(data_frame = df[tickers[0]]
                        ,x = df[tickers[0]]
                        ,y = [df["Unnamed: 1"]],
                        title="En points",
                        )

    fig.update_traces(line_color='#B9A049')

    fig.update_layout(
            xaxis=dict(
                showline=False,
                showgrid=False,
                title="",
                ticks='outside',
                visible= True,
                showticklabels = True,
            ),
            yaxis=dict(
                showgrid=True,
                zeroline=True,
                showline=False,
                showticklabels=True,
                ticks='outside',
                gridwidth=1,
                gridcolor='rgb(242, 242, 242)',
                linecolor='rgb(0, 0, 0)',
                linewidth= 1,
                title=None,
                tickfont=dict(
                    family='Proxima Nova',
                    size=13,
                    color='rgb(82, 82, 82)',
                    )
            ),#E5EBF7  
            showlegend = False,
            plot_bgcolor='white',
        )
    fig.data[0].line.color = 'rgb(197, 175, 92)'
    fig.data[0].line.width = 1
    first_date= df[tickers[0]].iloc[0]
    last_date = df[tickers[0]].iloc[-1]
    max_value = df["Unnamed: 1"].max() + 20


    fig.add_annotation(x=last_date + relativedelta(days=15), y=0, ax=first_date - relativedelta(days=15), ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=1, arrowcolor='black')

    fig.add_annotation(x=first_date - relativedelta(days=15), y=max_value, ax=first_date - relativedelta(days=15) , ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=1, arrowcolor='black')
    
    time_to_add_style = relativedelta(days=5)    
    time_to_add = relativedelta(years=1)    
    
    lastdate = last_date
    lastdate_tmp =  last_date - time_to_add_style
    firstdate = first_date
    firstdate_tmp = firstdate
    seconddate = firstdate + 2 * time_to_add
    thirddate = firstdate + 2 * 2 * time_to_add
    fourthdate = firstdate + 3 *2 * time_to_add
    fivthdate = firstdate + 4 * 2 * time_to_add
    sixthdate = firstdate + 5 *2 * time_to_add - relativedelta(months=4)
    month = str(firstdate)[5:7]
    day = str(firstdate)[8:10]
    year = str(firstdate)[0:4]
    monthfin = str(lastdate)[5:7]
    dayfin = str(lastdate)[8:10]
    yearfin = str(lastdate)[0:4]        # ###############LE STYLE D AFFICHAGE###########
    
    firstdate_visu = str(day) + "/" + str(month) + "/" + str(year) 
    seconddate_visu = str(day) + "/" + str(month) + "/" + str(int(year) + 2)
    thirddate_visu = str(day) + "/" + str(month) + "/" + str(int(year) + 2 * 2)
    fourthdate_visu = str(day) + "/" + str(month) + "/" + str(int(year) + 2 * 3)
    fivthdate_visu = str(day) + "/" + str(month) + "/" + str(int(year) + 2 * 4)
    sixthdate_visu = str(day) + "/" + str(month) + "/" + str(int(year) + 2 * 5 )
    lastdate_value = str(dayfin) + "/" + str(monthfin) + "/" + str(yearfin) 
    ###############LE STYLE D AFFICHAGE###########
    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [firstdate_tmp, seconddate, thirddate, fourthdate, fivthdate, sixthdate, lastdate_tmp],
                    ticktext= [firstdate_visu, seconddate_visu, thirddate_visu, fourthdate_visu, fivthdate_visu, sixthdate_visu, lastdate_value]
                    ),
    fig.write_image(Name, format="png", scale=4, engine='kaleido')


    simple_yahoo_value_arrays = [1, 3 ,5 , 10 ] # le tableau pour la boucle pour les années
    for i in Class.Yahoo:
        my_array = [] #j'initie un nouveau tableau a chaque sousjacent

        for i in simple_yahoo_value_arrays: #je fias une boucle pour parcourir les valeurs (1, 3,5 etc)
            try:
                result = get_value_array(int(i), last_date, df)
                result = ("{:.2f}".format(result))
                result = result.replace(".", ",") #joli format écrit
                result = result + "%"

                my_array.append(result)
            except Exception:
                my_array.append("N/A")
                pass
            Class.Yahoo_value.append(my_array)

    fig.show()

def indice_multiple_tickers(tickers, Class, Name):
    bdays=BDay()    
    # df = df.iloc[1: , :]
    df_list = []

    for datas in (tickers):
        # print(datas)
        df = pd.read_excel (r'database/database_indice.xlsx', datas)
        print(datas)
        df = df.iloc[1: , :]
        df_list.append(df["Unnamed: 1"])

    # print(df_list[0])
    print(df_list[0])

    # colors = ['#B9A049', '#0B3371', '#C00000', '#007A37', '#4639F3']
    df = pd.read_excel (r'database/database_indice.xlsx', sheet_name=tickers[0])
    df = df.iloc[1: , :]

    if len(df_list) == 2:
            print("yeah yeah")
            df_list[0] = df_list[0].reset_index(drop=True, inplace=True)

            fig = px.line(data_frame = df[0]
                        ,x = df[0]
                        ,y = df_list[0],
                        title="En points",
                        ) 
            print("POUET")
            # fig.data[0].name = Class.Yahoo_value_name[0]
            # fig.data[1].name = Class.Yahoo_value_name[1]

            
    #fig.show()

def indice_main(Class, Name):
        ticker = Class.TSJ
        tickers = Class.Yahoo #vraie
        if (len(tickers) == 1):
            indice_simple_tickers(ticker, Class, Name)
        
        elif (len(tickers) > 1):
            indice_multiple_tickers(ticker, Class, Name)

        else: 
            print("error")
        # print("Error sous hacent")

        for ticker in Class.Yahoo_value_name:
            Class.legende_tickers += "\n" + ticker