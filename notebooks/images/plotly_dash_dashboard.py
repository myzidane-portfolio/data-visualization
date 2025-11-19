
import dash
from dash import dcc, html, Input, Output
import plotly.express as px

# Load data
df = px.data.gapminder()

# Initialize app
app = dash.Dash(__name__)

years = sorted(df['year'].unique())
continents = df['continent'].unique()

app.layout = html.Div([
    html.H1("🌍 Global Development Dashboard", style={'textAlign': 'center'}),

    html.Div([
        html.Div([
            html.Label("Select Year:"),
            dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': str(y), 'value': y} for y in years],
                value=2007,
                clearable=False
            )
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '0 10px'}),

        html.Div([
            html.Label("Select Continent:"),
            dcc.Dropdown(
                id='continent-dropdown',
                options=[{'label': c, 'value': c} for c in continents],
                value='Asia',
                clearable=False
            )
        ], style={'width': '45%', 'display': 'inline-block', 'padding': '0 10px'})
    ]),

    html.Br(),

    html.Div([
        dcc.Graph(id='scatter-plot'),
        dcc.Graph(id='bar-chart')
    ])
])

@app.callback(
    [Output('scatter-plot', 'figure'),
     Output('bar-chart', 'figure')],
    [Input('year-dropdown', 'value'),
     Input('continent-dropdown', 'value')]
)
def update_dashboard(selected_year, selected_continent):
    dff = df[(df['year'] == selected_year) & (df['continent'] == selected_continent)]

    scatter_fig = px.scatter(
        dff, x="gdpPercap", y="lifeExp", size="pop", color="country",
        hover_name="country", log_x=True,
        title=f"Life Expectancy vs GDP per Capita ({selected_continent}, {selected_year})"
    )
    scatter_fig.update_layout(title_x=0.5)

    bar_fig = px.bar(
        dff.sort_values('lifeExp', ascending=False),
        x="country", y="lifeExp", color="country",
        title=f"Life Expectancy by Country ({selected_continent}, {selected_year})"
    )
    bar_fig.update_layout(title_x=0.5, xaxis_tickangle=-45)

    return scatter_fig, bar_fig

if __name__ == "__main__":
    app.run_server(debug=True)
