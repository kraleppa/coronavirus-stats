from flask import Flask, render_template
from PlotImageParse import create_plot, refresh_plots
from DataService import refresh_data
from flask import make_response, jsonify
from flask import send_file

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route("/refresh")
def refresh():
    refresh_data()
    refresh_plots()
    res = make_response(jsonify({"message": "Data updated"}), 201)
    return res


@app.route("/")
def landing_page():
    return render_template('landing_page.html')


@app.route("/infections")
def infections():
    return send_file("static/images/Liczba przypadków zachorowań na COVID-19.png", mimetype='image/png')


@app.route("/in_quarantine")
def in_quarantine():
    return send_file("static/images/Liczba osób poddanych kwarantannie.png", mimetype='image/png')


@app.route("/number_of_tests")
def number_of_tests():
    return send_file("static/images/Liczba przeprowadzonych testów na COVID-19.png", mimetype='image/png')


@app.route("/daily_number_of_tests")
def daily_number_of_tests():
    return send_file("static/images/Dzienna liczba przeprowadzonych testów na COVID-19.png", mimetype='image/png')
