
def SV(Class):
    if Class.type_bar == "degressif" or Class.type_bar == "airbag":
        Class.SV = "<DBAC>"

    else:
        Class.SV = "<BAC>"


