def Memoire(Class):
    if Class.CPN_is_memoire == "oui":
        Class.Memoire = " \n + \n Les éventuels coupons mémorisés au préalable"

    else:
        Class.Memoire = ""

def Memoire2(Class):
    if Class.CPN_is_memoire == "oui":
        Class.Memoire2 = ", il est mis en mémoire"
    else:
        Class.Memoire2 = ""

def Memoire3(Class):
    if Class.CPN_is_memoire == "oui":
        Class.Memoire3 = "Les coupons non versés précédemment sont récupérés et versés au prochain paiement éventuel du coupon."
    else:
        Class.Memoire3 = ""

def Memoire4(Class):
    if Class.CPN_is_memoire == "oui":
        Class.Memoire4 = ", ils sont mis en mémoire"
    else:
        Class.Memoire4 = ""

def Memoire5(Class):
    if Class.CPN_is_memoire == "oui":
        Class.Memoire5 = "ainsi que le coupon mémorisé au préalable"
    else:
        Class.Memoire5 = ""

def Memoire6(Class):
    if Class.CPN_is_memoire == "oui":
        Class.Memoire6 = " ainsi que les coupons mémorisés au préalable"
    else:
        Class.Memoire6 = ""

def BFP(Class):
    if (Class.type_bar2 == "degressif"):
        Class.BFP = Class.DBAC

    else:
        Class.BFP = "<BCPN>"

def PAGE(Class):
    if (Class.type_bar2 == " "):
        Class.PAGE = "page 7"

    else:
        Class.PAGE = "page 8"