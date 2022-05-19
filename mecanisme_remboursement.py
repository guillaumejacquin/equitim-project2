from cgitb import text
from optparse import Values
import plotly.graph_objects as go
import kaleido

# 1 #si  coupon == coupon_autocall == True, 2 blocs, (soit SANS barrière coupon)

# 2 #si coupon == coupon_Phoenix == True, 3 blocs (soit avec barrière coupon)
        ## Possibilité qu'il y ait uniquement deux bloc dans le cas ou la balise (tag) de Non-Call (1PR) == 0
        ## Sinon, NC > 0, alors toujours 3 blocs et dans le premier bloc se trouveras uniquement la barrière coupon(bleu marine)

def mecanisme_remboursement():
    x0 = 4
    x1 = x0+0.5
    niveau_autocall = [100, 77.5, 70] #ligne verte
    niveau_coupon = [70, 70, 70] #ligne noire  niveau coupon
    niveau_capital = 40 #Ligne rouge

    niveau_median = niveau_coupon[0] - niveau_capital

    labels = [5, 27]
    widths = [20,10]

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
# #------------------------------------------NE BOUGE PAS----------------------------------------------------------------------------------------------
#     fig.add_annotation( x=4.5, y=140, ax=4.5, ay=0, xref='x', yref='y', axref='x', ayref='y',
#      text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')

#     fig.add_annotation(x=38, y=0, ax=4.25, ay=0, xref='x', yref='y', axref='x', ayref='y', text='',
#     showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')

#     fig.update_xaxes(tickangle=0,
#                     tickmode = 'array',
#                     tickvals = [14, 31.5],
#                     ticktext= ["Trimestre 4 à 39", "Trimestre 40"],
#                     tickfont_size = 8                    
#                     )

#     fig.update_yaxes(tickangle=0,
#                     tickmode = 'array',
#                     tickvals = [0],
#                     ticktext= ["","", "", ""],
#                     ),

#     #LIGNE NOIRE
#     lol = 1
#     if ( lol == 0):
#         fig.add_shape( # add la ligne horizontale deuxieme block line
#             type="line", line_color="black", line_width=3, opacity=1, line_dash="dot",
#             x0=5, x1=25, y0=niveau_coupon[0], y1=niveau_coupon[1]
#         )

#         fig.add_shape( # add la ligne horizontale troisieme block line
#             type="line", line_color="black", line_width=3, opacity=1, line_dash="dot",
#             x0=27, x1=37, y0=niveau_coupon[2], y1=niveau_coupon[2]
#         )
#         fig.add_shape(type="line",
#         x0=x0, y0=niveau_coupon[-1], x1=x1, y1=niveau_coupon[-1],
#         line=dict(color="black",width=3))
#         fig.add_annotation(x=3.0, y=niveau_coupon[-1], text= str(niveau_coupon[-1]) +"%", showarrow=False,
#                         font=dict( family="Proxima Nova", size=14, color="Black" ),
#                         )
# #     # !LIGNE NOIRE

# #     #LIGNE VERTE

#     fig.add_shape( # add la ligne horizontale deuxieme block line degressive
#         type="line", line_color="green", line_width=3, opacity=1, line_dash="dot",
#         x0=5, x1=25, y0=niveau_autocall[0], y1=niveau_autocall[1]
#     )

#     fig.add_shape( # add la ligne horizontale deuxieme block line degressive
#         type="line", line_color="green", line_width=3, opacity=1, line_dash="dot",
#         x0=27, x1=37, y0=niveau_autocall[2], y1=niveau_autocall[2]
#     )
# #     #!LIGNE VERTE

#     #LIGNE ROUGE
#     if (niveau_capital >= niveau_autocall[2] and niveau_autocall[2] > 0 or niveau_capital >= niveau_coupon[2] and niveau_coupon[2] > 0):
#         niveau_capital = -5
#     fig.add_shape( # add la ligne horizontale deuxieme block line degressive
#         type="line", line_color="#C00000", line_width=3, opacity=1, line_dash="dash",
#         x0=27, x1=37, y0=niveau_capital, y1=niveau_capital
#     )

# #     #!LIGNE ROUGE

#     if (niveau_autocall[1] > 0):
#         fig.add_trace(go.Scatter(x=[5,25,25,5],
#                             y=[niveau_autocall[0],niveau_autocall[1], 0, 0],
#                             fill='toself',
#                             fillcolor='#E5EBF7',
#                             line=dict(width=0),
#                             showlegend=False,
#                             mode='lines',  
#                             hoverinfo ='none',
# ))


# #     #ici on remplace les valeurs x (ecrites abcisses(ne plus avoir 10 20 30 40 mais trimestre1 etc))
# #         # ajout des petites lignes nulles

#     fig.add_shape(type="line",
#     x0=x0, y0=niveau_autocall[0], x1=x1, y1=niveau_autocall[0],
#     line=dict(color="green",width=3))

#     fig.add_shape(type="line",
#     x0=x0, y0=niveau_capital, x1=x1, y1=niveau_capital,
#     line=dict(color="#C00000",width=3))
# # #------------------------------------------NE BOUGE PAS---------------------------------------------------------------------------------------------


# # #-------------------------------------Pas fini, doit gerer les 100% ----------------------------------------------------
# #     #NIVEAU de reference seulement si 100 % sinon creer bloc 90%(classique) et au dessu sniveau de reference100% (en noir)

# #     #les valeurs qu on va mettre
#     if (niveau_autocall[0] != 100):
#         fig.add_annotation(x=2.5, y=100 - 2,text= ("Niveau de Référence<br> (100%)"), showarrow=False,
#                     font=dict( family="Proxima Nova", size=8, color="Green" ),
#                     )

#         fig.add_annotation(x=3.0, y=niveau_autocall[0], text= str(niveau_autocall[0]) +"%", showarrow=False,
#                     font=dict( family="Proxima Nova", size=8, color="Green" ))
#     else:
#         fig.add_annotation(x=2.25, y=100 - 2,text= ("Niveau de<br> Référence<br> (" + str(niveau_autocall[0]) + "%)"), showarrow=False,
#                     font=dict( family="Proxima Nova", size=8, color="Green" ),
#                     )


#     fig.add_annotation(x=2.0, y=130, text= "Niveau de  <br> l'indice par <br> rapport à son <br> Niveau initial", showarrow=False,
#                     font=dict( family="Proxima Nova", size=8, color="black" ),
#                     )
                    
#     fig.add_annotation(x=3.0, y=niveau_capital,text= str(niveau_capital) +"%", showarrow=False,
#                     font=dict( family="Proxima Nova", size=8, color="Red" ),
#                     )
# # #-------------------------------------!Pas fini, doit gerer les 100%! ----------------------------------------------------

#     #le premier parametre de range x, permet de mettre ou non un blanc entre le 0 et le premier bloc
   
#     fig.add_shape(type="line",
#     x0=38, y0=116, x1=48, y1=116,
#     line=dict(color="green",width=2),  line_dash="dot")
    
    
#     fig.add_annotation(x=44, y=96,text= ("Seuil d'activation du <br> mécanisme de <br> remboursement anticipé <br> automatique à partir de la fin du <br> trimestre 4 jusqu'à la fin du trimestre <br> 20 et de versement des gains à <br> l'échéance"), showarrow=False,
#                     font=dict(family="Proxima Nova", size=8, color="Black" ),
#                     )


#     fig.add_shape(type="line",
#     x0=38, y0=60, x1=48, y1=60,
#     line=dict(color="red",width=2),  line_dash="dot")
    
    
#     fig.add_annotation(x=44, y=52,text= ("Seuil de perte en capital <br> à l'échéance"), showarrow=False,
#                     font=dict(family="Proxima Nova", size=8, color="Black" ),
#                     )
    
#     fig.update_xaxes(range=[2,48])
#     fig.update_yaxes(range=[0,130])

#     #enlever le fond blanc

    fig.update_layout({
        'plot_bgcolor': 'rgba(0, 0, 0, 0)',
        })


    # fig.write_image("file_name222.png", format="png", scale=2, engine='kaleido')
    fig.show()
    return(fig)



    #REGARDER SI POSSIBLE DE FAIRE  ALIGNER DISTRIBUER VERTICALEMENT
mecanisme_remboursement()