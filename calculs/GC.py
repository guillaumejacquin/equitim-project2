def GC(Class):
    if Class.BCPN_is_degressif != "" and Class.Typologie != "coupon autocall":
        Class.GC = "coupon"
    else:
        Class.GC = "gain"
    #coupon ou gain en fonction de si autocall ou phoenix



def GCA(Class):
    frequence = Class.F0

    if frequence == "année":
        i = 1
    if frequence == "semestre":
        i = 2
    if frequence == "trimestre":
        i = 4
    if frequence == "mois":
        i = 12
    if frequence == "jours":
        i = 365
    
    #le nombre de coupon à l'année
    GCA = float(Class.CPN) * i
    GCA = round(GCA, 2)
    GCA = (f'{GCA:.2f}')
    Class.GCA = str(GCA)