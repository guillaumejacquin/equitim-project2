def DR1(Class):
    #date de premier rappel
    dr1 = Class.DR1
    annee = dr1[0:4]
    jours = dr1[5:7]
    mois = dr1[8:10]
  
    mystring = jours + "/" + mois + "/" + annee
    Class.DR1_affichage = mystring