#si frequence == annee alors du se transforme en "de l'(annee)" au lieu "du (semestre)"

def F0du(Class):
    if (Class.F0 == "année"):
        Class.DU = "de l'"
        Class.DU1 = "De l'"
