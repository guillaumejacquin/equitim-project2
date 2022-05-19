import plotly.graph_objects as go

def bloc5():
    coupon = 80

    green = "#00B050"
    blue = "#002E8A"
    red = "#C00000"
    black = "#000000"
    fig = go.Figure()
    fig.update_layout(
        xaxis=dict(
            showline=True,
            showgrid=True,
            showticklabels=True,
            linecolor='rgb(0, 0, 0)',
            linewidth= 1,
            ticks='outside',
            title=None,
            tickfont=dict(
                family='Proxima Nova',
                size=12,
                color='rgb(82, 82, 82)',   
            ),
        ),
        yaxis=dict(
            showgrid=True,
            zeroline=False,
            showline=True,
            showticklabels=True,
            ticks='outside',
            gridwidth=1,
            gridcolor='rgb(242, 242, 242)',
            linecolor='rgb(0, 0, 0)',
            linewidth= 1,
            title=None,
            tickfont=dict(
                family='Proxima Nova',
                size=13,
                color='rgb(82, 82, 82)',
                )
        ),
        showlegend=False,

        plot_bgcolor='white'
    )

    fig.add_annotation(x=1, y=155, ax=1, ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black',align="left")
    
    fig.add_annotation(x=20.5, y=0, ax= 1, ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black',align="left")
    
    fig.add_annotation(x=20.15, y=155, ax=20.15, ay=0, xref='x', yref='y', axref='x', ayref='y',
     text='', showarrow=True, arrowhead=3, arrowwidth=2, arrowcolor='black')
    
    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=green, line_width=2, opacity=1,
        x0=20.15, x1=20.15, y0=0, y1=155
    )

    fig.update_xaxes(range=[1,20.5])
    fig.update_yaxes(range=[0,155])

    fig.add_shape( # add la ligne horizontale deuxieme block line degressive
        type="line", line_color=green, line_width=2, opacity=1,
        x0=0, x1=25, y0=coupon, y1=coupon
    )


    fig.show()

bloc5()
  
