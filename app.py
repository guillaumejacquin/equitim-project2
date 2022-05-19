
from flask import Flask
from flask import render_template, url_for, request
import sys
from main import *
from flask_cors import CORS
from flask import jsonify


sys.path.append("../")
from app import *
app = Flask(__name__)
CORS(app)




@app.route("/add", methods=["POST"])
def add_articles():
    Myclass = InformationsForm()

    data = request.json
    Myclass.template = data["template"]
    Myclass.Nom = data["Nom"]
    Myclass.Typologie = data["Typologie"]
    Myclass.Droit = data["Droit"]
    Myclass.Isin = data["Isin"]
    


    #probleme de date, je coupe pour que ca enelever la merde apres 
    emission = data["Emission"]
    Myclass.Emission = emission[0:10]

    dci = data["DCI"]
    Myclass.DCI = dci
    

    dr1 = data["DR1"]
    Myclass.DR1 = dr1[0:10]
    
    Myclass.DPR = data["DPR"]

    dadr = data["DADR"]
    Myclass.DADR = dadr[0:10]
    
    dcf = data["DCF"]
    Myclass.DCF = dcf[0:10]

    dec = data["DEC"]
    Myclass.DEC = dec[0:10]

    Myclass.ADCF = data["ADCF"]
    Myclass.F0 = data["F0"]
    TSJ = data["TSJ"]
    Myclass.TSJ = list(TSJ.split(", "))


    Myclass.CPN = data["CPN"]
    Myclass.CPN_is_memoire = data["CPN_is_memoire"]
    Myclass.PDI = data["PDI"]
    Myclass.BAC = data["BAC"]
    Myclass.BAC_is_degressif = data["BAC_is_degressif"]
    Myclass.BCPN = data["BCPN"]
    Myclass.BCPN_is_degressif = data["BCPN_is_degressif"]

    Myclass.COM = data["COM"]
    Myclass.NSD = data["NSD"]
    Myclass.NSM = data["NSM"]
    Myclass.NSF = data["NSF"]
    Myclass.ABDAC = data["ABDAC"]
    Myclass.DBAC = data["DBAC"]
    Myclass.DEG = data["DEG"]
    Myclass.type_strike = data["type_strike"]
    Myclass.type_bar = data["type_bar"]
    Myclass.sous_jacent = data["sous_jacent"]
    Myclass.NJO = data["NJO"]

    ddp = data["DDP"]
    if (ddp == None):
        Myclass.DDP = "error"

    else: 
        Myclass.DDP = ddp[0:10]
    Myclass.type_bar2 = data["type_bar2"]

    # Myclass.DCF = "2027-07-14"
    print("AHHHHHHHHHHHHHHHHHHHHHHHHHH", "Emission = ", Myclass.Emission, "DATE PREMIER remboursement = ", Myclass.DPR, "DATE PREMIER RAPPEL", Myclass.DR1, "Date d'avant dernier remboursement ", Myclass.DADR, "DATE de constatation finale", Myclass.DCF,"Date d'échéance",  Myclass.DEC, "Avant derniere date de constatation finale", Myclass.ADCF)

    resultmain = main(Myclass)  
    if resultmain == 0:
        return jsonify("True")
    else:
        return jsonify("False")
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
