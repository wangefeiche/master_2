from flask import Flask, render_template, request
from flask_plotly.script import create_plot

app = Flask(__name__)


@app.route('/')
def index():
    bar = create_plot.create_plot()
    return render_template('index.html',
                           plot=bar)

@app.route('/bar', methods=['GET', 'POST'])
def change_features():

    feature = request.args['selected']
    graphJSON= create_plot.new_create_plot(feature)

    return graphJSON

if __name__ == '__main__':
    app.run()