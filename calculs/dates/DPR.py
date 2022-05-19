def DPR(Class):
    dpr = Class.DPR
    annee = dpr[0:4]
    jours = dpr[5:7]
    mois = dpr[8:10]
  
    mystring = jours + "/" + mois + "/" + annee
    Class.DPR_affichage = mystring