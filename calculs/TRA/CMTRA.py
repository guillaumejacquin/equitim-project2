def BaliseCMTRA(Class):
    if(Class.type_bar == "degressif" or (Class.type_bar == "airbag" and float(Class.DBAC) == float(Class.PDI))):
        Class.BaliseCMTRA = "<TRA.MG.A>"
    else:  
        Class.BaliseCMTRA = "<TRA.M.A>"

