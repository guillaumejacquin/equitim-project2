from cgitb import text
from optparse import Values
import plotly.graph_objects as go
import kaleido


#on arrive au bloc des deux graphs , j'ignorais encore qu'on pouvait des fonctions (j'avais eu un bug), bonne chance pour la lecture
def bloc2(Class, name, whitestrap=False):
    text_legende = Class.SJR3 + " de <br> l'"+ Class.TDP +  " par <br> rapport à son <br>" + Class.NDR
   
   #valeurs des x_tickers
    secondvaluexabciss = Class.F0 + Class.F0s + " " + str(int(Class.PR1))  + " à " + str(int(Class.DPRR) - 1)
    secondvaluexabciss = secondvaluexabciss.capitalize()
    thirdvaluexabciss = Class.F0  +" " + str(Class.DPRR)
    thirdvaluexabciss = thirdvaluexabciss.capitalize()
    gce = ("{:.2f}".format(Class.GCE))

    #les couleurs
    green = "#00B050"
    blue = "#002E8A"
    red = "#C00000"
    black = "#000000"
    #Variables des courbes
    x0 = 4
    x1 = x0+0.5

    #les barrières, en tableau pour une raison de simplicité
    niveau_autocall = [float(Class.BAC), float(Class.ABDAC), float(Class.DBAC)] #ligne verte
    niveau_coupon = [float(Class.BCPN), float(Class.BCPN), float(Class.BCPN)] #ligne noire  niveau coupon
    niveau_capital = float(Class.PDI) #Ligne rouge
    niveau_median = niveau_coupon[0] - niveau_capital

   
    #:
    # !Variables des courbes

#Size des blocs (positions + taille)
    labels = [5, 27]
    widths = [20,10]
#Size des blocs (positions + taille)

    fig = go.Figure()
    
    data = {
        "x1": [niveau_coupon[0],niveau_coupon[0],niveau_capital],
        "x2": [niveau_coupon[0],0,niveau_median],
        "x3": [0,niveau_coupon[0],niveau_coupon[0]],
    }
    color = {
        "x1": '#E5EBF7',
        "x2":  '#D9CD9F',
        "x3":  '#F7F4E9',
    }

    #la boucle du dictionnaire data (avec color) pour tracer les blocs
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
     text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black',align="left")
    
    fig.add_annotation(x=38, y=0, ax=4.25, ay=0, xref='x', yref='y', axref='x', ayref='y', text='',
    showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black',align="left")
    #LES ARROWS, 


    fig.update_xaxes(tickangle=0,
                    tickmode = 'array',
                    tickvals = [14, 31.5],
                    ticktext= [secondvaluexabciss, thirdvaluexabciss], #ajouter les variables des x des deux blocs
                    tickfont_size = 12,
                    color="black"       
                    )

    fig.update_yaxes(tickangle=0,
                    tickmode = 'array', #les y variables
                    tickvals = [0],
                    ticktext= ["","", "", ""],
                    ),

#     #LIGNE VERTE


    fig.add_trace(go.Scatter(x=[5,25,25,5],
                            y=[130 ,130 ,niveau_autocall[1],niveau_autocall[0]],
                            fill='toself',
                            fillcolor='#D9CD9F',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',))
                            

    fig.add_annotation(x=24, y=niveau_autocall[1] + 5,text=str(niveau_autocall[1]) + "%", showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color=green ),align="left",
                    )
           
    fig.add_annotation(x=36, y=niveau_autocall[2] + 3,text=str(niveau_autocall[2]) + "%", showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color=green ),align="left",
                    )         
    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=green, line_width=3, opacity=1, line_dash="dot",
        x0=5, x1=25, y0=niveau_autocall[0], y1=niveau_autocall[1]
    )

    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=green, line_width=3, opacity=1, line_dash="dot",
        x0=27, x1=37, y0=niveau_autocall[2], y1=niveau_autocall[2]
    )
#     #!LIGNE VERTE
    #LIGNE ROUGE
    if (niveau_capital >= niveau_autocall[2] and niveau_autocall[2] > 0 or niveau_capital >= niveau_coupon[2] and niveau_coupon[2] > 0):
        niveau_capital = -5
    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color="#C00000", line_width=2, opacity=1, line_dash="dash",
        x0=27, x1=37, y0=niveau_capital, y1=niveau_capital
    )


    if ((niveau_capital) <= -2):
        fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=red, line_width=2, opacity=1, line_dash="dash",
        x0=27, x1=37, y0=float(Class.DBAC) - 1, y1=float(Class.DBAC) -1
    )
#     #!LIGNE ROUGE

    if (niveau_autocall[1] > 0):
        fig.add_trace(go.Scatter(x=[5,25,25,5],
                            y=[niveau_autocall[0],niveau_autocall[1], 0, 0],
                            fill='toself',
                            fillcolor='#E5EBF7',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',
))
    #if (niveau_autocall[2] - niveau_capital >= 10 and niveau_capital >0):
    fig.add_trace(go.Scatter(x=[27,37,37,27], 
                                y=[niveau_autocall[2],niveau_autocall[2], niveau_capital, niveau_capital],
                                fill='toself',
                                fillcolor='#D9CD9F',
                                line=dict(width=0),
                                showlegend=False,
                                mode='lines',  
                                hoverinfo ='none',))
#niveau_autocall[2] niveau capital


#     #ici on remplace les valeurs x (ecrites abcisses(ne plus avoir 10 20 30 40 mais trimestre1 etc))
#         # ajout des petites lignes nulles

    fig.add_shape(type="line",
    x0=x0, y0=niveau_autocall[0], x1=x1, y1=niveau_autocall[0],
    line=dict(color=green,width=3))

    fig.add_shape(type="line",
    x0=x0, y0=niveau_capital, x1=x1, y1=niveau_capital,
    line=dict(color="#C00000",width=3))
# #------------------------------------------NE BOUGE PAS---------------------------------------------------------------------------------------------


# #-------------------------------------Pas fini, doit gerer les 100% ----------------------------------------------------
#     #NIVEAU de reference seulement si 100 % sinon creer bloc 90%(classique) et au dessu sniveau de reference100% (en noir)

#     #les valeurs qu on va mettre
    mystring =  "100%"

    #si le niveau_autocall est différent de 100 , dessiner les options
    if (niveau_autocall[0] != 100):
        fig.add_annotation(x=3, y=100,text= (mystring), showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color=black ),align="center",
                    )
        
        fig.add_shape(type="line",
            x0=4, y0=100, x1=4.5, y1=100,
            line=dict(color=black, width=3))


    
        fig.add_annotation(x=3.0, y=niveau_autocall[0], text= str(niveau_autocall[0]) +"%", showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color=green ),align="left")
    else:
        #si le niveau_autocall est égal à 100 , dessiner les options

        mystring = str(niveau_autocall[0]) + "%"
        fig.add_annotation(x=2.25, y=100 ,text= (mystring), showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color=green ),align="left",
                    )

    mystring = Class.SJR3 + " de  <br> l'" + Class.TDP + "par <br> rapport à son <br> " + Class.SJR3 + " initial"
    fig.add_annotation(x=2.0, y=130, text= text_legende, showarrow=False,
                    font=dict( family="Proxima Nova", size=11, color=black ),align="right",
                    )
                    
    fig.add_annotation(x=3.0, y=niveau_capital,text= str(niveau_capital) +"%", showarrow=False,
                    font=dict( family="Proxima Nova", size=14, color=red ),align="left",
                    )
# #-------------------------------------!Pas fini, doit gerer les 100%! ----------------------------------------------------

    #le premier parametre de range x, permet de mettre ou non un blanc entre le 0 et le premier bloc
   
    fig.add_shape(type="line",
    x0=37.75, y0=116, x1=45, y1=116,
    line=dict(color=green,width=1),  line_dash="dot")
    
    
    fig.add_annotation(x=41.5, y=101,text= ("Seuil d'activation du <br> mécanisme de <br> remboursement anticipé <br> automatique à partir de la fin du <br>" + Class.F0  + " " + str(int(Class.PR1)) + " jusqu'à la fin du " + Class.F0 + " "  + str(int(Class.DPRR) -1) + " <br> et de versement des gains à <br> l'échéance"), showarrow=False,
                    font=dict(family="Proxima Nova", size=12, color=black ), align="left"
                    )


    fig.add_shape(type="line",
    x0=38, y0=60, x1=45, y1=60,
    line=dict(color=red,width=1),  line_dash="dot")
    
    
    fig.add_annotation(x=40.25, y=53,text= ("Seuil de perte en capital <br> à l'échéance"), showarrow=False,
                    font=dict(family="Proxima Nova", size=12, color=black ), align="left",
                    )
    
    fig.update_xaxes(range=[2,48]) #la size max, x
    fig.update_yaxes(range=[0,130]) # y

    #enlever le fond blanc
    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        })


    if (whitestrap == False): #La bande blanche
        fig.add_trace(go.Scatter(x=[5,25,25,5], 
                                y=[niveau_autocall[0] +1 ,niveau_autocall[1] + 1, niveau_autocall[1] -1, niveau_autocall[0] -1],
                                fill='toself',
                                fillcolor='white',
                                line=dict(width=0),
                                showlegend=False,
                                mode='lines',  
                                hoverinfo ='none',))

        fig.add_trace(go.Scatter(x=[27,37,37,27], 
                                y=[niveau_autocall[2] +1 ,niveau_autocall[2] + 1, niveau_autocall[2] -1, niveau_autocall[2] -1],
                                fill='toself',
                                fillcolor='white',
                                line=dict(width=0),
                                showlegend=False,
                                mode='lines',  
                                hoverinfo ='none',))
        fig.add_trace(go.Scatter(x=[27,37,37,27], 
                                y=[niveau_capital +1 ,niveau_capital + 1, niveau_capital -1, niveau_capital -1],
                                fill='toself',
                                fillcolor='white',
                                line=dict(width=0),
                                showlegend=False,
                                mode='lines',  
                                hoverinfo ='none',))     

      
        fig.add_trace(go.Scatter(x=[27,37,37,27], 
                                y=[130 ,130 + 1, niveau_autocall[2], niveau_autocall[2]],
                                fill='toself',
                                fillcolor='#F7F4E9',
                                line=dict(width=0),
                                showlegend=False,
                                mode='lines',  
                                hoverinfo ='none',))  

        fig.add_trace(go.Scatter(x=[5,25,25,5],
                            y=[130 ,130 ,niveau_autocall[1],niveau_autocall[0]],
                            fill='toself',
                            fillcolor='#F7F4E9',
                            line=dict(width=0),
                            showlegend=False,
                            mode='lines',  
                            hoverinfo ='none',))   

    #####################TEXTE DE SES MORTS##############################################
    #autocall[1]
    texta = "<b>Le produit continue </b>:<br><br><br> Aucun " +  str(Class.GC)+ " n'est versé"
    fig.add_annotation(
        x=(15),
        y=(niveau_coupon[1]/2 + 10),
        text=texta,
        showarrow=False,
        font=dict(color=black, size=10)
    )
    gca = ("{:.2f}".format(float(Class.GCA)))

    mystring = "<b>Remboursement à l'échéance : </b><br><br> Le capital inital diminué de l'intégralité <br> de la baisse enregistrée par <br> l'action la moins performante <br> entre la date de constatation initiale <br> et la date de constatation finale <br><br> <b>(perte en capital partielle voire totale)</b>"
    fig.add_annotation(
        x=32,
        y=(niveau_capital/2),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=10)
    )                        


    cpn = Class.CPN.replace(".", ",")


    mystring = "<b>Remboursement anticipé automatique:</b> <br> <br> L'intégralité du capital initial<br>+<br>Un gain de " + cpn + "% par " + Class.F0 + " écoulé <br> depuis la date de constatation initiale <br> (soit un gain de "+ str(gca) + "% par année écoulée)"
    fig.add_annotation(
        x=(15),
        y=(niveau_coupon[0] + (130-niveau_coupon[0]) /2 +5),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=10)
    )      


    mystring = "<b>Remboursement à l'échéance: </b><br><br>L'intégralité du capital initial<br>+<br>Un gain de " + str(cpn) + "% par " + Class.F0 + " écoulé <br> depuis la date de constatation initiale <br> (soit un gain total de "+ str(gce) + "%)"
    fig.add_annotation(
        x=(32),
        y=(float(Class.DBAC) + (130- float(Class.DBAC)) /2 +5),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=10)
    )   

    
    mystring = "<b>Remboursement à l'échéance: </b><br><br>L'intégralité du capital initial"
    #FLECHE ET MOUVEMENT DE TEXTE SI PAS ASSEZ DE PLACE
    if (float(Class.DBAC) - niveau_capital < 10):
        fig.add_annotation(
        x=(41.5),
        y=(30),
        text=mystring,
        showarrow=False,
        font=dict(color=black, size=10)
    )       
    
        fig.add_annotation(
            x=32,  # arrows' head
            ay=31,  # arrows' head
            ax=38,  # arrows' tail
            y=float(Class.DBAC) - (float(Class.DBAC) - niveau_capital)/2 - 10,  # arrows' tail
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
            x=(32),
            y=(float(Class.DBAC) - (float(Class.DBAC) - niveau_capital)/2),
            text=mystring,
            showarrow=False,
            font=dict(color=black, size=10)
        )       
#---------------------------------------------------------------------------------        
    fig.update_layout(  #affichage des options
                        legend=dict(
                        # Adjust click behavior
                            itemclick="toggleothers",
                            itemdoubleclick="toggle"),
                        #legend_title_font_color=f'''rgb({front['barr_green']})''',
                        autosize=True,
                        width=1280,#1400
                        height=700,#800
                        plot_bgcolor='rgb(255,255,255)',
                        margin=dict(
                            l=50,
                            r=0,
                            b=0,
                            t=50,
                            pad=0),
                        paper_bgcolor='white')

    fig.write_image(name, format="png", scale=2, engine='kaleido') #enregistrer l'image
    #fig.show()
    return(fig)

