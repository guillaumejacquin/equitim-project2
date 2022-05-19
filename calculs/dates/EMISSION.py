def emission(Class):
    emisison = Class.Emission
    annee = emisison[0:4]
    mois = emisison[5:7]
    jours = emisison[8:10]
  
    mystring = jours + "/" + mois + "/" + annee
    Class.Emission_affichage = mystring