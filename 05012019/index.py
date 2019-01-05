import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly as py


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



body = dbc.Container([
	dbc.Row([
		dbc.Col([
			dbc.Button("Primary", color="primary", className="mr-1"),
        	dbc.Button("Secondary", color="secondary", className="mr-1"),
        	dbc.Button("Success", color="success", className="mr-1")
			], className=['m-5', 'p-2', 'col-4'], style={'border':'solid black thin'}), 
		dbc.Col([])
		])
	])








app.layout = html.Div([body])

if __name__ == '__main__':
	app.run_server(debug = True)