from datetime import date
from operator import index
from tkinter import E
from pandas import array
from pyxirr import xirr
from datetime import datetime, timedelta
from dateutil.relativedelta import *
import pandas as pd


def tra_athena(Class):
    #Ici, on appelle une fonction avec les variables qui changent  selon les tra
    Class.TRA_A_S1 = (xirr_test(Class, Class.PDC2, Class.DEC, Class.NSD)) #Scénario défavorable Athena (-100, NSD)
    Class.TRA_A_S2_100 = (xirr_test(Class, Class.PDC2, Class.DEC, 100)) #Scénario médian Athena (-100, 100)
    Class.TRA_A_S2_GAIN = (xirr_test(Class, Class.PDC2, Class.DEC, float(Class.GCE)+100)) #Scénario médian + gain Athena(-100, GCE+100)
    Class.TRA_M_SJ = (xirr_test(Class, Class.PDC2, Class.DEC, float(Class.NSM))) #Scénario médian SJ( -100 , NSM)
    tra_a = float(Class.CPN) * float(Class.PR1) + 100 #Scénario Favorable Athena( -100, CPN*1PR+100)
    Class.TRA_F_A = (xirr_test(Class, Class.PDC2, Class.DR1, tra_a)) #Scénario Favorable Athena( -100, CPN*1PR+100)
    Class.TRA_F_SJ = (xirr_test(Class, Class.PDC2, Class.DR1, Class.NSF)) #Scénario Favorable SJ( -100 , NSF)
    tra_mra_min_a =  float(Class.CPN)*float(Class.ADPR)+100 #Mécanisme de remboursement échéance perte (-100, PDI)
    Class.ADCF = Class.ADCF[0:10]

    Class.TRA_MIN_A = (xirr_test(Class, Class.PDC2, Class.DADR, tra_mra_min_a))#Mécanisme de remboursement anticipé MIN(-100, CPN*ADPR+100)
    Class.TRA_echeance_perte_A = (xirr_test(Class, Class.PDC2, Class.DEC, Class.PDI))#Mécanisme de remboursement échéance perte(-100, PDI)

def phoenix_3dates(Class, période1, période2):
        période1 = période1[6:10]+ "-" + période1[3:5] + "-" + période1[0:2]
        période2 = période2[6:10]+ "-" + période2[3:5] + "-" + période2[0:2]

        Class.TRA_D_P = (xirr_3dates_phoenix(Class, Class.PDC2 ,période1, Class.DEC, Class.CPN, Class.NSD)) #Scénario défavorable phoenix(-100,CPN, NSD)
        Class.TRA_M_P = (xirr_3dates_phoenix(Class, Class.PDC2,période2, Class.DEC, Class.CPN, 100)) #Scénario médian phoenix(-100,CPN, 100)
        Class.TRA_M_MP = (xirr_3dates_phoenix(Class, Class.PDC2,période2, Class.DEC, float(Class.CPN)*2, 100)) #Scénario médian phoenix mémoire(-100,CPN*2, 100)
        Class.TRA_GM_P = (xirr_3dates_phoenix(Class, Class.PDC2,période2, Class.DEC, Class.CPN,  float(Class.CPN) +100)) #Scénario médian phoenix ( -100,CPN, CPN+100)       
        tragmpm = float(Class.GCE) + 100 - 2 * float(Class.CPN)
        Class.TRA_GM_PM = (xirr_3dates_phoenix(Class, Class.PDC2,période2, Class.DEC, float(Class.CPN) * 2, tragmpm)) #Scénario médian phoenix mémoire(-100,CPN*2, GCE+100-2*CPN)
        Class.TRA_MIN_P = (xirr_test(Class, Class.PDC2, Class.ADCF, float(Class.CPN) + 100)) #Mécanisme de remboursement anticipé MIN phoenix ( -100, CPN+100)    
        #Mécanisme de remboursement anticipé MIN phoenix mémoire (-100, CPN*ADPR+100)


def xirr_test(Class, date1, date2, variable=100):
    first_date = date1 #max entre date émission et strike
    DPR = Class.DPR#first_date_autocall
    second_date = date2 #date_echeance

    flux_var = variable #Scenario Defavorable = flux_var

    # #variable formules
    first_date = datetime.strptime(first_date, '%Y-%m-%d')
    second_date = datetime.strptime(second_date, '%Y-%m-%d')
    soustract2dates = abs(first_date - second_date)
    soustract2dates = soustract2dates.days
    #soustraction des deux dates

    flux_varNet = float(flux_var)*0.99**(float(soustract2dates)/365)
    #operation des flux

    result = (xirr([first_date,second_date], [-100, float(flux_varNet)]))
    #appel de la fonction xirr (librairie)

    try:
        result = float(result) *100
        result = round(result, 2)
        result = (f'{result:.2f}')
        # mettre le résutlat en %

    except Exception:
        pass
    return(result)

#la meme chose que xirr_test mais avec 3 dates
def xirr_3dates_phoenix(Class, date1, date2, date3, variable, variable2):
    first_date = date1[0:10] #max entre date émission et strike
    second_date = date2[0:10] #date_echeance
    third_date = date3[0:10]

    flux_var = float(variable) #Scenario Defavorable = flux_var
    flux_var2 = float(variable2)
    # #variable formules
    first_date = datetime.strptime(first_date, '%Y-%m-%d')
    second_date = datetime.strptime(second_date, '%Y-%m-%d')
    third_date = datetime.strptime(third_date, '%Y-%m-%d')

    soustract2dates = abs(first_date - second_date)
    soustract2dates = soustract2dates.days
    flux_varNet = float(flux_var)*0.99**(float(soustract2dates)/365)

    soustracttheseconddates = abs(third_date - first_date)
    soustracttheseconddates = soustracttheseconddates.days
    flux_varNet2 = float(flux_var2)*0.99**(float(soustracttheseconddates)/365)

    result = (xirr([first_date,second_date, third_date], [-100, float(flux_varNet), float(flux_varNet2)]))
    #la fonction xirr

    try:
        result = float(result) *100
        result = round(result, 2)
        result = (f'{result:.2f}')

    except Exception:
        pass
    return(result)


def boucleTRA(Class, date1, date2, df, variable, variable2, exception=""):
    first_date = datetime.strptime(date1, '%Y-%m-%d')
    second_date = datetime.strptime(date2, '%Y-%m-%d')

    df["dates"] = pd.to_datetime(df['dates'], format='%d/%m/%Y')
    #on met le dataframe au format de dates
    #premiere date 
    
    pd.options.mode.chained_assignment = None 
    try:  
        df["flux"] = float(variable)
        df["flux"].loc[0] = -100
        df["flux"].loc[-1] = float(variable2)
        df["dates"].loc[0] = first_date
        

        df["dates"] = pd.to_datetime(df['dates'], format='%Y-%m-%d')
        df["soustract2dates"] = (df["dates"] - first_date).dt.days

        df2 = df[ df['dates'] <= second_date]
        df2["flux"].iloc[-1] += 100
        #on cree un deuxième dataframe mon pote

        if (exception == "med_p"):
            df2["flux"].iloc[-1] = float(Class.PDI)
            #une exception

        if (exception == "tout_sauf_p"):
            df2["flux"].iloc[-1] = 100
            #une exception


        df2["flux_varNet"] = (df2['flux'])*0.99**((df2["soustract2dates"])/365)
        #on ajoute des colomnes
        
        result = (xirr(df2["dates"], df2["flux_varNet"]))
        #toujours l'appel a la fonction xirr

    except Exception:
        print("non")

    try:
             
            result = float(result) *100
            result = round(result, 2)
            result = (f'{result:.2f}')
            #on met en %

    except Exception:
            result = 0
            print("je chiale") #message d'erreur


    return(result)

def ALL_TRA(Class):
    #athéna
    tra_athena(Class)
    
    #Phoenix

    Class.TRA_MRE_Min_P = (xirr_test(Class, Class.PDC2, Class.DEC, 100 + float(Class.CPN)))
    Class.TRA_MRA_MIN_PM = (xirr_test(Class, Class.PDC2, Class.DADR, 100 + float(Class.GCE) - float(Class.CPN)))

    Class.TRA_MRE_MIN_PM = (xirr_test(Class, Class.PDC2, Class.DEC, 100 + float(Class.GCE)))

    if (Class.F0 == "jours"):
        compteur = relativedelta(days=+1) 

    if (Class.F0 == "mois"):
        compteur = relativedelta(months=+1)

    if (Class.F0 == "trimestre"):
        compteur = relativedelta(months=+3)        
    
    if (Class.F0 == "semestre"):
        compteur = relativedelta(months=+6)

    if (Class.F0 == "année"):
        compteur = relativedelta(years=+1)    

    #on appelle le dataframe pour les tra_max
    dataframe_dates = Class.Datespaiement1.split(", ")
    df = pd.DataFrame({'col':dataframe_dates})
    df.columns=["dates"]

    compteurvar = Class.DADR
    date_time_obj = datetime.strptime(Class.PDC2, '%Y-%m-%d')
    compteurvar = datetime.strptime(compteurvar, '%Y-%m-%d')
    période = 0

    #les 2 périodes
    période1 = df['dates'].iloc[1]
    période2 = df['dates'].iloc[2]
    # print("------------------------------------------------------------------------------------------------")
    # print(df['dates'])
    # print("------------------------------------------------------------------------------------------------")

    phoenix_3dates(Class, période1, période2)


    #On appelle encore la fcontion en changeant les arguments pour que le résultat ne soit pas le même
    Class.TRA_F_P = (boucleTRA(Class, Class.PDC2, Class.DR1, df, Class.CPN, float(Class.CPN)+100)) #Scénario favorable phoenix
    # df.drop(df.tail(1).index,inplace=True)
  
    # Class.MDR_P = (boucleTRA(Class, Class.PDC2, df2, Class.CPN, Class.PDI)) #Scénario favorable phoenix( -100,CPN,…,PDI)
    # Class.MDR_TRA_TOUT_SAUF_P = (boucleTRA(Class, Class.PDC2, df2, Class.CPN, 100)) #TRA remboursement échéance médian max( -100,CPN,…,100)
    Class.TRA_TOUT_P = (boucleTRA(Class, Class.PDC2,Class.DEC, df, Class.CPN, Class.PDI)) #Scénario favorable phoenix( -100,CPN,…,PDI)
    
    Class.TRA_MED_P = (boucleTRA(Class, Class.PDC2,Class.DEC, df, Class.CPN, Class.PDI, "med_p")) #Scénario favorable phoenix( -100,CPN,…,PDI)
    # Class.TRA_FP = (boucleTRA(Class, Class.PDC2, df, Class.CPN, float(Class.CPN)+100)) #Scénario favorable phoenix
    Class.TRA_TOUT_1_P = (boucleTRA(Class, Class.PDC2,Class.DADR, df, Class.CPN, Class.PDI)) #Scénario favorable phoenix( -100,CPN,…,PDI)
    Class.TRA_TOUT_SAUF_P = (boucleTRA(Class, Class.PDC2,Class.DEC, df, Class.CPN, Class.PDI, "tout_sauf_p"))
    #2 eme dataframe pour aller jusqu a l echance et plus jusque a 1dr
    compteurvar = Class.DEC
    try:#des petites gestions d erreurs pour éviter le crash
        Class.TRA_MAX_P = max(Class.TRA_TOUT_P, Class.TRA_F_P) 
    except Exception:
        Class.TRA_MAX_P = 0
    
    #print(Class.TRA_TOUT_1_P, Class.TRA_F_P)
    try:
        Class.TRA_MRA_MAX_P = max(Class.TRA_TOUT_1_P, Class.TRA_F_P) 
    except Exception:
        Class.TRA_MRA_MAX_P = 0


    if (Class.Typologie == "coupon phoenix" and  Class.CPN_is_memoire == "oui"):
        Class.TRA_RM_P = Class.TRA_MRA_MIN_PM
    else:
        Class.TRA_RM_P = Class.TRA_MRA_MIN_P
    
    if (Class.CPN_is_memoire == "oui"):
        Class.TRA_EM_P = Class.TRA_MRE_MIN_PM
    else:
        Class.TRA_EM_P = Class.TRA_MRE_MIN_P

    

    if Class.PDI == Class.BFP:
        if (Class.CPN_is_memoire == "oui"):
            Class.TRA_EM_P = Class.TRA_GM_PM
        else:
            Class.TRA_RM_P = Class.TRA_GM_P
    
    else:
        if (Class.CPN_is_memoire == "oui"):
            Class.TRA_EM_P = Class.TRA_M_PM
        else:
            Class.TRA_RM_P = Class.TRA_M_P

