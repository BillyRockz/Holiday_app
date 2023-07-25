from flask import request, render_template, redirect, url_for
from app.views.components import Endpoints
#from app.views.menu import HomeMenu
from app import app


@app.route("/holiday_calendar", methods=["GET", "POST"])
def home_menu():
    """
    This endpoint is the start menu for the holidays api
    it prompts a screen to check the user creds
    """
    if request.method == "POST":
        day = request.form["day"]
        month = request.form["month"]
        year = request.form["year"]
        country = request.form["country"]
        return redirect(url_for('get_holiday', day=day, month=month, year=year, country=country))

    return render_template("home.html")


@app.route("/holiday_calendar/<country>/<month>/<day>/<year>", methods=["GET"])
def get_holiday(country, month, day, year):
    """
    This endpoint makes a call to holidays api to obtain a json
    with the information of that holiday
    :param country: us
    :param month: 12
    :param day: 25
    :param year: 2023
    :return:
        response =
        This holiday is Christmas Day
    """
    try:
        response = Endpoints().obtain_holiday_name(country, month, day, year)
        return render_template("result.html", response=response)
    except:
        msg = "Nope!"
        Exception(msg)

@app.route("/users", methods=["POST"])
def users():
    try:
        pass
        data = request.get()

    except Exception as e:
        pass
