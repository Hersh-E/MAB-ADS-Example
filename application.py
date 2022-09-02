import dash
import dash_bootstrap_components as dbc
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State

import flask
import glob
import os

from app import app
from app import application

from tabs import epsilon_greedy_example

# chart_directory = './GuidedAnalyses/*/Charts/'
# list_of_charts = {os.path.basename(x): os.path.dirname(x) for x in glob.glob('{}*.html'.format(chart_directory))}
# static_chart_route = '/charts/'

app.layout = app.layout = html.Div([
    html.Div(
        dbc.Container([
    		html.H1("Using Machine Learning to Cleanse Data", className="display-3"),
    		html.P("This is a proof of concept on how clustering can help cleanse manual entry data", className="lead"),
    		html.Hr(className="my-2"),
    		html.P([
    			"Read the below guide for how this proof of concept works.", html.Br(),
    			"Check out the interactive example on the following tab.", html.Br(),
    			"Lastly, go over the considerations. This is only a proof of concept after all."
    		]),
    	], className='py-3'),
    className="p-3 bg-light rounded-3"),
	# Tab Line
    dbc.Container([
    	dbc.Row([
    		dbc.Tabs([
    			# dbc.Tab(label="Overview", tab_id="overview"),
    			dbc.Tab(label="Epsilon Greedy Example", tab_id="eg_ex"),
    			# dbc.Tab(label="Considerations", tab_id="considerations"),
    			# dbc.Tab(label="About", tab_id="about"),
    		], id='tabs', active_tab="eg_ex"),
			html.Hr(className="mb-0 px-0 pb-0"),
		], className='pt-3'),
	], className='',),
	# Info Cards
	# dbc.Container([], id="content", style={'padding':0}, className="tab-content"),
	dbc.Container([], id="content", className="tab-content"),
	# hidden div to hold the name data
	html.Div(id='name-list', style={'display':'none'}),
])


@app.callback([Output("content", "children")], [Input("tabs", "active_tab")])
def switch_tab(at):
	if at == "eg_ex":
		content = epsilon_greedy_example.serve_layout()
	# elif at == "example":
	# 	content = example_view
	# elif at == "considerations":
	# 	content = considerations
	# elif at == "about":
	# 	content = about
	return [content]



# @app.server.route('{}<fig_path>.html'.format(static_chart_route))
# def serve_image(fig_path):
#     fig_name = '{}.html'.format(fig_path)
#     if fig_name not in list_of_charts:
#         raise Exception('"{}" is excluded from the allowed static files'.format(fig_path))
#     return flask.send_from_directory(list_of_charts[fig_name], fig_name)

# @app.server.route('{}<image_path>.png'.format(static_image_route))
# def serve_image(image_path):
#     image_name = '{}.png'.format(image_path)
#     if image_name not in list_of_images:
#         raise Exception('"{}" is excluded from the allowed static files'.format(image_path))
#     return flask.send_from_directory(image_directory, image_name)

if __name__ == '__main__':

	# app.run_server(debug=True, processes=1, threaded=True, host='127.0.0.1', port=8050)#, use_reloader=False)
	app.run_server(debug=True)
    # application.run()
