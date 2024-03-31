from dash import Dash, dcc, html
import plotly.express as px
from . import ids

WIND_DATA = px.data.wind()

def render(app: Dash) -> html.Div:
  fig = px.bar(WIND_DATA, x='direction', y='frequency', color='strength', text='strength')
  return html.Div(dcc.Graph(figure=fig), id=ids.BAR_CHART)

