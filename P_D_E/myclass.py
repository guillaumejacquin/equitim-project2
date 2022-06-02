from re import S


class InformationsForm():
    def __init__(self):
        #LES VARIABLES QU ON VA REMPLIR INITIEES VIA LE FORMULAIRE
        self.template = "testmercredi"
        self.Nom = "Actions BSV Mensuel Avril 2022"
        self.Typologie = "athéna"
        self.Droit = "français"
        self.Isin = "FR0014009DK8"
        self.Emission = "2022-04-22"
        self.DCI = "14-04-2022, 18-03-2022"
        self.DR1 = "2023-04-14"
        self.DPR = "2023-04-28"
        self.DADR = "2027-06-28"
        self.DCF = "2027-07-14"
        self.DEC = "2027-07-28"
        self.ADCF = "2027-06-14"

        self.F0 = "mois"
        self.TSJ = ["BNP FP Equity", "STLA FP Equity", "VIE FP Equity", "", ""]


        self.PCS1 = "Euronext Paris"
        self.PCS2 = "Euronext Paris"
        self.PCS3 = "Euronext Paris"
        self.PCS4 = ""
        self.PCS5 = ""


        self.CPN = "1.00"
        self.CPN_is_memoire = ""
        self.PDI = "50"
        self.BAC = "95"
        self.BAC_is_degressif = "oui"
        self.BCPN = "95"
        self.BCPN_is_degressif = ""

        self.COM = "1.0"
        self.NSD = "30"
        self.NSM = "70"
        self.NSF = "115"

        self.ABDAC = "67.5"
        self.DBAC = "66.95"
        self.DEG = "0.55"


        self.type_strike = "best strike"
        self.type_bar = "degressif"

        #self.sous_jacent_nom = ""
        self.sous_jacent = "wo action"
        #self.typeoffre = ""
    
        self.DDP = ""
        self.NJO = ""
        #on appelle la fonction pour  initier les variables de calcul
        self.var_calculs()
    
    #AUTRES VARIABLES, ICI CALCULS
    def var_calculs(self):
        self.NDR = ""
        self.DDCI = ""
        self.DPCI = ""
        self.PDC1 = ""
        self.PDC2 = ""
        self.DDR = ""
        self.DDR1 = ""
        self.DIC = ""
        self.PDIPERF = ""
        self.DTRAT = ""
        self.PR1 = ""
        self.DPRR = ""
        self.TDP = ""
        self.GC = ""
        self.GCA = ""
        self.GCE = ""
        self.ABAC = ""
        self.ADPR = ""
        self.F1 = ""
        self.F2 = ""

        self.SJR1 = ""
        self.SJR2 = ""
        self.SJR3 = ""
        self.SJR4 = ""
        self.SJR5 = ""
        self.SJR6 = ""
        self.SJR7 = ""
        self.SJR8 = ""

        self.TDS = ""
        
        self.GainOuCoupon = ""
        self.PDC1_affichage = ""
        self.PDC2_affichage = ""
        self.ADCF_affichage = ""
        self.DEC_affichage = ""
        self.DFC_affichage = ""
        self.Emission_affichage = ""
        self.F0s = "s"

        self.SPONSOR = "sponsor"
        self.sponsor = ""
        self.balise = ""
        self.DU = "du"
        self.DU1 = "Du"
        self.NOMSOUSJACENT = ""
        self.DIVIDENDE = ""
        self.TICKER = ""
        self.Site = ""
        self.inconvenient = ""
        self.EBAC = "et <BAC>"


        self.balisedeg = ""
        self.balisedeg2 = ""
        self.balisedeg3 = ""
        self.balisedeg4 = ""
        self.baliseCM = ""
        self.baliseCM22 = ""
        self.baliseCM2 = ""

        self.baliseCM3 = ""
        self.baliseCM4 = ""
        self.baliseCM5 = ""
        self.baliseCM6 = ""

        self.SV = ""
        self.PRS = ""
        self.shapes = []
        self.deleteblocs = []
        self.BLOCDIVIDENDE = ""
        self.Yahoo = []
        self.Yahoo_value = []
        self.Yahoo_value_name = []
        self.Yahoo_value_dividende = []

        self.PR1_1 = ""


        self.ABAC2 = ""
        self.type_bar2 = ""
        self.Memoire = ""
        self.Memoire2 = ""
        self.Memoire3 = ""
        self.Memoire4 = ""
        self.DDPP = ""
        self.BFP = ""
        self.PAGE = ""
        self.DDCI_M_B_Strike = ""
        self.var_degressivite()

    def var_degressivite(self):
        self.desonndr = "de son <NDR>"
        self.longuephrase = "Sinon, si le mécanisme de remboursement anticipé automatique n’a pas été activé au préalable et si, à la date de constatation finale(1), <SJR1> clôture à un <SJR3> strictement inférieur à <DBAC> mais supérieur ou égal à <PDI> de son <NDR>, l’investisseur récupère l’intégralité de son capital initialement investi."
        self.SDBAC = "strictement inférieur à <DBAC> mais "
        self.PDINSM = "mais supérieur à <PDI> de ce dernier (<NSM> dans cet exemple)"
        self.ETPDI = "et <PDI> "
        self.var_graphs()
        
    def var_graphs(self):
        self.graph1 = ""
        self.graph2 = ""
        self.graph3 = ""
        self.graph4 = ""
        self.graph5 = ""
        self.TRA_graphs()

    def TRA_graphs(self):
        #ATHENA
        self.TRA_A_S1 = "" #oui
        self.TRA_A_S2_100 = "" #oui
        self.TRA_A_S2_GAIN = "" #oui
        self.TRA_M_SJ = "" #oui
        self.TRA_F_A = "" #oui
        self.TRA_F_SJ = "" #oui
        self.TRA_MRA_Min_A = "" #oui
        self.TRA_echeance_perte_A = "" #oui
        self.BaliseCMTRA = "" #oui
        #PHOENIX
        self.TRA_D_P = "" #oui
        self.TRA_M_P = "" #oui
        self.TRA_M_PM = "" #oui
        self.TRA_GM_P = "" #oui
        self.TRA_GM_PM = "" #oui
        self.TRA_F_P = ""
        self.TRA_MRA_Min_P = "" #oui
        self.TRA_MRA_Min_PM = "" #oui
        self.TRA_TOUT_1_P = ""
        self.TRA_MRA_P = ""
        self.TRA_MED_P = ""
        self.TRA_TOUT_SAUF_P = ""
        self.TRA_TOUT_P = ""
        self.TRA_MRE_MIN_P = ""
        self.TRA_MRA_Max_P = ""


        self.TRA_MIN_P = ""
        self.TRA_MRA_MIN_P = ""
        self.TRA_MRA_MIN_PM = ""

        self.TRA_MAX_P = ""
        self.TRA_RM_P = ""
        self.TRA_EM_P = ""
        self.TRA_RM_P = ""
        self.var_style()

    def var_style(self):
        self.NOMP1 = ""
        self.NOMSOUSJACENTP1 = ""
        self.SJR6P1 = ""
        self.dates_style()

    def dates_style(self):
        self.PDC1_MAJ = ""
        self.PDC2_MAJ = ""
        self.DDR_MAJ = ""
        self.DDR1_MAJ = ""
        self.DDR1_12_MAJ = ""

        self.DEC_MAJ = ""
        self.DDCI_MAJ = ""
        self.DPCI_MAJ = ""
        self.F1_MAJ = ""
        self.ABAC2_MAJ = ""

        self.dates_boucle()


    def dates_boucle(self):
        self.Datesconstatations1 = ""
        self.Datesconstatations2 = ""
        self.Datesconstatations3 = ""
        self.Datesconstatations4 = ""
        self.Datesremb1 = ""
        self.Datesremb2 = ""
        self.Datesremb3 = ""
        self.Datesremb4 = ""
        self.Datesremb5 = ""
        self.Datesremb6 = ""
        self.Datesremb7 = ""
        self.Datesremb8 = ""
        self.Datespaiement1 = "[]"
        self.Datespaiement2 = "[]"
        self.Datespaiement3 = "[]"
        self.Datespaiement4 = "[]"
        self.Datespaiement5 = "[]"
        self.Datespaiement6 = "[]"
        self.Datespaiement7 = "[]"
        self.Datespaiement8 = "[]"

        self.dates_constat_autocall = ""
        self.dates_paiement_autocall = ""
        self.dates_constat_phoenix = ""
        self.dates_paiement_phoenix = ""
        self.dates_last_remboursement_rappel = ""

#Graph 2 blocs, si strike moyen ou best strike, afficher dans les blocs en haut la date max des constatations initiales
#niveau de référence cours de référence bloc 2