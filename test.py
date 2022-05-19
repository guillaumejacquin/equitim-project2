import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta


def get_all_dates_between_2_dates():
    date_depart = "2024-04-19 00:00:00"
    date_fin = "2032-04-19 00:00:00"
    
    result_dates = []

    inFile = "database/Calendar_US_Target.xlsx"
    inSheetName = "Sheet1"
    df =(pd.read_excel(inFile, sheet_name = inSheetName))

    date_depart = datetime.datetime.strptime(date_depart, '%Y-%m-%d %H:%M:%S')
    date_fin = datetime.datetime.strptime(date_fin, '%Y-%m-%d %H:%M:%S')

    var_date_depart = date_depart

    while var_date_depart < date_fin:
        mask = (df['TARGETirs_holi'] >= var_date_depart)
        # print(mydataframe.head())
        result = df[mask]['TARGETirs_holi'].iloc[0]
        result = (str(result)[0:10])
        result = result[8:10] + "/" + result[5:7] + "/" + result[0:4]
        result_dates.append(str(result))

        
        var_date_depart = var_date_depart + relativedelta(years=1)



    print((result_dates))

