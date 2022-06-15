
from tkinter import EXCEPTION
from pandas_datareader import data
import pandas as pd
import plotly.express as px
from pandas.tseries.offsets import Day, BDay
from datetime import date
import datetime
from dateutil.relativedelta import relativedelta

def bloc4(Class, Name):
    try:
        tickers = ['ALO.PA'] #Exemple de test
        #recuper les tickers de la base de donnée
        tickers = ['WFC', 'RNO.PA', '^GSPC'] #exemple de test
        ###ici####
        tickers = Class.Yahoo #vraie
        if (len(tickers) == 1):
            bloc4_simple_tickers(tickers, Class, Name)
        
        elif (len(tickers) > 1):
            bloc4_multiple_tickers(tickers, Class, Name)

        else: 
            print("error")
    except Exception:
        print("Error sous hacent")

    for ticker in Class.Yahoo_value_name:
        Class.legende_tickers += "\n" + ticker


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


def bloc4_simple_tickers(tickers, Class, Name):
    bdays=BDay()
    
    end_date = Class.DPCI
    
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    end_date = end_date - datetime.timedelta(days=1)
    is_business_day = bdays.is_on_offset(end_date)

    try:
        while is_business_day != True:
            end_date = end_date - datetime.timedelta(days=1)
            is_business_day = bdays.is_on_offset(end_date)
        #end_date/startdate -1
        start_date = end_date - relativedelta(days=1)
        start_date = end_date - relativedelta(years=12)
        is_business_day = bdays.is_on_offset(start_date)
        while is_business_day != True:
            start_date = start_date + datetime.timedelta(days=1)
            is_business_day = bdays.is_on_offset(start_date)
      
        # User pandas_reader.data.DataReader to load the desired data. As simple as that.
        panel_data = data.DataReader(tickers[0], 'yahoo', start_date, end_date)
        #ADj close,

        adj_close = panel_data["Adj Close"]
        adj_close.columns = ['Adj Close']

        max_value = adj_close.max() + 20

        fig = px.line(data_frame = adj_close.index
                        ,x = adj_close.index
                        ,y = [adj_close],
                        title="EUR"
                        )
        fig.update_traces(line_color='#B9A049')

        fig.update_layout(
            xaxis=dict(
                showline=False,
                showgrid=True,
                linecolor='rgb(0, 0, 0)',
                linewidth= 1,
                ticks='inside',
                visible= True,
                showticklabels = True,
                title=None,
                tickfont=dict(
                    family='Proxima Nova',
                    size=12,
                    color='rgb(82, 82, 82)',   
                ),
            ),
            yaxis=dict(
                showgrid=True,
                zeroline=True,
                showline=False,
                showticklabels=True,
                ticks='inside',
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
            title=dict(
                x=0.09,
                y=0.85,
                font=dict(
                    family="Arial",
                    size=10,
                    color='#000000'
                )
            ),
            showlegend=True,
            legend_title=" ",

            plot_bgcolor='white',
            legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.05
            )
        )

        fig.add_annotation( x=adj_close.index[0] - relativedelta(days=10), y=max_value + 10, ax=adj_close.index[0] - relativedelta(days=10), ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=1, arrowcolor='black')

        fig.add_annotation(x=adj_close.index[-1] +  relativedelta(months=10), y=0, ax=adj_close.index[0] - relativedelta(days=15) , ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=1, arrowcolor='black')

        fig.data[0].line.color = 'rgb(197, 175, 92)'
        fig.data[0].line.width = 1
        fig.data[0].name = Class.Yahoo_value_name[0]
        


        time_to_add_style = relativedelta(days=5)    
        time_to_add = relativedelta(years=1)    
        
        lastdate = Class.DDR1
        lastdate_tmp =  adj_close.index[-1] - time_to_add_style
        firstdate = Class.DDR1 - relativedelta(years=12)
        firstdate_tmp = firstdate
        seconddate = firstdate + 2* time_to_add
        thirddate = firstdate + 2 *2 * time_to_add
        fourthdate = firstdate + 3 *2 * time_to_add
        fivthdate = firstdate + 4 *2 * time_to_add
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
        # lastdate_visu = lastdate[8:10] + "/" + lastdate[5:7] + "/" + lastdate[0:4]

        ###############LE STYLE D AFFICHAGE###########

        fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [firstdate_tmp, seconddate, thirddate, fourthdate, fivthdate, sixthdate, lastdate_tmp],
                    ticktext= [firstdate_visu, seconddate_visu, thirddate_visu, fourthdate_visu, fivthdate_visu, sixthdate_visu, lastdate_value]
                    ),
        
        #fig.show()
        # fig.update_xaxes(range=[firstdate - relativedelta(months=4), lastdate])
        # fig.update_yaxes(range=[-3,130])
        fig.write_image(Name, format="png", scale=4, engine='kaleido')
    except Exception:
        print("error yahoo")

    simple_yahoo_value_arrays = [1, 3 ,5 , 10 ] # le tableau pour la boucle pour les années
    for i in Class.Yahoo:
        my_array = [] #j'initie un nouveau tableau a chaque sousjacent

        for i in simple_yahoo_value_arrays: #je fias une boucle pour parcourir les valeurs (1, 3,5 etc)
            try:
                result = get_value_array(int(i), end_date, adj_close)
                result = ("{:.2f}".format(result))
                result = result.replace(".", ",") #joli format écrit
                result = result + "%"

                my_array.append(result)
            except Exception:
                my_array.append("N/A")
                pass
        
        try: #je  sors de la boucle et je rajoute le 10 ans "manuellement" car il est légèrement différent
            result = get_value_array(int(0), start_date, adj_close)
            result = ("{:.2f}".format(result))
            result = result.replace(".", ",")
            result = result + "%"

            my_array.append(result)

        except Exception:
            my_array.append("N/A")
        

        Class.Yahoo_value.append(my_array)


#S'il y'a plusieurs blocs
def bloc4_multiple_tickers(tickers, Class, Name):
    bdays=BDay()

    end_date = Class.DPCI    
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    end_date = end_date - datetime.timedelta(days=1)
    is_business_day = bdays.is_on_offset(end_date)

    try:
        while is_business_day != True:
            end_date = end_date - datetime.timedelta(days=1)
            is_business_day = bdays.is_on_offset(start_date)
        #end_date/startdate -1
        start_date = end_date - relativedelta(days=1)
        start_date = end_date - relativedelta(years=12)
        is_business_day = bdays.is_on_offset(start_date)
        while is_business_day != True:
            start_date = start_date + datetime.timedelta(days=1)
            is_business_day = bdays.is_on_offset(start_date)
      
        df_list = []
        result = pd.DataFrame()
        name = []
        i = 0
        # User pandas_reader.data.DataReader to load the desired data. As simple as that.
        for datas in tickers:
            try:
                panel_data = data.DataReader(datas, 'yahoo', start_date, end_date)

                adj_close = panel_data["Adj Close"]
                lastvalue = adj_close.iloc[0]
                adj_close.columns = ['Adj Close']

                df_list.append(adj_close)
                
                panel_data[datas] = (panel_data['Adj Close'] / lastvalue) * 100
                result[datas] = (panel_data['Adj Close'] / lastvalue) * 100
                name.append(datas)
                print("aasoikjoasjaisooajisioaj", Class.Yahoo_value_name)
                i += 1
            except Exception:
                print("erreur tickers")

            # result = ((lastvalue/firstvalue) -1) * 100

        colors = ['#B9A049', '#0B3371', '#C00000', '#007A37', '#4639F3']

        if len(name) == 2:
                fig = px.line(data_frame = result
                        ,x = result.index
                        ,y = [result[name[0]],result[name[1]]],
                                                title="Base 100",

                        ) 
                fig.data[0].name = Class.Yahoo_value_name[0]
                fig.data[1].name = Class.Yahoo_value_name[1]

        if len(name) == 3:
                fig = px.line(data_frame = result
                        ,x = result.index
                        ,y = [result[name[0]],result[name[1]], result[name[2]]],
                                                title="Base 100",

                        )
                fig.data[0].name = Class.Yahoo_value_name[0]
                fig.data[1].name = Class.Yahoo_value_name[1]
                fig.data[2].name = Class.Yahoo_value_name[2]

        if len(name) == 4:
                fig = px.line(data_frame = result
                        ,x = result.index
                        ,y = [result[name[0]],result[name[1]], result[name[2]], result[name[3]]],
                                                title="Base 100",

                        )
                fig.data[0].name = Class.Yahoo_value_name[0]
                fig.data[1].name = Class.Yahoo_value_name[1]
                fig.data[2].name = Class.Yahoo_value_name[2]
                fig.data[3].name = Class.Yahoo_value_name[3]

        if len(name) == 5:
                fig = px.line(data_frame = result
                        ,x = result.index
                        ,y = [result[name[0]],result[name[1]], result[name[2]], result[name[3]], result[name[4]]],
                                                title="Base 100",

                        )
                fig.data[0].name = Class.Yahoo_value_name[0]
                fig.data[1].name = Class.Yahoo_value_name[1]
                fig.data[2].name = Class.Yahoo_value_name[2]
                fig.data[3].name = Class.Yahoo_value_name[3]
                fig.data[4].name = Class.Yahoo_value_name[4]

        for color_line in range(len(name)): #tracer des couleurs des lignes
            fig['data'][color_line]['line']['color']=colors[color_line]
            #fig['data'][color_line]['line']['name']= Class.Yahoo_value_name[color_line]

        fig.update_layout(
                xaxis=dict(
                    showline=False,
                    showgrid=True,
                    showticklabels=True,
                    linecolor='rgb(0, 0, 0)',
                    linewidth= 1,
                    
                    ticks='outside',
                    title=None,
                    tickfont=dict(
                        family='Proxima Nova',
                        size=12,
                        color='rgb(82, 82, 82)',   
                    ),
                ),
                yaxis=dict(
                    showgrid=True,
                    zeroline=False,
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
                ),
                 title=dict(
                x=0.09,
                y=0.85,
                font=dict(
                    family="Arial",
                    size=10,
                    color='#000000'
                )
            ),
                showlegend=True,
                legend_title=" ",

                 legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.05
            ),
                plot_bgcolor='white'
            )
                
        lastvalue = adj_close.iloc[-1]
        firstvalue = adj_close.iloc[0]
        max_value = result.max() + 20

        max_max_value = (max(max_value))

        fig.add_annotation( x=result.index[0] -  relativedelta(days=10), y=max_max_value + 10, ax=result.index[0] - relativedelta(days=10), ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=1, arrowcolor='black')

        fig.add_annotation(x=result.index[-1] + relativedelta(months=10), y=0, ax=result.index[0] - relativedelta(days=15), ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=1, arrowcolor='black')

        # fig.show()
        time_to_add_style = relativedelta(days=5)    
        time_to_add = relativedelta(years=1)    
        lastdate = Class.DDR1
        lastdate_tmp =  adj_close.index[-1] - time_to_add_style
        firstdate = Class.DDR1 - relativedelta(years=12)
        firstdate_tmp = firstdate
        seconddate = firstdate + 2* time_to_add
        thirddate = firstdate + 2 *2 * time_to_add
        fourthdate = firstdate + 3 *2 * time_to_add
        fivthdate = firstdate + 4 *2 * time_to_add
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
        # lastdate_visu = lastdate[8:10] + "/" + lastdate[5:7] + "/" + lastdate[0:4]

        ###############LE STYLE D AFFICHAGE###########

        fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [firstdate_tmp, seconddate, thirddate, fourthdate, fivthdate, sixthdate, lastdate_tmp],
                    ticktext= [firstdate_visu, seconddate_visu, thirddate_visu, fourthdate_visu, fivthdate_visu, sixthdate_visu, lastdate_value]
                    ),
        fig.write_image(Name, format="png", scale=2, engine='kaleido')
       
    except Exception:
        print("error in yahoo")
    

    simple_yahoo_value_arrays = [1, 3 ,5 , 10] # le tableau pour la boucle pour les années

    compteur = 0
    end = datetime.datetime.strptime(Class.DDR, '%d/%m/%Y')
    end_date = end -  datetime.timedelta(days=1)

    is_business_day = bdays.is_on_offset(end_date)

    while is_business_day != True:
            end_date = end_date - datetime.timedelta(days=1)
            is_business_day = bdays.is_on_offset(end_date)

        
    for i in Class.Yahoo:
        my_array = [] #j'initie un nouveau tableau a chaque sousjacent
        for j in simple_yahoo_value_arrays: #je fias une boucle pour parcourir les valeurs (1, 3,5 etc)
            try:
                result = get_value_array(int(j), end_date, df_list[compteur])
                result = ("{:.2f}".format(result))
                result = result.replace(".", ",") #joli format écrit
                result = result + "%"

                my_array.append(result)
            except Exception:
                my_array.append("N/A")
        
        try: #je  sors de la boucle et je rajoute le 10 ans "manuellement" car il est légèrement différent
            result = get_value_array(int(0), start_date, df_list[compteur])
            result = ("{:.2f}".format(result))
            result = result.replace(".", ",")
            result = result + "%"

            my_array.append(result)

        except Exception:
            my_array.append("N/A")
        
        compteur +=1
        Class.Yahoo_value.append(my_array)

        # print(Class.Yahoo_value)