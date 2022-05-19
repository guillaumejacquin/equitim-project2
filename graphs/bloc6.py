from cgitb import text
from flask import Flask
import plotly.graph_objects as go
import kaleido

#legende en haut a droite
def legende(Class, fig, green, black, blue, red, niveau_capital):
    fig.add_shape(type="line",
    x0=74, y0=116, x1=83, y1=116,
    line=dict(color=green,width=3),  line_dash="dot")
    fig.add_annotation(x=80.5, y=102.5,text= ("Seuil d'activation du <br> mécanisme de <br> remboursement anticipé <br> automatique à partir de la fin du <br>" + Class.F0 +" " + str(int(Class.PR1)) + " jusqu'à la fin du " + str(Class.F0) +"<br> " + str(int(Class.DPRR)-1) ), showarrow=False,
                    font=dict(family="Proxima Nova", size=12, color=black ), align="left"
                    )
    fig.add_shape(type="line",
    x0=75, y0=77, x1=83, y1=77,
    line=dict(color=blue,width=3),  line_dash="dot")
    fig.add_annotation(x=80.5, y=71.5,text= ("Seuil de détachement des coupons"), showarrow=False,
                    font=dict(family="Proxima Nova", size=12, color=black ), align="left"
                    )
    fig.add_shape(type="line",
    x0=75, y0=50, x1=83, y1=50,
    line=dict(color=red,width=3), line_dash="dash")

    fig.add_annotation(x=79, y=45,text= ("Seuil de perte en capital <br> à l'échéance"), showarrow=False,
                    font=dict(family="Proxima Nova", size=12, color=black ), align="left",
                    )
    return fig

#Laxe abcisse ordonnée, parametrage visuel
def abcisse_ordonnee(Class, fig, niveau_autocall, niveau_coupon,niveau_capital, green, blue):
    fig.add_annotation( x=4.5, y=140, ax=4.5, ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')

    fig.add_annotation(x=75, y=0, ax=4.5, ay=0, xref='x', yref='y', axref='x', ayref='y', text='',
    showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')
    
    # Periode + le nombre (exempla trimestre 1 a 3)
    if (int(Class.PR1) != 2):
        firstvaluexabciss = Class.F0 + Class.F0s + " 1 à " +  str(int(Class.PR1) - 1)
    else:
        firstvaluexabciss = Class.F0 + " 1"

    firstvaluexabciss = firstvaluexabciss.capitalize()
    croisement =  int(float(Class.BAC) - float(Class.BCPN) +1)
    secondvaluexabciss = Class.F0 + Class.F0s + " " +  str(int(Class.PR1))  + " à " + str(croisement)
    secondvaluexabciss = secondvaluexabciss.capitalize()
    
    third_value = Class.F0 + Class.F0s + " " +  str(croisement + 1)  + " à " + str(int(Class.DPRR) - 1)
    third_value = third_value.capitalize()

    lastvalue = Class.F0  + " " + str(Class.DPRR)
    lastvalue = lastvalue.capitalize()

    
    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [12, 29, 46, 65],
                    ticktext= [firstvaluexabciss, secondvaluexabciss, third_value, lastvalue],
                    color="black")

    fig.update_yaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [0],
                    ticktext= ["","", "", ""],
                    ),


    mystring = "100%"
    if (niveau_autocall[2] != 100):

   
        fig.add_annotation(x=2.5, y=niveau_autocall[2], text= str(niveau_autocall[2]) +"%", showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color=green ))
    else:
        mystring = str(Class.BAC) + "%"
        fig.add_annotation(x=3, y=str(Class.BAC),text= (mystring), showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color=green ),
                    )

    fig.add_annotation(x=2.5, y=niveau_coupon[-1], text= str(niveau_coupon[-1]) +"%", showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color=blue ),
                    )
    fig.add_annotation(x=2.5, y=niveau_capital,text= str(niveau_capital) +"%", showarrow=False,
                    font=dict(family="Proxima Nova", size=14, color="red" ),
                    )

    
    #le premier parametre de range x, permet de mettre ou non un blanc entre le 0 et le premier bloc
    fig.update_xaxes(range=[0,88])
    fig.update_yaxes(range=[-3,130])
    
    return(fig)


#le bloc le plus a gauche
def firstbloc_text(Class, fig, niveau_coupon, niveau_autocall, black):
    cpn = ("{:.2f}".format(float(Class.CPN)))
    cpn = cpn.replace(".", ",")

    gce = ("{:.2f}".format(float(Class.GCE)))
    gce = gce.replace(".", ",")

    mystring = "<b>Le produit continue </b>:<br><br>  Un coupon de " + cpn + "% <br> + <br> Les éventuels coupons mémorisés <br> au préalable"
    fig.add_annotation(
        x=(12.5),
        y=(niveau_coupon[1] + (130-niveau_coupon[0]) /2),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=10),
    )

    mystring = "<b>Le produit continue </b>:<br><br> Aucun coupon versé, il est mis en mémoire"
    fig.add_annotation(
        x=(12.5),
        y=(niveau_coupon[1] /2),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=10)
    )
    
def second_bloc_text(Class, fig, niveau_coupon, niveau_autocall, black):
    mystring = "<b>Le produit continue </b>:<br><br> Aucun coupon versé, il est mis en mémoire"
    fig.add_annotation(
        x=(29.5),
        y=(niveau_coupon[1] /2),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=10)
    )
 
    cpn = ("{:.2f}".format(float(Class.CPN)))
    cpn = cpn.replace(".", ",")
    gce = ("{:.2f}".format(float(Class.GCE)))
    gce = gce.replace(".", ",")
    mystring = "<b>Remboursement anticipé automatique(1) :</b><br><br>L'intégralité du capital initial <br> + <br> Un coupon de " + str(cpn) + " % <br> + <br> Les éventuels coupons mémorisés au préalable"
    mystring = mystring.replace("(1)", "⁽¹⁾")

    fig.add_annotation(
        x=(29.5),
        y= 130 - (130 - float(Class.BAC))/2,
        text=mystring,
        showarrow=False,
        font=dict(color=black,size=9)
    )

    mystring = "<b>Le produit continue :</b> <br><br> Un coupon de " + str(cpn) + "% est versé <br> + <br> Les éventuels coupons mémorisés au préalable "
    fig.add_annotation(
            x=(26.75),
            y= niveau_autocall[2] - (niveau_autocall[2] - niveau_coupon[0])/2,
            text=mystring,
            showarrow=False,
            font=dict(color=black,size=6),
            # align="left"
        )

def third_bloc_text(Class, fig, niveau_coupon, niveau_autocall, black):
    mystring = "<b>Le produit continue </b>:<br><br> Aucun coupon versé, il est mis en mémoire"
    fig.add_annotation(
        x=(46.5),
        y=(niveau_coupon[3] /2),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=10)
    )

    cpn = ("{:.2f}".format(float(Class.CPN)))
    cpn = cpn.replace(".", ",")
    gce = ("{:.2f}".format(float(Class.GCE)))
    gce = gce.replace(".", ",")
    mystring = "<b>Remboursement anticipé automatique(1) :</b><br><br>L'intégralité du capital initial <br> + <br> Un coupon de " + str(cpn) + " % <br> + <br> Les éventuels coupons mémorisés au préalable"
    mystring = mystring.replace("(1)", "⁽¹⁾")
    
    fig.add_annotation(
        x=(46.5),
        y= 130 - (130 - float(Class.BAC))/2,
        text=mystring,
        showarrow=False,
        font=dict(color=black,size=9)
    )
    

def last_bloc_text(Class, fig, niveau_coupon, niveau_autocall, black, niveau_capital):
    mystring = "<b>Remboursement à l'échéance(1)</b> :<br><br>Le capital initial diminué de <br> l'intégralité de la baisse enregistrée <br> par l'indice entre <br> la date de constatation initiale <br> et la date de constatation finale"
    mystring = mystring.replace("(1)", "⁽¹⁾")

    cpn = ("{:.2f}".format(float(Class.CPN)))
    cpn = cpn.replace(".", ",")
    gce = ("{:.2f}".format(float(Class.GCE)))
    gce = gce.replace(".", ",")

    fig.add_annotation(
        x=(65.5),
        y=(float(Class.PDI) /2),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=10)
    )

    mystring = "<b>Remboursement à l'échéance(1)</b> :<br><br>L'intégralité du capital initial <br> + <br> Un coupon de " + cpn + "% est versé<br> + <br> Les éventuels coupons <br> mémorisés au préalable"
    mystring = mystring.replace("(1)", "⁽¹⁾")
    y = niveau_capital
    fig.add_annotation(
        x=(65.5),
        y=(float(Class.ABDAC) + (130-float(Class.ABDAC)) /2),
        text=mystring,
        showarrow=False,
        font=dict(color=black,size=10)
    )
    mystring = "<b>Remboursement à l'échéance(1)</b> :<br><br>L'intégralité du capital initial "
    mystring = mystring.replace("(1)", "⁽¹⁾")

    fig.add_annotation(
        x=(65.5),
        y= float(Class.DBAC) - (float(Class.DBAC) - niveau_capital)/2,
        text=mystring,
        showarrow=False,
        font=dict(color=black,size=10)
    )


def first_bloc(Class, fig, blue, niveau_coupon):
    fig.add_shape( # add la ligne horizontale deuxieme block line
        type="line", line_color=blue, line_width=3, opacity=1, line_dash="dot",
        x0=5, x1=20,  y0=niveau_coupon[0], y1=niveau_coupon[1]
    )
    fig.add_trace(go.Scatter(x=[5, 20, 20, 5], 
                                    y=[niveau_coupon[0] +1 ,niveau_coupon[1] + 1, niveau_coupon[1] -1, niveau_coupon[0] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

    return(fig)


def second_block(Class, fig, niveau_coupon, blue, green):
    fig.add_trace(go.Scatter(x=[22,37,37,22],
                            y=[float(Class.BAC),float(Class.BCPN),float(Class.BCPN),float(Class.BCPN)],
                            fill='toself',
                            fillcolor='#D9CD9F',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',

    ))
    fig.add_trace(go.Scatter(x=[22,37,37,22], 
                                    y=[float(Class.BAC) +1 ,float(Class.BCPN) +1 ,float(Class.BCPN) -1,float(Class.BAC) -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

    fig.add_trace(go.Scatter(x=[22,37,37,22], 
                                    y=[niveau_coupon[2] +1 ,niveau_coupon[3] + 1, niveau_coupon[3] -1, niveau_coupon[2] -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

    fig.add_shape( # add la ligne horizontale deuxieme block line
        type="line", line_color=blue, line_width=3, opacity=1, line_dash="dot",
        x0=22, x1=37,  y0=niveau_coupon[2], y1=niveau_coupon[3]
    )
    
    fig.add_shape( # add la ligne horizontale deuxieme block line
        type="line", line_color=green, line_width=3, opacity=1, line_dash="dot",
        x0=22, x1=37,  y0=float(Class.BAC), y1=float(Class.BCPN)
    )
    return(fig)


def third_block(Class, fig, blue):
    fig.add_trace(go.Scatter(x=[39,54,54,39],
                            y=[ float(Class.ABDAC),  float(Class.DBAC), 0, 0],
                            fill='toself',
                            fillcolor='#E5EBF7',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',
    ))

    fig.add_trace(go.Scatter(x=[39,54,54,39],
                            y=[ Class.BCPN,  float(Class.DBAC), float(Class.DBAC), float(Class.DBAC)],
                            fill='toself',
                            fillcolor='#E5EBF7',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',
))

    fig.add_trace(go.Scatter(x=[39,54,54,39], 
                                    y=[float(Class.BCPN) +1 ,float(Class.ABDAC) +1 ,float(Class.ABDAC) -1,float(Class.BCPN) -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))
    fig.add_shape( # add la ligne horizontale deuxieme block line
        type="line", line_color=blue, line_width=3, opacity=1, line_dash="dot",
        x0=39, x1=54, y0=float(Class.BCPN), y1=float(Class.ABDAC)
    )

def lastblock(Class, fig, green, red, blue):
    fig.add_trace(go.Scatter(x=[58,73,73,58], 
                                    y=[float(Class.DBAC) +1 , float(Class.DBAC) + 1, float(Class.DBAC) -1, float(Class.DBAC) -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

    fig.add_shape( # add la ligne horizontale deuxieme block line
        type="line", line_color=blue, line_width=3, opacity=1, line_dash="dot",
        x0=58, x1=73, y0=float(Class.DBAC), y1=float(Class.DBAC)
    )
    #Class.PDI

    fig.add_trace(go.Scatter(x=[58,73,73,58], 
                                    y=[float(Class.PDI) +1 , float(Class.PDI) + 1, float(Class.PDI) -1, float(Class.PDI) -1],
                                    fill='toself',
                                    fillcolor='white',
                                    line=dict(width=0),
                                    showlegend=False,
                                    mode='lines',  
                                    hoverinfo ='none',))

    fig.add_shape( # add la ligne horizontale deuxieme block line
        type="line", line_color=red, line_width=3, opacity=1, line_dash="dash",
        x0=58, x1=73, y0=float(Class.PDI), y1=float(Class.PDI)
    )

def bloc3_4(Class, name, whitestrap=False):
    bloc = 3
    green = "#00B050"
    blue = "#002E8A"
    red = "#C00000"
    black = "#000000"
    niveau_autocall = [-50, -50, float(Class.BAC), float(Class.ABDAC), float(Class.DBAC)] #ligne verte
    niveau_coupon = [float(Class.BCPN), float(Class.BCPN), float(Class.BCPN), float(Class.BCPN), float(Class.BCPN)] #ligne noire  niveau coupon
    niveau_capital = float(Class.PDI) #Ligne rouge
    niveau_median = niveau_coupon[0] - niveau_capital
    labels = [5, 22, 39, 58]
    widths = [15,15, 15, 15]
    myvar = niveau_capital

    fig = go.Figure()
    
  
    x2=  130 - niveau_coupon[0]
    secondblock = float(Class.DBAC) - niveau_capital
    x3_3 = 130 - (niveau_capital + secondblock)
    data = {
        "x1": [niveau_coupon[0],niveau_coupon[0],niveau_capital, niveau_capital],
        "x2": [x2,0,secondblock, secondblock],
        "x3": [0,x2, x3_3, x3_3],
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
#-

    abcisse_ordonnee(Class, fig, niveau_autocall, niveau_coupon,niveau_capital, green, blue)
    
    #ici on remplace les valeurs x (ecrites abcisses(ne plus avoir 10 20 30 40 mais trimestre1 etc))
        # ajout des petites lignes nulles #LES TICK SES FDP
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
    # if (niveau_autocall[2] != 100):
    #     fig.add_annotation(x=3, y=niveau_coupon[0],text= (niveau_coupon[0]), showarrow=False,
    #                 font=dict(family="Proxima Nova", size=14, color=green ),
    #                 )
   
    #     # fig.add_annotation(x=2.5, y=niveau_autocall[2], text= str(niveau_autocall[2]) +"%", showarrow=False,
    #     #             font=dict(family="Proxima Nova", size=14, color=green ))
    # else:
    #     mystring = str(Class.BAC) + "%"
    #     fig.add_annotation(x=3, y=str(Class.BAC),text= (mystring), showarrow=False,
    #                 font=dict(family="Proxima Nova", size=14, color=green ),
    #                 )

    # fig.add_annotation(x=2.5, y=niveau_coupon[-1], text= str(niveau_coupon[-1]) +"%", showarrow=False,
    #                 font=dict(family="Proxima Nova", size=14, color=blue ),
    #                 )
    # fig.add_annotation(x=2.5, y=niveau_capital,text= str(niveau_capital) +"%", showarrow=False,
    #                 font=dict(family="Proxima Nova", size=14, color="red" ),
    #                 )
   
#-------------------------------------!Pas fini, doit gerer les 100%! ----------------------------------------------------



    if ((niveau_capital) <= -2):
        fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=red, line_width=2, opacity=1, line_dash="dash",
        x0=39, x1=49, y0=float(Class.DBAC) - 1, y1=float(Class.DBAC) -1
    )


    first_bloc(Class, fig, blue, niveau_coupon)
    firstbloc_text(Class, fig, niveau_coupon,niveau_autocall,  black)
    second_bloc_text(Class, fig, niveau_coupon, niveau_autocall, black)

    second_block(Class, fig, niveau_coupon, blue, green)
    third_block(Class, fig, blue)
    third_bloc_text(Class, fig,niveau_coupon, blue, black)
    last_bloc_text(Class, fig,niveau_coupon, blue, black, niveau_capital)
    lastblock(Class, fig, green, red, blue)

#     fig.add_trace(go.Scatter(x=[39,54,54,39],
#                             y=[float(Class.BCPN),float(Class.BCPN),float(Class.BCPN),float(Class.BCPN)],
#                             fill='toself',
#                             fillcolor='#D9CD9F',
#                             line=dict(width=0),
#                             showlegend=False,
#                             mode='lines',  
#                             hoverinfo ='none',
# ))



    legende(Class, fig, green, black, blue, red, niveau_capital)



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
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        })
  
    fig.write_image(name, format="png", scale=2, engine='kaleido')
    # fig.show()

    return(fig)

