#https://dash-bootstrap-components.opensource.faculty.ai/docs/components/layout/

#defender_fig = px.scatter(data_frame=df, x='Tck/90', y='Shts Blckd/90', title="defender_metrics", hover_name="Name")

from dash import Dash, html, dash_table, dcc, callback, Output, Input, State
import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc

## Create stats dicts
stats_per_90 = {
   'Saves per 90':'Saves/90',
   'Team Goals per 90':'Tgls/90',
   'Non-Penalty Expected Goals per 90':'NP-xG/90',
   'Goals per 90':'Gls/90',
   'Expected Goals per 90':'xG/90',
   'Expected Assists per 90':'xA/90',
   'Conceded per 90':'Con/90',
   'Clean Sheets per 90':'Cln/90',
   'Tackles per 90':'Tck/90',
   'Team Goals Conceded per 90':'Tcon/90',
   'Shots per 90':'Shot/90',
   'Shots Blocked per 90':'Shts Blckd/90',
   'Shots on Target per 90':'ShT/90',
   'Possession Won per 90':'Poss Won/90',
   'Progressive Passes per 90':'Pr passes/90',
   'Pressures Completed per 90':'Pres C/90',
   'Pressures Attempted per 90':'Pres A/90',
   'Possession Lost per 90':'Poss Lost/90',
   'Passes Completed per 90':'Ps C/90',
   'Pass Attempts per 90':'Ps A/90',
   'Open Play Key Passes per 90':'OP-KP/90',
   'Open Play Crosses Completed per 90':'OP-Crs C/90',
   'Open Play Crosses Attempted per 90':'OP-Crs A/90',
   'Key Tackles per 90':'K Tck/90',
   'Crosses Completed per 90':'Cr C/90',
   'Key Passes per 90':'K Ps/90',
   'Key Headers per 90':'K Hdrs/90',
   'Interceptions per 90':'Int/90',
   'Clearances per 90':'Clr/90',
   'Sprints per 90':'Sprints/90',
   'Headers Lost per 90':'Hdrs L/90',
   'Headers Won per 90':'Hdrs W/90',
   'Expected Goals Prevented per 90':'xGP/90',
   'Dribbles Made per 90':'Drb/90',
   'Crosses Attempted per 90':'Crs A/90',
   'Distance Covered per 90':'Dist/90',
   'Chances Created per 90':'Ch C/90',
   'Assists per 90':'Asts/90',
   'Aerial Challenges per 90':'Aer A/90',
   'Blocks per 90':'Blk/90',
   }

stats_dict = {
    'Yellow Cards':'Yel',
    'Expected Goals':'xG',
    'Team Goals Conceded':'Tcon',
    'Team Goals':'Tgls',
    'Starts':'Starts',
    'Red Cards':'Red',
    'Points Won per Game':'Pts/Gm',
    'Player of the Match':'PoM',
    'Penalties Scored Ratio':'Pen/R',
    'Penalties Scored':'Pens S',
    'Penalties Saved Ratio':'Pens Saved Ratio',
    'Penalties Saved':'Pens Saved',
    'Penalties Faced':'Pens Faced',
    'Penalties Taken':'Pens',
    'Non-Penalty Expected Goals':'NP-xG',
    'Minutes Since Last Goal':'Last Gl',
    'Minutes Since Last Conceded':'Last C',
    'Minutes per Game':'Mins/Gm',
    'Minutes':'Mins',
    'Last Match Rating':'LMR',
    'Average Rating Over the Last Five Games':'Last 5 Games',
    'Average Rating Over the Last Five First-Team Games':'Last 5 FT Games',
    'International Goals Conceded':'Int Conc',
    'International Average Rating':'Int Av Rat',
    'International Assists':'Int Ast',
    'International Appearances (Season)':'Int Apps',
    'Goals Conceded':'Conc',
    'Goals':'Gls',
    'Games Won':'Won',
    'Games Missed in a Row':'G. Mis',
    'Games Lost':'Lost',
    'Games Drawn':'D',
    'Game Win Ratio':'Gwin',
    'Fouls Made':'Fls',
    'Fouls Against':'FA',
    'Expected Goals Overperformance':'xG-OP',
    'Expected Assists':'xA',
    'Clean Sheets':'Clean sheets',
    'Average Rating':'Av Rat',
    'Minutes per Goal':'Mins/Gl',
    'Assists':'Ast',
    'Appearances':'Apps',
    'All Time League Goals':'AT Lge Gls',
    'All Time League Appearances':'AT Lge Apps',
    'All Time Career Goals':'AT Gls',
    'Tackles Won':'Tck W',
    'Tackle Won Ratio':'Tck R',
    'Tackle Attempts':'Tck A',
    'Shot on Target Ratio':'Shot %',
    'Shots on Target':'ShT',
    'Shots Blocked':'Shts Blckd',
    'Shots':'Shots',
    'Saves Tipped':'Svt',
    'Saves Parried':'Svp',
    'Saves Held':'Svh',
    'Save Ratio':'Sv %',
    'Progressive Passes':'Pr Passes',
    'Pressures Completed':'Pres C',
    'Pressures Attempted':'Pres A',
    'Passes Completed':'Ps C',
    'Pass Completion Ratio':'Pas %',
    'Pass Attempts':'Pas A',
    'Open Play Key Passes':'OP-KP',
    'Open Play Crosses Completed':'OP-Crs C',
    'Open Play Crosses Attempted':'OP-Crs A',
    'Open Play Cross Completion Ratio':'OP-Cr %',
    'Offsides':'Off',
    'Mistakes Leading to Goal':'Gl Mst',
    'Key Tackles':'K Tck',
    'Key Passes':'K Pas',
    'Interceptions':'Itc',
    'Headers Won Ratio':'Hdr %',
    'Headers Won':'Hdrs',
    'Expected Save Percentage':'xSv %',
    'Expected Goals Prevented':'xGP',
    'Expected Goals per Shot':'xG/shot',
    'Dribbles Made':'Drb',
    'Distance Covered':'Distance',
    'Crosses Completed':'Cr C',
    'Crosses Completed Compared to Crosses Attempted':'Cr C/A',
    'Overall Crosses Attempted':'Cr A',
    'Conversion Rate':'Conv %',
    'Clearances':'Clear',
    'Clear Cut Chances Created':'CCC',
    'Blocks':'Blk',
    'Name':'Name',
    'Headers Attempted':'Hdrs A',
    'All Time Appearances':'AT Apps',
}

goalkeeper_stats = {
    'Name':'Name',
    'Last Match Rating':'LMR',
    'Average Rating Over the Last Five First-Team Games':'Last 5 FT Games',
    'Points Won per Game':'Pts/Gm',
    'Clean Sheets':'Clean sheets',
    'Save Ratio':'Sv %',
    'Expected Save Percentage':'xSv %',
    'Expected Goals Prevented':'xGP',
    'Goals Conceded':'Conc',
    'Minutes':'Mins',
    'Minutes Since Last Conceded':'Last C',
    'Saves Tipped':'Svt',
    'Saves Parried':'Svp',
    'Saves Held':'Svh',
    'Starts':'Starts',
    'Saves per 90':'Saves/90',
    'Conceded per 90':'Con/90',
    'Clean Sheets per 90':'Cln/90',
    'Shots Blocked per 90':'Shts Blckd/90',
    'Passes Completed per 90':'Ps C/90',
    'Expected Goals Prevented per 90':'xGP/90',
}

defender_stats = {
    'Name':'Name',
    'Last Match Rating':'LMR',
    'Average Rating Over the Last Five First-Team Games':'Last 5 FT Games',
    'Points Won per Game':'Pts/Gm',
    'Minutes':'Mins',
    'Mistakes Leading to Goal':'Gl Mst',
    'Clean Sheets per 90':'Cln/90',
    'Fouls Made':'Fls',
    'Fouls Against':'FA',
    'Yellow Cards':'Yel',
    'Red Cards':'Red',
    'Tackles per 90':'Tck/90',
    'Tackle Won Ratio':'Tck R',
    'Shots Blocked per 90':'Shts Blckd/90',
    'Possession Won per 90':'Poss Won/90',
    'Possession Lost per 90':'Poss Lost/90',
    'Key Tackles per 90':'K Tck/90',
    'Key Headers per 90':'K Hdrs/90',
    'Interceptions per 90':'Int/90',
    'Clearances per 90':'Clr/90',
    'Headers Lost per 90':'Hdrs L/90',
    'Headers Won per 90':'Hdrs W/90',
    'Headers Won Ratio':'Hdr %',
    'Expected Goals Prevented':'xGP',
    'Expected Goals Prevented per 90':'xGP/90',
    'Aerial Challenges per 90':'Aer A/90',
    'Blocks per 90':'Blk/90',
    'Clearances':'Clear',
}

midfield_stats = {
    'Name':'Name',
    'Last Match Rating':'LMR',
    'Average Rating Over the Last Five First-Team Games':'Last 5 FT Games',
    'Points Won per Game':'Pts/Gm',
    'Minutes':'Mins',
    'Goals':'Gls',
    'Fouls Made':'Fls',
    'Fouls Against':'FA',
    'Yellow Cards':'Yel',
    'Red Cards':'Red',
    'Headers Won Ratio':'Hdr %',
    'Tackle Won Ratio':'Tck R',
    'Tackles per 90':'Tck/90',
    'Key Tackles per 90':'K Tck/90',
    'Possession Won per 90':'Poss Won/90',
    'Possession Lost per 90':'Poss Lost/90',
    'Interceptions per 90':'Int/90',
    'Open Play Key Passes per 90':'OP-KP/90',
    'Open Play Crosses Completed per 90':'OP-Crs C/90',
    'Open Play Crosses Attempted per 90':'OP-Crs A/90',
    'Crosses Completed Compared to Crosses Attempted':'Cr C/A',
    'Key Passes per 90':'K Ps/90',
    'Sprints per 90':'Sprints/90',
    'Dribbles Made per 90':'Drb/90',
    'Crosses Attempted per 90':'Crs A/90',
    'Distance Covered per 90':'Dist/90',
    'Chances Created per 90':'Ch C/90',
    'Assists per 90':'Asts/90',
    'Expected Assists':'xA',
}

striker_stats = {
    'Name':'Name',
    'Last Match Rating':'LMR',
    'Average Rating Over the Last Five First-Team Games':'Last 5 FT Games',
    'Points Won per Game':'Pts/Gm',
    'Minutes':'Mins',
    'Goals':'Gls',
    'Fouls Made':'Fls',
    'Fouls Against':'FA',
    'Yellow Cards':'Yel',
    'Red Cards':'Red',
    'Minutes':'Mins',
    'Non-Penalty Expected Goals':'NP-xG',
    'Minutes Since Last Goal':'Last Gl',
    'Expected Goals Overperformance':'xG-OP',
    'Minutes per Goal':'Mins/Gl',
    'Shot on Target Ratio':'Shot %',
    'Offsides':'Off',
    'Expected Goals per Shot':'xG/shot',
    'Conversion Rate':'Conv %',
    'Shots per 90':'Shot/90',
    'Shots on Target per 90':'ShT/90',
    'Expected Goals per 90':'xG/90',
    'Expected Assists per 90':'xA/90',
    'Possession Won per 90':'Poss Won/90',
    'Passes Completed per 90':'Ps C/90',
    'Pass Attempts per 90':'Ps A/90',
    'Open Play Crosses Completed per 90':'OP-Crs C/90',
    'Open Play Crosses Attempted per 90':'OP-Crs A/90',
    'Headers Won Ratio':'Hdr %',
}

radio_items_dict = {
    "Goalkeeper Stats": goalkeeper_stats,
    "Defender Stats": defender_stats,
    "Midfield Stats": midfield_stats,
    "Striker Stats": striker_stats,
}

## Get FM data
html_file = "./raw_data/stats.html"

df = pd.read_html(html_file)
main_df = df[0]

names = main_df.Name.unique().tolist()

#defender_stats = ['Name', 'Tck/90', 'Shts Blckd/90', 'Yel', 'Red']
defender_df = main_df.filter(list(defender_stats.values()), axis=1)


dropdown_menu_items = [
    dbc.DropdownMenuItem("Goalkeeper Stats", id="dropdown-menu-item-1"),
    dbc.DropdownMenuItem("Defender Stats", id="dropdown-menu-item-2"),
    dbc.DropdownMenuItem("Midfielder Stats", id="dropdown-menu-item-3"),
    dbc.DropdownMenuItem("Striker Stats", id="dropdown-menu-item-4"),
    dbc.DropdownMenuItem(divider=True),
    dbc.DropdownMenuItem("Clear", id="dropdown-menu-item-clear")

]

## Initialize Dash App
external_stylesheets = [dbc.themes.COSMO]
app = Dash(__name__, external_stylesheets=external_stylesheets)

# App layout
app.layout = dbc.Container(
    [
        dbc.Row(
            [
                html.Div(
                    "Goalkeeper Analysis",
                    className="text-primary text-center fs-3",
                ),
            ]
        ),

        dbc.Row(
            [
                dcc.Dropdown(
                    placeholder="Please select all players you want to analyze",
                    options=[{"label": i, "value": i} for i in names],
                    multi=True,
                    #value=list(main_df['Name']),
                    #value=main_df.Name.values,
                    style={"width": 1024},
                    id='goalkeeper-player-input',
                ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    dcc.RadioItems(
                        options=[{"label": x, "value": goalkeeper_stats[x]} for x in goalkeeper_stats],
                        value='Last 5 FT Games',
                        labelStyle={'display': 'block'},
                        id='goalkeeper-stats-x',
                    ),
                ),

                dbc.Col(
                    dcc.RadioItems(
                        options=[{"label": x, "value": goalkeeper_stats[x]} for x in goalkeeper_stats],
                        value='Pts/Gm',
                        style={'width': '100%'},
                        labelStyle={'display': 'block', 'width': '100%'},
                        id='goalkeeper-stats-y',
                    ),
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={}, 
                        id='goalkeeper-graph-placeholder',
                        style={
                            'display': 'inline-block',
                            'width': '55vh',
                            'height': '60vh',
                            },
                    ),
                ),
            ]
        ),
        dbc.Row(
            [
                dash_table.DataTable(
                    data=main_df.to_dict('records'),
                    columns=[{"name": i, "id": goalkeeper_stats[i]} for i in goalkeeper_stats],
                    page_size=12,
                    sort_action='native',
                    column_selectable='single',
                    style_table={'overflowX': 'auto'},
                    id='goalkeeper-table-container',
                ),
            ]
        ),


        dbc.Row(
            [
                html.Div(
                    "Defender Analysis",
                    className="text-primary text-center fs-3",
                ),
            ]
        ),

        dbc.Row(
            [
                dcc.Dropdown(
                    placeholder="Please select all players you want to analyze",
                    options=[{"label": i, "value": i} for i in names],
                    multi=True,
                    #value=list(main_df['Name']),
                    #value=main_df.Name.values,
                    style={"width": 1024},
                    id='defender-player-input',
                ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    dcc.RadioItems(
                        options=[{"label": x, "value": defender_stats[x]} for x in defender_stats],
                        value='Last 5 FT Games',
                        labelStyle={'display': 'block'},
                        id='defender-stats-x',
                    ),
                ),

                dbc.Col(
                    dcc.RadioItems(
                        options=[{"label": x, "value": defender_stats[x]} for x in defender_stats],
                        value='Pts/Gm',
                        style={'width': '100%'},
                        labelStyle={'display': 'block', 'width': '100%'},
                        id='defender-stats-y',
                    ),
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={}, 
                        id='defender-graph-placeholder',
                        style={
                            'display': 'inline-block',
                            'width': '55vh',
                            'height': '60vh',
                            },
                    ),
                ),
            ]
        ),
        dbc.Row(
            [
                dash_table.DataTable(
                    data=main_df.to_dict('records'),
                    columns=[{"name": i, "id": defender_stats[i]} for i in defender_stats],
                    page_size=12,
                    sort_action='native',
                    column_selectable='single',
                    style_table={'overflowX': 'auto'},
                    id='defender-table-container',
                ),
            ]
        ),
        dbc.Row(
            [
                html.Div(
                    "Midfielder Analysis",
                    className="text-primary text-center fs-3",
                ),
            ]
        ),

        dbc.Row(
            [
                dcc.Dropdown(
                    placeholder="Please select all players you want to analyze",
                    options=[{"label": i, "value": i} for i in names],
                    multi=True,
                    #value=list(main_df['Name']),
                    #value=main_df.Name.values,
                    style={"width": 1024},
                    id='midfielder-player-input',
                ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    dcc.RadioItems(
                        options=[{"label": x, "value": midfield_stats[x]} for x in midfield_stats],
                        value='Last 5 FT Games',
                        labelStyle={'display': 'block'},
                        id='midfielder-stats-x',
                    ),
                ),

                dbc.Col(
                    dcc.RadioItems(
                        options=[{"label": x, "value": midfield_stats[x]} for x in midfield_stats],
                        value='Pts/Gm',
                        style={'width': '100%'},
                        labelStyle={'display': 'block', 'width': '100%'},
                        id='midfielder-stats-y',
                    ),
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={}, 
                        id='midfielder-graph-placeholder',
                        style={
                            'display': 'inline-block',
                            'width': '55vh',
                            'height': '60vh',
                            },
                    ),
                ),
            ]
        ),
        dbc.Row(
            [
                dash_table.DataTable(
                    data=main_df.to_dict('records'),
                    columns=[{"name": i, "id": midfield_stats[i]} for i in midfield_stats],
                    page_size=12,
                    sort_action='native',
                    column_selectable='single',
                    style_table={'overflowX': 'auto'},
                    id='midfielder-table-container',
                ),
            ]
        ),


        dbc.Row(
            [
                html.Div(
                    "Striker Analysis",
                    className="text-primary text-center fs-3",
                ),
            ]
        ),

        dbc.Row(
            [
                dcc.Dropdown(
                    placeholder="Please select all players you want to analyze",
                    options=[{"label": i, "value": i} for i in names],
                    multi=True,
                    #value=list(main_df['Name']),
                    #value=main_df.Name.values,
                    style={"width": 1024},
                    id='striker-player-input',
                ),
            ]
        ),

        dbc.Row(
            [
                dbc.Col(
                    dcc.RadioItems(
                        options=[{"label": x, "value": striker_stats[x]} for x in striker_stats],
                        value='Last 5 FT Games',
                        labelStyle={'display': 'block'},
                        id='striker-stats-x',
                    ),
                ),

                dbc.Col(
                    dcc.RadioItems(
                        options=[{"label": x, "value": striker_stats[x]} for x in striker_stats],
                        value='Pts/Gm',
                        style={'width': '100%'},
                        labelStyle={'display': 'block', 'width': '100%'},
                        id='striker-stats-y',
                    ),
                ),
                dbc.Col(
                    dcc.Graph(
                        figure={}, 
                        id='striker-graph-placeholder',
                        style={
                            'display': 'inline-block',
                            'width': '55vh',
                            'height': '60vh',
                            },
                    ),
                ),
            ]
        ),
        dbc.Row(
            [
                dash_table.DataTable(
                    data=main_df.to_dict('records'),
                    columns=[{"name": i, "id": striker_stats[i]} for i in striker_stats],
                    page_size=12,
                    sort_action='native',
                    column_selectable='single',
                    style_table={'overflowX': 'auto'},
                    id='striker-table-container',
                ),
            ]
        ),
    ], fluid=True
)


# Add controls to build the interaction
## First Goalkeepers
@callback(
    Output(component_id='goalkeeper-graph-placeholder', component_property='figure'),
    Input(component_id='goalkeeper-player-input', component_property='value'),
    Input(component_id='goalkeeper-stats-x', component_property='value'),
    Input(component_id='goalkeeper-stats-y', component_property='value')
)
def update_graph(players_chosen, x_chosen, y_chosen):
    try:
        figure_df = update_dataframe(players_chosen)
        fig = px.scatter(data_frame=figure_df, x=x_chosen, y=y_chosen, title="Goalkeeper Metrics", hover_name="Name")

        return fig
    except ValueError:
        fig = px.scatter(data_frame=main_df, x=x_chosen, y=y_chosen, title="Goalkeeper Metrics", hover_name="Name")
        return fig


@callback(
    Output(component_id='goalkeeper-table-container', component_property='data'),
    Input(component_id='goalkeeper-player-input', component_property='value')
)
def update_dataframe(players_chosen):
    """Return a dataframe with chosen players."""
    try:
        player_df =  main_df[main_df.Name.isin(players_chosen)]
        return player_df.to_dict('records')
    except TypeError:
        return main_df.to_dict('records')

## Defenders

@callback(
    Output(component_id='defender-graph-placeholder', component_property='figure'),
    Input(component_id='defender-player-input', component_property='value'),
    Input(component_id='defender-stats-x', component_property='value'),
    Input(component_id='defender-stats-y', component_property='value')
)
def update_graph(players_chosen, x_chosen, y_chosen):
    try:
        figure_df = update_dataframe(players_chosen)
        fig = px.scatter(data_frame=figure_df, x=x_chosen, y=y_chosen, title="Defender Metrics", hover_name="Name")

        return fig
    except ValueError:
        fig = px.scatter(data_frame=main_df, x=x_chosen, y=y_chosen, title="Defender Metrics", hover_name="Name")
        return fig


@callback(
    Output(component_id='defender-table-container', component_property='data'),
    Input(component_id='defender-player-input', component_property='value')
)
def update_dataframe(players_chosen):
    """Return a dataframe with chosen players."""
    try:
        player_df =  main_df[main_df.Name.isin(players_chosen)]
        return player_df.to_dict('records')
    except TypeError:
        return main_df.to_dict('records')

## Midfielders
@callback(
    Output(component_id='midfielder-graph-placeholder', component_property='figure'),
    Input(component_id='midfielder-player-input', component_property='value'),
    Input(component_id='midfielder-stats-x', component_property='value'),
    Input(component_id='midfielder-stats-y', component_property='value')
)
def update_graph(players_chosen, x_chosen, y_chosen):
    try:
        figure_df = update_dataframe(players_chosen)
        fig = px.scatter(data_frame=figure_df, x=x_chosen, y=y_chosen, title="Midfield Metrics", hover_name="Name")

        return fig
    except ValueError:
        fig = px.scatter(data_frame=main_df, x=x_chosen, y=y_chosen, title="Midfield Metrics", hover_name="Name")
        return fig


@callback(
    Output(component_id='midfielder-table-container', component_property='data'),
    Input(component_id='midfielder-player-input', component_property='value')
)
def update_dataframe(players_chosen):
    """Return a dataframe with chosen players."""
    try:
        player_df =  main_df[main_df.Name.isin(players_chosen)]
        return player_df.to_dict('records')
    except TypeError:
        return main_df.to_dict('records')

## Strikers
@callback(
    Output(component_id='striker-graph-placeholder', component_property='figure'),
    Input(component_id='striker-player-input', component_property='value'),
    Input(component_id='striker-stats-x', component_property='value'),
    Input(component_id='striker-stats-y', component_property='value')
)
def update_graph(players_chosen, x_chosen, y_chosen):
    try:
        figure_df = update_dataframe(players_chosen)
        fig = px.scatter(data_frame=figure_df, x=x_chosen, y=y_chosen, title="Striker Metrics", hover_name="Name")

        return fig
    except ValueError:
        fig = px.scatter(data_frame=main_df, x=x_chosen, y=y_chosen, title="Striker Metrics", hover_name="Name")
        return fig


@callback(
    Output(component_id='striker-table-container', component_property='data'),
    Input(component_id='striker-player-input', component_property='value')
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