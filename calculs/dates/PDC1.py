from datetime import date


def PDC1(Class):
    remove_blank =  Class.DCI.replace(" ", "")
    mylist = remove_blank.split(",")
    myreallist = []
    for i in mylist:
        date_transformed = i[6:] + "-" + i[3:5] + "-" + i[:2]
        myreallist.append(date_transformed)

    min_mylist = max(myreallist)
    date_min = (min(Class.Emission, min_mylist))

    #on met en format fr
    annee = date_min[0:4]
    mois = date_min[5:7]
    jours = date_min[8:10]
  
    pdc1 = jours + "/" + mois + "/" + annee
    Class.PDC1 = date_min
    Class.PDC1_affichage = pdc1

def PDC2(Class):
    remove_blank =  Class.DCI.replace(" ", "")
    mylist = remove_blank.split(",")
    myreallist = []
    for i in mylist:
        date_transformed = i[6:] + "-" + i[3:5] + "-" + i[:2]
        myreallist.append(date_transformed)

    min_mylist = max(myreallist)
    date_min = (max(Class.Emission, min_mylist))

    
    Class.PDC2 = date_min
    
    #on met en format fr
    annee = date_min[0:4]
    mois = date_min[5:7]
    jours = date_min[8:10]
  
    pdc2 = jours + "/" + mois + "/" + annee
    Class.PDC2_affichage = pdc2