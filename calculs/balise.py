def balise(Class):
    #les variables
    strike = Class.type_strike
    ndr = Class.NDR
    sjr1 = Class.SJR1
    sjr3 = Class.SJR3
    ddi = Class.DDCI_affichage
    ddi2 = Class.DPCI
    ddi2 = ddi2[8:10] + "/" + ddi2[5:7] + "/" + ddi2[0:4]
    
    #de l' ou du
    if (Class.TDP == "action"):
        du = "de l'"
    else:
        du = "du"


    if (strike == "strike normal"):
        mystring = "Le "+ Class.NDR + " correspond au " + sjr3 + " de clôture de " + sjr1 + "" + Class.NOMSOUSJACENT +  " le " + ddi

    if (strike == "strike moyen"):
        mystring = "Le "+ Class.NDR + " correspond à la moyenne arithmétique des " + sjr3 + " de clôture de " + sjr1 + " " + Class.NOMSOUSJACENT + " du " + ddi2 + " au " + ddi

    if (strike == "best strike"):
        mystring = "Le "+ Class.NDR + " correspond au " + sjr3 + " de clôture " + Class.NOMSOUSJACENT + " le plus bas observé aux dates suivantes : \n" + Class.DCI + "."

    Class.balise = mystring


#DCF MAJUSCULE