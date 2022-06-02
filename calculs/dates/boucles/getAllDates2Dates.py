import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import sys


def get_all_dates_between_2_dates_with_special_begin(Class, date_départ, date_de_fin, date_debut_analyse, date_fin_analyse, exclus=False, constat=True):
    date_depart = date_départ
    date_fin = date_de_fin
    compteur = 0
    result_dates = []
    inFile = "database/Calendar_US_Target.xlsx" #On ouvre l'excel
    inSheetName = "Sheet1" #le nom de l excel
    df =(pd.read_excel(inFile, sheet_name = inSheetName))

    date_depart = datetime.datetime.strptime(date_depart, '%Y-%m-%d') #date du départ
    date_fin = datetime.datetime.strptime(date_fin, '%Y-%m-%d') #date finale

    date_calcul_depart = datetime.datetime.strptime(date_debut_analyse, '%Y-%m-%d') #date d'ou va commencer le tableau
    date_calcul_fin = datetime.datetime.strptime(date_fin_analyse, '%Y-%m-%d') #date d'ou va finir notre tableau

    var_date_depart = date_depart

    time_to_add = ""

    #pour ajouter la fréquence (en fonction de la fréquence)
    if (Class.F0 == "mois"):
        time_to_add = relativedelta(months=1)    
        
    if (Class.F0 == "trimestre"):
        time_to_add = relativedelta(months=3)    

    if (Class.F0 == "semestre"):
        time_to_add = relativedelta(months=6)    

    if (Class.F0 == "année"):
        time_to_add = relativedelta(years=1)    


    #une boucle inf
    while var_date_depart <= date_fin +  relativedelta(days=1):
        #on récupère les colonnes du excel (parie francaise)
        mask = (df['TARGETirs_holi'] >= var_date_depart) # JOUR SUIVANT
        #ca recree un dataframe de valeurs plus grande
        result = df[mask]['TARGETirs_holi'].iloc[0]
        #on récupère la premiere valeur de ce dataframe

        if (result >= date_calcul_depart  and result <= date_calcul_fin):
            # print(result)
            #si la date est compris entre les 2 dates ou je veux qu il y ait mon tableau
            if (compteur == 0 and constat == True): #ajouter le premier element                
                mask = (df['TARGETirs_holi'] >= date_calcul_depart) # JOUR SUIVANT
        #ca recree un dataframe de valeurs plus grande
                result = df[mask]['TARGETirs_holi'].iloc[0]

            result = (str(result)[0:10])
            result = result[8:10] + "/" + result[5:7] + "/" + result[0:4] 

            result_dates.append(str(result))  #le resultat bien ajouté
            compteur += 1

        
        var_date_depart = var_date_depart + time_to_add #on ajoute x temps
    
    if (exclus == True):
        result_dates = result_dates[1:-1] #si l option exclus est ajoutée: On retire le premier élément

    real_result = ', '.join(result_dates)
    return(real_result)

def get_all_dates_between_2_dates_with_special_begin_njo(Class, date_départ, date_de_fin, date_debut_analyse, date_fin_analyse,  exclus=False, constat=False, exemple=""):
    date_depart = date_départ
    date_fin = date_de_fin
    compteur=0 

    #temporaire
    result = (str(Class.DR1)[0:10])
    result = result[8:10] + "/" + result[5:7] + "/" + result[0:4]
    result_dates = []
    #temporaire
    inFile = "database/Calendar_US_Target.xlsx"
    inSheetName = "Sheet1"
    df =(pd.read_excel(inFile, sheet_name = inSheetName))

    date_depart = datetime.datetime.strptime(date_depart, '%Y-%m-%d')
    date_fin = datetime.datetime.strptime(date_fin, '%Y-%m-%d')
    date_calcul_depart = datetime.datetime.strptime(date_debut_analyse, '%Y-%m-%d')

    date_calcul_fin = datetime.datetime.strptime(date_fin_analyse, '%Y-%m-%d')
    var_date_depart = date_depart

    time_to_add = ""
    nombre_dejours_ouvres = int(Class.NJO) #on y ajoute les jours ouvrés

    if (Class.F0 == "mois"):
        time_to_add = relativedelta(months=1)    
        
    if (Class.F0 == "trimestre"):
        time_to_add = relativedelta(months=3)    

    if (Class.F0 == "semestre"):
        time_to_add = relativedelta(months=6)    

    if (Class.F0 == "année"):
        time_to_add = relativedelta(years=1)    

    if (exemple == "paiement1"):
        if (Class.F0 == "mois"):
            time_to_add2 = relativedelta(months=1)    
            
        if (Class.F0 == "trimestre"):
            time_to_add2 = relativedelta(months=3)    

        if (Class.F0 == "semestre"):
            time_to_add2 = relativedelta(months=6)    

        if (Class.F0 == "année"):
            time_to_add2 = relativedelta(years=1)   
    else:
        time_to_add2 = relativedelta(days=0) 
        
    while var_date_depart < date_fin + relativedelta(days=1) + time_to_add2:
        mask = (df['TARGETirs_holi'] >= var_date_depart) # JOUR SUIVANT
        result = df[mask]['TARGETirs_holi'].iloc[0]
    
        # if result < date_calcul_depart:
        #     print("ici", result)

        if (result >= date_calcul_depart and result <= date_calcul_fin):
            if compteur == 0 and constat ==True:
                result = date_calcul_depart
                compteur +=1
            else:
                result = df[mask]['TARGETirs_holi'].iloc[nombre_dejours_ouvres] #on y ajoute l element de jours ouvrés


            result = (str(result)[0:10])
            result = result[8:10] + "/" + result[5:7] + "/" + result[0:4]
            result_dates.append(str(result))

        
        var_date_depart = var_date_depart + time_to_add
    
    if (exclus == True):
        result_dates = result_dates[1:-1]

    real_result = ', '.join(result_dates)
    return(real_result)

