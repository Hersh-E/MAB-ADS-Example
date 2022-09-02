import dash
import dash_bootstrap_components as dbc
import os

app = dash.Dash("Name my app", external_stylesheets=[dbc.themes.YETI], suppress_callback_exceptions=True)

application = app.server
