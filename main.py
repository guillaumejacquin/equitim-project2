from cgitb import small
from P_D_E.myclass import *
from calculs.dates.DR1 import DR1
from calculs.style.SJR6P1 import SJR6P1
from change_text import *
from calculs.dates.PDC1 import *
from calculs.dates.DDR import *
from calculs.dates.DIC import *
from calculs.pdiperf import *
from calculs.periodes.pr import *
from calculs.TDP import *
from calculs.GC import *
from calculs.abac import *
from calculs.ndr import *
from calculs.sjr import *
from calculs.TDS import *
from calculs.dates.DEC import *
from calculs.dates.DCF import *
from calculs.dates.DR1 import *
from calculs.dates.DPR import *
from calculs.dates.EMISSION import *
from calculs.periodes.f0s import *
from calculs.sponsor import *
from calculs.frequencedu import *
from calculs.balise import *
from database.mongo import *
from calculs.ebac import *
from calculs.dates.ADCF import *
from calculs.wordingdeg.SV import *
from calculs.wordingdeg.balisedeg import *
import time
from graphs.bloc3 import *
from graphs.bloc2 import *
from graphs.bloc4 import *
from graphs.bloc6 import *
from graphs.graph_scenario_defavorable import *
from graphs.graph_scenario_median import *
from graphs.graph_scenario_favorable import *

from calculs.dates.dates_maj import *
from calculs.GainOuCoupon import *
from calculs.Memoire.memoire import *
from calculs.TRA.tra import *
from calculs.TRA.CMTRA import *
from calculs.style.NOMP1 import *
from calculs.style.NOMSOUSJACENTP1 import *
from calculs.dates.DDPP import *
from calculs.dates.boucles.callAllDates2Date import *
from calculs.dates.DDCI_M_B_Strike import *
#traitement des données
def start_processus_template(Class):
    PDC1(Class)
    PDC2(Class)
    today_date(Class)
    dec(Class)
    dic(Class)
    pdiperf(Class)
    PR1(Class)
    DPRR(Class)
    adcf(Class)
    DPCI_maj(Class)

    TDP(Class)
    GC(Class)
    GCA(Class)
    ndr(Class)
    abac(Class)
    f1_f2(Class)
    SJR(Class)
    tds(Class)
    DCF(Class)
    DR1(Class)
    DPR(Class)
    emission(Class)
    f0s(Class)
    sponsor(Class)
    F0du(Class)
    balise(Class)
    takeinformations(Class)
    NOMP1(Class)
    NOMSOUSJACENTP1(Class)
    SJR6P1(Class)
    abac2(Class)
    # apdr_(Class)
    ebac(Class)
    Memoire(Class)
    Memoire2(Class)
    Memoire3(Class)
    Memoire4(Class)
    Memoire5(Class)
    Memoire6(Class)
    BFP(Class)
    PAGE(Class)
    DDPP(Class)
    GainOuCoupon(Class)
    PDC1_maj(Class)
    PDC2_maj(Class)
    DDR_maj(Class)
    DEC_maj(Class)
    DCI_maj(Class)
    DCF_maj(Class)
    DDCI_maj(Class)
    DDR1_maj(Class)
    DDR1_maj_start(Class)
    callAllDates2Date(Class)
    DDCI_M_B_Strike(Class)
    # ABAC2_MAJ(Class)
    ALL_TRA(Class)
    #si coupon autocall
    if (Class.Typologie == "coupon autocall"):
        Class.graph1 = bloc2(Class, "graph1.png", whitestrap=False)
    if (Class.Typologie == "coupon phoenix"):
        if (float(Class.ABDAC) <= float(Class.BCPN)):
            Class.graph1 = bloc3_4(Class, "graph1.png", whitestrap=False)
        else:
            Class.graph1 = bloc3(Class, "graph1.png", whitestrap=False)

    # Class.graph1 = bloc2(Class, "graph1.png", whitestrap=False)
    Class.graph2 = bloc3(Class, "graph2.png", whitestrap=True)
    Class.graph5 = bloc4(Class, "graph5.png")
    Class.smallgraph1 = smallgraph1(Class, "graph_scenario_def.png")
    Class.smallgraph2 = smallgraph2(Class, "graph_scenario_median.png")
    Class.smallgraph3 = smallgraph3(Class, "graph_scenario_fav.png")

    SV(Class)
    balisedeg(Class)
    BaliseCMTRA(Class)

    ChangeTextOnPpt(Class)

def main(Class):
        start = time.time()
        start_processus_template(Class)
        end = time.time()
        elapsed = end - start
        print("Votre pdf a été réalisé en", round(elapsed, 2), "secondes")
        return(0)
    # except Exception:
    #     return(1)



#date de constat mensuelles
#DATE SI MENSUEL, chaque "jour" du mois, à partir de la date du <premier rappel> (inclus), 
# et jusqu'au <date de constat finale> (inclus), ou le jour ouvré suivant si le "jour" du mois n'est pas un jour ouvré

#date remboursement mensuelle
#le <jour ouvré>  de Bourse suivant la date de constatation mensuelle.

#Lege,nde 3blocs (niveau de l'indice par rapport à son cours/niveau initial de référence)