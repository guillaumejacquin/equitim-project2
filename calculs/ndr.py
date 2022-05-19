def ndr(Class):
    if Class.TDP == "action" and Class.type_strike == "strike normal":
        Class.NDR = "Cours Initial" #la

    elif Class.TDP == "action" and (Class.type_strike == "best strike" or Class.type_strike == "strike moyen"):
        Class.NDR = "Cours de Référence"

    elif Class.TDP == "indice" and Class.type_strike == "strike normal":
        Class.NDR = "Niveau Initial" #celui la

    elif Class.TDP == "indice" and (Class.type_strike == "best strike" or Class.type_strike == "strike moyen"):
        Class.NDR = "Niveau de Référence"

    elif (Class.sous_jacent == "equipondéré indice" or Class.sous_jacent == "equipondéré action"):
        Class.NDR = "Niveau initial"
    else:
        Class.NDR = "ERREUR!!!!!!"
    
        print("TDP? NDR", Class.TDP, Class.NDR)
