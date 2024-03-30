from dash import Dash, html, dcc
from . import ids

def render(app: Dash) -> html.Div:
  all_locations = ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia', 'Antarctica']

  return html.Div(
    children=[
      html.H3('Locations')
      dcc.Dropdown(
        id=ids.LOCATION_DROPDOWN,
        options=[{'label':location, 'value':location} for location in all_locations],
        value=all_locations,
        multi=True,
      ),
    ]
  )