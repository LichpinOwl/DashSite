import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly as py


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])



body = dbc.Container([
	dbc.Navbar(
		children=[
		dbc.NavItem(dbc.NavLink("Link", href="#")),
		dbc.DropdownMenu(
			nav=True,
			in_navbar=True,
			label="Menu",
			children=[
			dbc.DropdownMenuItem("Entry 1"),
			dbc.DropdownMenuItem("Entry 2"),
			dbc.DropdownMenuItem(divider=True),
			dbc.DropdownMenuItem("Entry 3"),
			],
			),
		],
		brand="Demo",
		brand_href="#",
		sticky="top",
		),
	dbc.Row(
		[
		dbc.Jumbotron([
			html.Div([html.H1("Test Charts")])
			], 
			className=['m-1', 'col-12', 'bg-warning'])
		]),


	dbc.Row([
		dbc.Col(
			[
			dbc.Button("\xD9\x86\xD8\xA7\xD9\x85\x20\xD8\xAA\xD8\xB3\xD8\xAA", color="primary", className="mr-1", size='lg', outline='true'),
			dbc.Button("\xD9\x86\xD8\xA7\xD9\x85\x20\xD9\x85\xD8\xAD\xD8\xB5\xD9\x88\xD9\x84", color="secondary", className="mr-1", outline='true', size='lg'),
			dbc.Button("\xD9\xBE\xD9\x84\xD8\xAA\xD9\x81\xD9\x88\xD8\xB1\xD9\x85", color="success", className="mr-1", outline='true', size='lg')
			], 
			className=['m-1', 'p-2', 'col-12', 'd-flex', 'justify-content-center'], style={'border':'solid black thin', "font-family" : "sans-serif"}
			), 
		
		dbc.Col([])
		])

	], #className=['bg-secondary']
	)














app.layout = html.Div([body])

if __name__ == '__main__':
	app.run_server(debug = True)