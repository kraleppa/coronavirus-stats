from flask import Flask, render_template
from PlotImageParse import create_plot
from TypeEnum import Type

app = Flask(__name__)


@app.route("/")
def landing_page():
    return render_template('landing_page.html')


@app.route("/infections")
def infections():
    create_plot(Type.CONFIRMED)
    return render_template('infections.html')


@app.route("/in_quarantine")
def in_quarantine():
    create_plot(Type.IN_QUARANTINE)
    return render_template('in_quarantine.html')


@app.route("/number_of_tests")
def number_of_tests():
    create_plot(Type.NUMBER_OF_TESTS)
    return render_template('number_of_tests.html')


@app.route("/daily_number_of_tests")
def daily_number_of_tests():
    create_plot(Type.DAILY_NUMBER_OF_TESTS)
    return render_template('daily_number_of_tests.html')


if __name__ == '__main__':
    app.run(debug=True)
