from datetime import datetime
from dateutil import relativedelta

def DDPP(Class):
    frequence = Class.F0
    if Class.DDP == "error":
        Class.DDPP = ""
        return()

    date_time_obj = datetime.strptime(Class.DDP, '%Y-%m-%d')
    date_time_obj2 = datetime.strptime(Class.DDCI, '%Y-%m-%d')
    diff = date_time_obj2 - date_time_obj

    
    #Calcul à la louche, pour arrondir
    years = diff.days / 365
    months = diff.days / 30
    days = diff.days
    semestriels = diff.days/182
    trimestriels = diff.days / 91

    if (frequence == "jours"):
        result = days
    
    if (frequence == "mois"):
        result = int(months)
        if (months % days >= 15):
            result += 1

    if (frequence == "année"):
        result = int(years)
        if (years % days >= 182):
            result += 1

    if (frequence == "semestre"):
        result = int(semestriels)
        if (semestriels % days >= 91):
            result += 1

    if (frequence == "trimestre"):
        result = int(trimestriels)
        if (trimestriels % days >= 45):
            result += 1

    result = abs(result)
    #result = frequence + " " + str(result)
    Class.DDPP = result


