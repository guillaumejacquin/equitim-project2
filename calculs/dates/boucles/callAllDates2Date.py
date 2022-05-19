from pickle import TRUE
import pandas as pd
import datetime
from dateutil.relativedelta import relativedelta
import sys
from calculs.dates.boucles.getAllDates2Dates import *

def callAllDates2Date(Class):
    #print("jour suivant, exclus", get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DR1, True, True))
    #print("jour d'avant, exclus", get_all_dates_between_2_dates_with_special_begin_substraction(Class, Class.DDCI, Class.DCF, Class.DR1, exclus=True))
    Class.Datesconstatations1 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DR1, Class.DCF, True, False)

    #Class.Datesconstatations2 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DR1, True)

    Class.Datesconstatations3 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DDCI, Class.DCF, True, False)
    print("date de constatation autocall = ", Class.Datesconstatations3)
    print("-----\n")
    #Class.Datesconstatations4 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DCF, Class.DDCI, True)

    dpr = Class.DPR[0:10]
    print("ouhhh", Class.DR1)
    Class.Datesremb1 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DR1, Class.DCF, False, False)
    print("date de remboursement autocall = ", Class.Datesremb1)
    print("-----\n")

    #Class.Datesremb2 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DDCI, True, False)
    Class.Datesremb3 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DEC, Class.DDCI,Class.DEC, False, True)
    # Class.Datesremb4 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DDCI, True)
    Class.Datesremb5 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI,Class.DEC, False, False)
    # Class.Datesremb6 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DDCI, True)
    # Class.Datesremb7 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DDCI, True)
    # Class.Datesremb8 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DCF, Class.DDCI, True)
    
    Class.Datespaiement1 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI,Class.DEC, False, False)
    print("date de paiement coupon = ", Class.Datespaiement1)

    # Class.Datespaiement2 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI, True)
   # Class.Datespaiement3 = get_all_dates_between_2_dates_with_special_begin(Class, Class.DDCI, Class.DEC, Class.DDCI,Class.DEC, False, True)
    # #Class.Datespaiement4 = get_all_dates_between_2_dates_with_special_begin_constat(Class, Class.DDCI, Class.DEC, Class.DDCI, True)
    Class.Datespaiement5 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI,Class.DEC, True, True)
    # Class.Datespaiement6 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI, True)
    # Class.Datespaiement7 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI, True)
    # Class.Datespaiement8 = get_all_dates_between_2_dates_with_special_begin_njo(Class, Class.DDCI, Class.DEC, Class.DDCI, True)
