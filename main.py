#https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/

#defender_fig = px.scatter(data_frame=df, x='Tck/90', y='Shts Blckd/90', title="defender_metrics", hover_name="Name")

from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import pandas as pd
import plotly.express as px
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc

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
external_stylesheets = [dbc.themes.COSMO]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Div(
                    "Player Comparisons in FM",
                    className="text-primary text-center fs-3",
                ),
            ]
        ),

        dbc.Row(
            [
                dcc.Dropdown(
                    id='player-input',
                    placeholder="Please select all players you want to analyze",
                    options=[{"label": i, "value": i} for i in names],
                    multi=True,
                    #value=list(main_df['Name']),
                    #value=main_df.Name.values,
                    style={"width": 1024},
                ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    dcc.RadioItems(
                        options=main_df.columns.values,
                        value='Tck/90',
                        id='radio-button-x-defender-final',
                        labelStyle={'display': 'block'},
                    ),
                ),

                dbc.Col(
                    dcc.RadioItems(
                        options=main_df.columns.values,
                        value='Tck/90',
                        id='radio-button-y-defender-final',
                        style={'width': '100%'},
                        labelStyle={'display': 'block', 'width': '100%'},
                    ),
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={}, 
                        id='graph-placeholder',
                        style={'display': 'inline-block'},
                    ),
                ),
            ]
        ),

        dbc.Row(
            [
                dash_table.DataTable(
                    data=main_df.to_dict('records'),
                    columns=[{"name": i, "id": i} for i in defender_stats],
                    page_size=12,
                    sort_action='native',
                    column_selectable='single',
                    style_table={'overflowX': 'auto'},
                    id='table-container',
                ),
            ]
        ),
    ], fluid=True
)


# Add controls to build the interaction
@callback(
    Output(component_id='graph-placeholder', component_property='figure'),
    Input(component_id='player-input', component_property='value'),
    Input(component_id='radio-button-x-defender-final', component_property='value'),
    Input(component_id='radio-button-y-defender-final', component_property='value')
)
def update_graph(players_chosen, x_chosen, y_chosen):
    figure_df = update_dataframe(players_chosen)
    fig = px.scatter(data_frame=figure_df, x=x_chosen, y=y_chosen, title="defender_metrics", hover_name="Name")

    return fig


@callback(
    Output(component_id='table-container', component_property='data'),
    Input(component_id='player-input', component_property='value')
)
def update_dataframe(players_chosen):
    """Return a dataframe with chosen players."""
    try:
        player_df =  main_df[main_df.Name.isin(players_chosen)]
        return player_df.to_dict('records')
    except TypeError:
        return main_df.to_dict('records')



# Run the App
if __name__ == '__main__':
    app.run(debug=True)