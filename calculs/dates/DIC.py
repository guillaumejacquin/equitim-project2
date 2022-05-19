from datetime import date, datetime
from dateutil import relativedelta

def dic(Class):
    remove_blank =  Class.DCI.replace(" ", "")
    mylist = remove_blank.split(",")
    myreallist = []
    for i in mylist:
            myreallist.append( i[6:] + "-" + i[3:5] + "-" + i[:2])

    max_value = max(myreallist)
    min_value = min(myreallist)
    
    #on met en format fr
    annee = max_value[0:4]
    mois = max_value[5:7]
    jours = max_value[8:10]
  
    mystring = jours + "/" + mois + "/" + annee
    Class.DDCI = max_value
    Class.DPCI = min_value
    Class.DDCI_affichage = mystring

    #date_premier_rappel
    date_time_obj = datetime.strptime(Class.DCF, '%Y-%m-%d')
    date_time_obj2 = datetime.strptime(max_value, '%Y-%m-%d')
    
    diff = relativedelta.relativedelta(date_time_obj, date_time_obj2)
    year = diff.years
    #arrondir a l'année

    if diff.months >= 0:
        Class.DIC = str(year) + " ans et " + str(diff.months) + " mois"
    
    else:
        Class.DIC = str(year) + " ans"

