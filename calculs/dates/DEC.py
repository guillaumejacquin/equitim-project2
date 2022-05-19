def dec(Class):
    dec = Class.DEC
    annee = dec[0:4]
    mois = dec[5:7]
    jours = dec[8:10]
  
    mystring = jours + "/" + mois + "/" + annee
    Class.DEC_affichage = mystring