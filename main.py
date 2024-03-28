#!/usr/bin/env python3

from dash import Dash, html

def main():
  app = Dash()
  app.title = 'Analytics Visualized'
  app.layout = html.Div()
  app.run()

if __name__ == '__main__':
  main()