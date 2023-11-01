#defender_fig = px.scatter(data_frame=df, x='Tck/90', y='Shts Blckd/90', title="defender_metrics", hover_name="Name")

from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc

## Get FM data
html_file = "./raw_data/stats.html"

## Set players by position
defenders = ["Andre Blackman", "Zehn Mohammed", "Jack Holland"]

df = pd.read_html(html_file)
main_df = df[0]

names = main_df.Name.unique().tolist()

defender_stats = ['Name', 'Tck/90', 'Shts Blckd/90', 'Yel', 'Red']
defender_df = main_df.filter(defender_stats, axis=1)
defender_df = defender_df[main_df['Name'].isin(defenders)]



## Initialize Dash App
external_stylesheets = [dmc.theme.DEFAULT_COLORS]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dmc.Container([
    dmc.Title('My First App with Data, Graph, and Controls', color="blue", size="h3"),
    dcc.Dropdown(
        id='player-input',
        placeholder="Please select all players you want to analyze",
        options=[{"label": i, "value": i} for i in names],
        multi=True,
        #value=list(main_df['Name']),
        value=main_df.Name.values,
        style={"width": 400},
    ),
    dmc.Grid([
        dmc.Col([
            dash_table.DataTable(
                data=main_df.to_dict('records'),
                columns=[{"name": i, "id": i} for i in main_df.columns],
                page_size=12,
                sort_action='native',
                column_selectable='single',
                style_table={'overflowX': 'auto'},
                id='table-container',
            )
        ], span=6),
        dmc.Col([
            dcc.Graph(figure={}, id='graph-placeholder')
        ], span=6),
    ]),

], fluid=True)

# Add controls to build the interaction
@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='player-input', component_property='value')
)
def update_graph(col_chosen):
    fig = px.scatter(data_frame=main_df, x='Tck/90', y='Shts Blckd/90', title="defender_metrics", hover_name="Name")

    return fig


@callback(
    Output(component_id='table-container', component_property='data'),
    Input(component_id='player-input', component_property='value')
)
def update_dataframe(players_chosen):
    """Return a dataframe with chosen players."""
    player_df =  main_df[df.Name.isin(players_chosen)]

    return player_df.to_dict('records')

# Run the App
if __name__ == '__main__':
    app.run(debug=True)