import dash
import plotly
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import pandas as pd
from dash.dependencies import Input, Output, State, MATCH, ALL
from dash.exceptions import PreventUpdate

import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

from app import app
from datetime import date, timedelta

import os

from random import random, uniform, choice
from py_classes.epsilon_greedy_class import Creative

def actual_ad(index):
    return dbc.Card([
        dbc.CardHeader(f"Advertisement: {index}", style={'text-align': 'center'}),
        dbc.CardBody([
            html.P("Click Rate"),
            # dbc.Label('Click Rate', html_for={'type':'click_rate', 'index':index}),
            dbc.Input(type='number', min=0, max=1, value=random(), id={'type':'click_rate', 'index':index}),
            html.Hr(),
            html.P("Click Revenue"),
            # dbc.Label('Click Revenue', html_for={'type':'click_rev', 'index':index}),
            dbc.Input(type='number', min=0, max=10, value=uniform(1,10), id={'type':'click_rev', 'index':index}),
        ])
    ])


def learned_action(index):
    return dbc.Card([
        dbc.CardHeader(f"Advertisement: {index}", style={'text-align': 'center'}),
        dbc.CardBody([
            html.P("Click Rate"),
            # dbc.Label('Click Rate', html_for={'type':'click_rate', 'index':index}),
            dbc.Input(type='number', min=0, max=1, value=0, id={'type':'click_rate_learned', 'index':index}),
            html.Hr(),
            html.P("Rev Per Impression"),
            # dbc.Label('Click Revenue', html_for={'type':'click_rev', 'index':index}),
            dbc.Input(type='number', min=0, max=10, value=0, id={'type':'click_rev_learned', 'index':index}),
        ])
    ])


def serve_layout():
    return [
        dbc.Row([
            dbc.Col([actual_ad(1)], className='px-0'),
            dbc.Col([actual_ad(2)], className='px-0'),
            dbc.Col([actual_ad(3)], className='px-0'),
            dbc.Col([actual_ad(4)], className='px-0'),
        ]),
        dbc.Row([
            dbc.Button("run", color="primary", className="me-1", id='run_button'),
        ]),
        dbc.Row([
            dbc.Col([]),
            dbc.Col([]),
        ]),
        dbc.Row([
            dbc.Col([]),
            dbc.Col([]),
        ]),
        dbc.Row([
            dbc.Col([learned_action(1)], className='px-0'),
            dbc.Col([learned_action(2)], className='px-0'),
            dbc.Col([learned_action(3)], className='px-0'),
            dbc.Col([learned_action(4)], className='px-0'),
        ]),
    ]

@app.callback([Output({'type': 'click_rate_learned', 'index': ALL}, 'value'), Output({'type': 'click_rev_learned', 'index': ALL}, 'value')],
    [Input(f'run_button', 'n_clicks')],
    [State({'type': 'click_rate', 'index': ALL}, 'value'),
    State({'type': 'click_rev', 'index': ALL}, 'value'),
    State({'type': 'click_rev', 'index': ALL}, 'id'),
    ]
    )
def simulate(n_clicks, click_rates, click_revs, ids):

    if len(Creative.ad_list) == 0:
        for rate, rev, id in zip(click_rates, click_revs, ids):
            Creative(id['index'], rate, rev)

    for i in range(100):
        ad = Creative.epsilon_greedy(.5)
        ad.get_reward()

    learned_rates = []
    learned_revs = []
    for ad in Creative.ad_list:
        learned_rates.append(ad.calc_rate())
        learned_revs.append(ad.calc_Q())

    return [learned_rates, learned_revs]
