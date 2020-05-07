import dash
import dash_html_components as html

from flask import Flask

server = Flask(__name__)
app = dash.Dash(server=server)
app.layout = html.Div("Hello world.")

if __name__ == '__main__':
    app.run_server()
