import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Define your variables
beers=['2015', '2016', '2017', '2018']
ibu_values=[81, 103, 139, 164]
abv_values=[86, 84, 101, 103]
color1='lightgreen'
color2='orange'
mytitle='Payroll vs. Wins Comparison'
tabtitle='Money Wins?'
myheading='Astros Payroll vs. Wins'
label1='Payroll (M)'
label2='Wins'
githublink='hhttps://github.com/nomsdoms/flying-dog-beers'
sourceurl='https://www.baseball-reference.com/teams/HOU/index.shtml'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)


########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    ]
)

if __name__ == '__main__':
    app.run_server()
