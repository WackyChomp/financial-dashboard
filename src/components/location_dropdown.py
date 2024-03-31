from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from . import ids

def render(app: Dash) -> html.Div:
  all_locations = ['North America', 'South America', 'Europe', 'Asia', 'Africa', 'Australia', 'Antarctica']

  @app.callback(
    Output(ids.LOCATION_DROPDOWN, 'value'),
    Input(ids.SELECT_ALL_LOCATIONS_BUTTON, 'n_clicks')
  )
  def select_all_locations(_:int) -> list[str]:
    return all_locations

  return html.Div(
    children=[
      html.H3('Locations'),
      dcc.Dropdown(
        id=ids.LOCATION_DROPDOWN,
        options=[{'label':location, 'value':location} for location in all_locations],
        value=all_locations,
        multi=True,
      ),
      html.Button(
        className='dropdown-button',
        children=['Select All'],
        id=ids.SELECT_ALL_LOCATIONS_BUTTON
      )
    ]
  )