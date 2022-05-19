def DCF(Class):
    dcf = Class.DCF
    annee = dcf[0:4]
    mois = dcf[5:7]
    jours = dcf[8:10]
  
    mystring = jours + "/" + mois + "/" + annee
    Class.DCF_affichage = mystring