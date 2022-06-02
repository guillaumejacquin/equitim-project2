from pickle import TRUE
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import sys
from calculs.dates.boucles.getAllDates2Dates import *

def callAllDates2Date(Class):
    dcf_tmp = Class.DCF
    dcf = ", " + dcf_tmp[8:10] + "/" + dcf_tmp[5:7] + "/" + dcf_tmp[0:4]

    dpr = Class.DPR[0:10]
    #print("jour suivant, exclus", get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DR1, True, True))
    #print("jour d'avant, exclus", get_all_dates_between_2_dates_with_special_begin_substraction(Class, Class.DDCI, Class.DCF, Class.DR1, exclus=True))
    Class.Datesconstatations1 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, dpr, Class.DCF, False, False)
    # print("aiaiaiaiaiai", Class.DPR)
    # print("ici enculé", Class.Datesconstatations1)
    # print("---------------------------------------------------")
    Class.Datesconstatations1 = Class.Datesconstatations1 + dcf

    #Class.Datesconstatations2 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DR1, True)

    Class.Datesconstatations3 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DDCI, Class.DCF, True, False)
    Class.Datesconstatations3 = Class.Datesconstatations3 + dcf

    # print("date de constatation autocall = ", Class.Datesconstatations3)
    # print("-----\n")
    #Class.Datesconstatations4 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DDCI, True)

    
    Class.Datesremb1 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, dpr, Class.DCF, False, False) #Rjouter la premiere date
    Class.Datesremb1 = Class.Datesremb1[:-12]

    # print("date de remboursement autocall = ", Class.Datesremb1)
    # print("-----\n")

    #Class.Datesremb2 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DDCI, True, False)
    Class.Datesremb3 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DEC, Class.DDCI,Class.DEC, False, True)
    # Class.Datesremb4 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DDCI, True)
    Class.Datesremb5 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI,Class.DEC, False, False)
    # Class.Datesremb6 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DDCI, True)
    # Class.Datesremb7 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DDCI, True)
    # Class.Datesremb8 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DDCI, True)
    
    Class.Datespaiement1 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI,Class.DEC, True, False, "paiement1")
    # Class.Datespaiement1 += dcf
    #Class.Datespaiement1 = str(Class.DCF) + Class.Datespaiement1
    #print("date de paiement coupon = ", Class.Datespaiement1)

    # Class.Datespaiement2 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI, True)
   # Class.Datespaiement3 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DEC, Class.DDCI,Class.DEC, False, True)
    # #Class.Datespaiement4 = get_all_dates_between_2_dates_with_special_begin_constat(Class, Class.DDCI, Class.DEC, Class.DDCI, True)
    Class.Datespaiement5 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI,Class.DEC, True, True)
    # Class.Datespaiement6 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI, True)
    # Class.Datespaiement7 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI, True)
    # Class.Datespaiement8 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI, True)

    dpr = Class.DPR[0:10]
    Class.dates_constat_autocall = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DEC, dpr, Class.DCF, False, False)
    Class.dates_paiement_autocall = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, dpr, Class.DCF, False, False)


    Class.dates_constat_phoenix = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DEC, dpr, Class.DCF, False, False)
    Class.dates_paiement_phoenix = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, dpr, Class.DCF, False, False)
    Class.dates_last_remboursement_rappel = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, dpr, Class.DADR, False, True)

#pr
# 
# emier rajouter l
#date de remboursement il manque la premiere et jarter la drniere