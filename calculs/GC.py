def GC(Class):
    if Class.BCPN_is_degressif != "" and Class.Typologie != "coupon autocall":
        Class.GC = "coupon"
    else:
        Class.GC = "gain"
    



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
    
    GCA = float(Class.CPN) * i
    GCA = round(GCA, 2)
    GCA = (f'{GCA:.2f}')
    Class.GCA = str(GCA)