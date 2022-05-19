def tds(Class):
    NDR = Class.NDR
    SJR5 = Class.SJR5
    DCI = Class.DCI
    SJR3 = Class.SJR3

    if Class.type_strike == "strike moyen":
        string = "Le" +  NDR + "correspond à la moyenne arithmétique des " + SJR5 + " de clôture aux dates suivantes : " + DCI + "."
        Class.TDS = string

    if Class.type_strike == "best strike":
        string = "Le" +  NDR + "correspond au " + SJR3 + " de clôture aux dates suivantes : " + DCI +"."
        Class.TDS = string

    if Class.type_strike == "strike close" or Class.type_strike == "forward":
        string = "Le" +  NDR + "correspond au"+ SJR3 + " de clôture le " + DCI + "."
        Class.TDS = string
