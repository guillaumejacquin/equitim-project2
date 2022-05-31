from cgitb import text
from flask import Flask
import plotly.graph_objects as go
import kaleido

# 1 #si  coupon == coupon_autocall == True, 2 blocs, (soit SANS barrière coupon)

# 2 #si coupon == coupon_Phoenix == True, 3 blocs (soit avec barrière coupon)
        ## Possibilité qu'il y ait uniquement deux bloc dans le cas ou la balise (tag) de Non-Call (1PR) == 0
        ## Sinon, NC > 0, alors toujours 3 blocs et dans le premier bloc se trouveras uniquement la barrière coupon(bleu marine)

def bloc3(Class, name, whitestrap=True):
    bloc = 3
    green = "#00B050"
    blue = "#002E8A"
    red = "#C00000"
    black = "#000000"
    text_legende = Class.SJR3 + " de <br> l'"+ Class.TDP +  " par <br> rapport à son <br>" + Class.NDR

    niveau_autocall = [-50, -50, float(Class.BAC), float(Class.ABDAC), float(Class.DBAC)] #ligne verte
    niveau_coupon = [float(Class.BCPN), float(Class.BCPN), float(Class.BCPN), float(Class.BCPN), float(Class.BCPN)] #ligne noire  niveau coupon
    niveau_capital = float(Class.PDI) #Ligne rouge
    niveau_median = niveau_coupon[0] - niveau_capital
    labels = [5, 17, 39]
    widths = [10,20,10]
    myvar = niveau_capital

    fig = go.Figure()
    
    x2=  130 - niveau_coupon[0]
    secondblock = float(Class.DBAC) - niveau_capital
    x3_3 = 130 - (niveau_capital + secondblock)
    data = {
        "x1": [niveau_coupon[0],niveau_coupon[0],niveau_capital],
        "x2": [x2,0,secondblock],
        "x3": [0,x2, x3_3],
    }

    color = {
        "x1": '#E5EBF7',
        "x2":  '#D9CD9F',
        "x3":  '#F7F4E9',
    }

    for key in data:
        fig.add_trace(
            go.Bar(
            name=key,
            y=data[key],
            x= labels,
            width=widths,
            offset=0,
            # customdata=np.transpose([labels, widths*data[key]]),
            marker_color = color[key],
            textfont_color="white",
            textposition="inside",
            textangle=0,
            showlegend= False,
            hoverinfo ='none',
        ))
    fig.update_layout(barmode="stack",uniformtext=dict(mode="hide", minsize=10),
    
    )
#axe des abcisses
#------------------------------------------NE BOUGE PAS----------------------------------------------------------------------------------------------
    fig.add_annotation( x=4.5, y=140, ax=4.5, ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')

    fig.add_annotation(x=50, y=0, ax=4.5, ay=0, xref='x', yref='y', axref='x', ayref='y', text='',
    showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')
    
    # Periode + le nombre (exempla trimestre 1 a 3)
    firstvaluexabciss = Class.F0 + Class.F0s + " 1 à " +  str(int(Class.PR1) -1)
    firstvaluexabciss = firstvaluexabciss.capitalize()

    secondvaluexabciss = Class.F0 + Class.F0s + " " +  str(int(Class.PR1))  + " à " + str(int(Class.DPRR) - 1)
    secondvaluexabciss = secondvaluexabciss.capitalize()
  
    thirdvaluexabciss = Class.F0  +" " + str(Class.DPRR)
    thirdvaluexabciss = thirdvaluexabciss.capitalize()

    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [10, 27, 44.5],
                    ticktext= [firstvaluexabciss, secondvaluexabciss, thirdvaluexabciss],
                    color="black"       

                    )

    fig.update_yaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [0],
                    ticktext= ["","", "", ""],
                    color="black"       

                    ),
    #LIGNE NOIRE
    fig.add_shape( # add a lignes premier block line
        type="line", line_color=blue, line_width=3, opacity=1, line_dash="dot",
        x0=5, x1=15, y0=niveau_coupon[0], y1=niveau_coupon[1]
    )

    fig.add_shape( # add la ligne horizontale deuxieme block line
        type="line", line_color=blue, line_width=3, opacity=1, line_dash="dot",
        x0=17, x1=37, y0=niveau_coupon[2], y1=niveau_coupon[3]
    )

    # fig.add_shape(# add la ligne horizontale troisieme block line
    #     type="line", line_color=green, line_width=3, opacity=1, line_dash="dot",
    #     x0=39, x1=49, y0=niveau_coupon[4], y1=niveau_coupon[4]
    # )
    # !LIGNE NOIRE

    #LIGNE VERTE

    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=green, line_width=3, opacity=1, line_dash="dot",
        x0=5, x1=15, y0=niveau_autocall[0], y1=niveau_autocall[1]
    )
    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=green, line_width=3, opacity=1, line_dash="dot",
        x0=17, x1=37, y0=niveau_autocall[2], y1=niveau_autocall[3]
    )

    if (Class.BCPN_is_degressif == "oui"):
        fig.add_annotation(x=48, y=niveau_autocall[4] + 3, text=str(niveau_autocall[4]) + "%", showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color=green ),align="left",
                    )
        fig.add_annotation(x=36, y=niveau_autocall[3] + 5, text=str(niveau_autocall[3]) + "%", showarrow=False,
                        font=dict( family="Proxima Nova", size=14, color=green ),align="left",
                        )
    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
            type="line", line_color=blue, line_width=3, opacity=1, line_dash="dot",
            x0=39, x1=49, y0=niveau_autocall[4], y1=niveau_autocall[4]
        )
    #!LIGNE VERTE

    #LIGNE ROUGE
    if (niveau_capital >= niveau_autocall[4] and niveau_autocall[4] > 0 or niveau_capital >= niveau_coupon[4] and niveau_coupon[4] > 0):
        niveau_capital = -5
    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=red, line_width=3, opacity=1, line_dash="dash",
        x0=39, x1=49, y0=niveau_capital, y1=niveau_capital
    )

    #!LIGNE ROUGE
    if (niveau_autocall[3] > 0):
        fig.add_trace(go.Scatter(x=[17,37,37,17],
                            y=[niveau_autocall[2],niveau_autocall[3],niveau_coupon[3],niveau_coupon[2]],
                            fill='toself',
                            fillcolor='#D9CD9F',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',
))

    #ici on remplace les valeurs x (ecrites abcisses(ne plus avoir 10 20 30 40 mais trimestre1 etc))
    #ajout des petites lignes nulles #LES TICK SES FDP
    x0 = 4
    x1 = x0+0.5
    fig.add_shape(type="line",
    x0=x0, y0=niveau_autocall[2], x1=x1, y1=niveau_autocall[2],
    line=dict(color=green,width=3))

    fig.add_shape(type="line",
    x0=x0, y0=niveau_coupon[-1], x1=x1, y1=niveau_coupon[-1],
    line=dict(color=blue,width=3))

    fig.add_shape(type="line",
    x0=x0, y0=niveau_capital, x1=x1, y1=niveau_capital,
    line=dict(color="#C00000",width=3))
#------------------------------------------NE BOUGE PAS---------------------------------------------------------------------------------------------

#-------------------------------------Pas fini, doit gerer les 100% ----------------------------------------------------
    #NIVEAU de reference seulement si 100 % sinon creer bloc 90%(classique) et au dessu sniveau de reference100% (en noir)

    #les valeurs qu on va mettre
    mystring = "100%"

    fig.add_annotation(x=2.0, y=130, text= text_legende, showarrow=False, font=dict(family="Proxima Nova", size=12, color=black ),
                    )

    if (niveau_autocall[2] != 100):
        fig.add_annotation(x=3.0, y=niveau_autocall[2], text= str(niveau_autocall[2]) +"%", showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color=green ))
    else:
        mystring = str(Class.BAC) + "%"
        fig.add_annotation(x=3, y=str(Class.BAC),text= (mystring), showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color=green ),
                    )

    fig.add_annotation(x=3.0, y=niveau_coupon[-1], text= str(niveau_coupon[-1]) +"%", showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color=blue ),
                    )
    fig.add_annotation(x=3.0, y=niveau_capital,text= str(niveau_capital) +"%", showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color="red" ),
                    )
   
#-------------------------------------!Pas fini, doit gerer les 100%! ----------------------------------------------------

    #le premier parametre de range x, permet de mettre ou non un blanc entre le 0 et le premier bloc
    fig.update_xaxes(range=[0,61])
    fig.update_yaxes(range=[-3,130])

    #enlever le fond blanc
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        })
    if (whitestrap == True):
            fig.add_trace(go.Scatter(x=[5,15,15,5], 
                                    y=[niveau_autocall[0] +1 ,niveau_autocall[1] + 1, niveau_autocall[1] -1, niveau_autocall[0] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

            fig.add_trace(go.Scatter(x=[17,37,37,17], 
                                    y=[niveau_autocall[2] +1 ,niveau_autocall[3] + 1, niveau_autocall[3] -1, niveau_autocall[2] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

            fig.add_trace(go.Scatter(x=[39,49,49,39], 
                                    y=[niveau_autocall[4] +1 ,niveau_autocall[4] + 1, niveau_autocall[4] -1, niveau_autocall[4] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))
                            
            fig.add_trace(go.Scatter(x=[39,49,49,39], 
                                    y=[niveau_capital +1 ,niveau_capital + 1, niveau_capital -1, niveau_capital -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

            fig.add_trace(go.Scatter(x=[5,15,15,5], 
                                    y=[niveau_coupon[0] +1 ,niveau_coupon[1] + 1, niveau_coupon[1] -1, niveau_coupon[0] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

            fig.add_trace(go.Scatter(x=[17,37,37,17], 
                                    y=[niveau_coupon[2] +1 ,niveau_coupon[3] + 1, niveau_coupon[3] -1, niveau_coupon[2] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))
            
            fig.add_trace(go.Scatter(x=[39,49,49,39], 
                                    y=[niveau_coupon[4] +1 ,niveau_coupon[4] + 1, niveau_coupon[4] -1, niveau_coupon[4] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

                                    
    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=green, line_width=3, opacity=1, line_dash="dot",
        x0=5, x1=15, y0=niveau_autocall[0], y1=niveau_autocall[1]
    )

    texta = "<b>Le produit continue </b>:<br><br> Aucun coupon n'est versé, il <br> est mis en mémoire"
    fig.add_annotation(
        x=(10),
        y=(niveau_coupon[0] - (niveau_coupon[0]/2) + 10),
        text=texta,
        showarrow=False,
        font=dict(color=black, size=12)
    )
    cpn = ("{:.2f}".format(float(Class.CPN)))
    cpn = cpn.replace(".", ",")

 
    gce = ("{:.2f}".format(float(Class.GCE)))
    gce = gce.replace(".", ",")


    mystring = "<b>Le produit continue </b>:<br><br>  Un coupon de " + cpn + "% <br> + <br> Les éventuels coupons mémorisés <br> au préalable"
    fig.add_annotation(
        x=(10),
        y=(niveau_coupon[0] + (130-niveau_coupon[0]) /2),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=12),
        
    )

    mystring = "<b>Le produit continue </b>:<br><br> Aucun coupon versé, il est mis en mémoire"
    fig.add_annotation(
        x=(28),
        y=(niveau_autocall[3] /2),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=12)
    )
   

    mystring = "<b>Le produit continue </b>:<br><br>Aucun coupon n'est versé, il est mis en mémoire"
    fig.add_annotation(
        x=(28),
        y=niveau_autocall[1]/2,
        text=mystring,
        showarrow=False,
        font=dict(color=black,size=12)
    )
  
    mystring = "<b>Remboursement à l'échéance(1)</b> :<br><br>Le capital initial diminué de <br> l'intégralité de la baisse enregistrée <br> par l'indice entre <br> la date de constatation initiale <br> et la date de constatation finale"
    mystring = mystring.replace("(1)", "⁽¹⁾")

    if (niveau_capital < 0 ):
        y = float(Class.DBAC)
    else:
        y = niveau_capital
    fig.add_annotation(
        x=(44),
        y= y/2,
        text=mystring,
        showarrow=False,
        font=dict(color=black,size=12)
    )
    
    if (niveau_capital <= 0):
        mystring= " "
    else:
        mystring = "<b>Remboursement à l'échéance:(1)</b> :<br><br>L'intégralité du capital initial "
        mystring = mystring.replace("(1)", "⁽¹⁾")

    if (float(Class.DBAC) - niveau_capital < 10 or  niveau_capital < 0):
        mystring = "<b>Remboursement à l'échéance(1)</b> :<br><br>L'intégralité du capital initial"
        mystring = mystring.replace("(1)", "⁽¹⁾")

        fig.add_annotation(
        x=(55),
        y=(30),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=12)
    )
        y_arrow =abs(float(myvar - (myvar  - float(Class.DBAC))))
        fig.add_annotation(
            x=44,  # arrows' head
            ay=31.5,  # arrows' head
            ax=49.6,  # arrows' tail
            y=y_arrow - (float(Class.DBAC) - niveau_capital)/2,  # arrows' tail
            xref='x',
            yref='y',
            axref='x',
            ayref='y',
            text='',  # if you want only the arrow
            showarrow=True,
            arrowhead=3,
            arrowsize=1,
            arrowwidth=1,
            arrowcolor='black'
        )
    else:
        fig.add_annotation(
        x=(44.5),
        y= float(Class.DBAC) - (float(Class.DBAC) - niveau_capital)/2,
        text=mystring,
        showarrow=False,
        font=dict(color=black,size=12)
    )
    mystring = "<b>Remboursement anticipé automatique(1) :</b><br><br>L'intégralité du capital initial <br> + <br> Un coupon de " + str(cpn) + " % <br> + <br> Les éventuels coupons mémorisés au préalable"
    mystring = mystring.replace("(1)", "⁽¹⁾")

    fig.add_annotation(
        x=(28),
        y= 130 - (130 - niveau_autocall[2])/2,
        text=mystring,
        showarrow=False,
        font=dict(color=black,size=12)
    )
    if (niveau_autocall[3] != niveau_autocall[2]):
        x = 23
    else:
        x= 28

    mystring = "<b>Le produit continue :</b> <br><br>Un coupon de " + str(cpn) + "% est versé <br> + <br> Les éventuels coupons mémorisés au préalable "
    fig.add_annotation(
            x=(x),
            y= niveau_autocall[2] - (niveau_autocall[2] - niveau_coupon[0])/2,
            text=mystring,
            showarrow=False,
            font=dict(color=black,size=10),
            # align="left"
        )
        
    
    mystring = "<b>Remboursement à l'échéance(1)</b> :<br><br>L'intégralité du capital initial <br> + <br> Un coupon de " + str(cpn) + " % <br> + <br>Les éventuels coupons <br> mémorisés au préalable <br>"
    mystring = mystring.replace("(1)", "⁽¹⁾")

    fig.add_annotation(
        x=(44),
        y= 130 - (130 - niveau_autocall[4])/2,
        text=mystring,
        showarrow=False,
        font=dict(color=black,size=12)
    )


    fig.add_shape(type="line",
    x0=50.5, y0=116, x1=60, y1=116,
    line=dict(color=green,width=3),  line_dash="dot")
    fig.add_annotation(x=55, y=102.5,text= ("Seuil d'activation du <br> mécanisme de <br> remboursement anticipé <br> automatique à partir de la fin du <br>" + Class.F0 +" " + str(int(Class.PR1)) + " jusqu'à la fin du " + str(Class.F0) +"<br> " + str(int(Class.DPRR)-1) ), showarrow=False,
                    font=dict(family="Proxima Nova", size=13, color=black ), align="left"
                    )


    fig.add_shape(type="line",
    x0=50.5, y0=77, x1=60, y1=77,
    line=dict(color=blue,width=3),  line_dash="dot")
    fig.add_annotation(x=55, y=71.5,text= ("Seuil de détachement des coupons"), showarrow=False,
                    font=dict(family="Proxima Nova", size=13, color=black ), align="left"
                    )



    fig.add_shape(type="line",
    x0=51, y0=50, x1=60, y1=50,
    line=dict(color=red,width=3), line_dash="dash")
    
    if ((niveau_capital) <= -2):
        fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=red, line_width=2, opacity=1, line_dash="dash",
        x0=39, x1=49, y0=float(Class.DBAC) - 1, y1=float(Class.DBAC) -1
    )

    fig.add_annotation(x=54, y=45,text= ("Seuil de perte en capital <br> à l'échéance"), showarrow=False,
                    font=dict(family="Proxima Nova", size=13, color=black ), align="left",
                    )
    
    fig.update_layout(
                            legend=dict(
                                itemclick="toggleothers",
                                itemdoubleclick="toggle"),
                            autosize=True,
                            width=1400,#1400
                            height=675,#800
                            plot_bgcolor='rgb(255,255,255)',
                            margin=dict(
                                l=50,
                                r=0,
                                b=20,
                                t=50,
                                pad=0),
                            paper_bgcolor='white')



    fig.write_image(name, format="png", scale=2, engine='kaleido')
    # fig.show()


    return(fig)


#page 2 voir de l indice espace