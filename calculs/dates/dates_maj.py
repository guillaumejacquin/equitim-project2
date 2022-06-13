from dateutil.relativedelta import relativedelta

month =["POUET POUET", "janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre" ]
#tableau des mois(le tableau commencant a 0 et les mois a un, j'ai rempli le premier


#TOUTES LES DATES EN MAJUSCULE
def PDC1_maj(Class):
    month_string = (Class.PDC1[5:7])
    month_string = int(month_string)
    month_string = (month[month_string])

    pdc1_maj_constructor = Class.PDC1[8:10] + " " + month_string + " " + Class.PDC1[0:4] 
    Class.PDC1_MAJ = pdc1_maj_constructor

def PDC2_maj(Class):
    month_string = (Class.PDC2[5:7])
    month_string = int(month_string)
    month_string = (month[month_string])

    pdc2_maj_constructor = Class.PDC2[8:10] + " " + month_string + " " + Class.PDC2[0:4] 
    Class.PDC2_MAJ = pdc2_maj_constructor

def DDR_maj(Class):
    month_string = (Class.DDR[3:5])
    month_string = int(month_string)
    month_string = (month[month_string])

    DDR_maj_constructor = Class.DDR[0:2] + " " + month_string + " " + Class.DDR[6:10] 
    Class.DDR_MAJ = DDR_maj_constructor

def DPR_maj(Class):
    month_string = (Class.DPR[5:7])
    month_string = int(month_string)
    month_string = (month[month_string])

    DDR_maj_constructor = Class.DPR[8:10] + " " + month_string + " " + Class.DPR[0:4] 
    Class.DPR_MAJ = DDR_maj_constructor

def DEC_maj(Class):
    month_string = (Class.DEC[5:7])
    month_string = int(month_string)
    month_string = (month[month_string])

    DEC_maj_constructor = Class.DEC[8:10] + " " + month_string + " " + Class.DEC[0:4] 
    Class.DEC_MAJ = DEC_maj_constructor

def DCI_maj(Class):

    month_string = (Class.DCI[3:5])
    month_string = int(month_string)
    month_string = (month[month_string])

    DDR_maj_constructor = Class.DCI[0:2] + " " + month_string + " " + Class.DCI[6:10] 
    Class.DCI_MAJ = DDR_maj_constructor

def DCF_maj(Class):
    month_string = (Class.DCF[5:7])
    month_string = int(month_string)
    month_string = (month[month_string])

    DDR_maj_constructor = Class.DCF[8:10] + " " + month_string + " " + Class.DCF[0:4] 
    Class.DCF_MAJ = DDR_maj_constructor

def DDCI_maj(Class):
    month_string = (Class.DCI[3:5])
    month_string = int(month_string)
    month_string = (month[month_string])

    DDR_maj_constructor = Class.DDCI[8:10] + " " + month_string + " " + Class.DDCI[0:4] 
    Class.DDCI_MAJ = DDR_maj_constructor

def DPCI_maj(Class):
    month_string = (Class.DPCI[5:7])
    month_string = int(month_string)
    month_string = (month[month_string])

    DDR_maj_constructor = Class.DPCI[8:10] + " " + month_string + " " + Class.DPCI[0:4] 
    Class.DPCI_MAJ = DDR_maj_constructor

def DDR1_maj(Class):
    ddr1 = str(Class.DDR1)[0:10]

    month_string = (ddr1[5:7])
    month_string = int(month_string)
    month_string = (month[month_string])

    DDR_maj_constructor = ddr1[8:10] + " " + month_string + " " + ddr1[0:4] 
    DDR_maj_constructor = DDR_maj_constructor.upper()
    ddr_min = DDR_maj_constructor

    Class.DDR1_MAJ = DDR_maj_constructor
    Class.DDR1_MAJ_MIN = ddr_min

#DCI MAJ, DCF MAJ, DDCIDDR1_12_MAJ



def DDR1_maj_start(Class):
    ddr2 = (Class.DDR1) - relativedelta(years=12)
    ddr1 = str(ddr2)[0:10]

    month_string = (ddr1[5:7])
    month_string = int(month_string)
    month_string = (month[month_string])

    DDR_maj_constructor = ddr1[8:10] + " " + month_string + " " + ddr1[0:4] 
    DDR_maj_constructor = DDR_maj_constructor.upper()

    Class.DDR1_12_MAJ = DDR_maj_constructor

def F1_MAJ(Class):
    month_string = (Class.F1[5:7])
    month_string = int(month_string)
    month_string = (month[month_string])

    DDR_maj_constructor = Class.F1[8:10] + " " + month_string + " " + Class.F1[0:4] 
    Class.F1_MAJ = DDR_maj_constructor


# def ABAC2_MAJ(Class):
#     print("AHHHHHHHHHHH", )
#     month_string = (Class.ABAC2[5:7])
#     month_string = int(month_string)
#     month_string = (month[month_string])

#     DDR_maj_constructor = Class.ABAC2[8:10] + " " + month_string + " " + Class.ABAC2[0:4] 
#     Class.ABAC2_MAJ = DDR_maj_constructor
    

