"""
main.py : The Dice Rolling Simulation!
Why roll hundreds of dice for a D&D session
when you can just do them all in advance, 
in literal microseconds!! Save time and surprise, 
and introduce the strategy of saving those rolls!

OOP and Web (Flask) friendly.
"""

from flask import Flask, flash, render_template, redirect, request
import simulation
from simulation import DiceRollSimulation
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
import sentry_sdk
from flask import Flask
from sentry_sdk.integrations.flask import FlaskIntegration

"""
    A bug hunting, Flask friendly service. 
    Sends aggregated bug alerts to my email.
"""
sentry_sdk.init(
    dsn="https://4cc80b3231ff473db55edd5aaaade132@o554551.ingest.sentry.io/5683234",
    integrations=[FlaskIntegration()],
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Home page
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        """ 
        Takes user input and creates
        a simulation via DiceRollSimulation()
        """
        die_type = request.form.get("die_type")
        roll_count = request.form.get("roll_count")
        user_sim = DiceRollSimulation(die_type, roll_count)
        print(" here at / ")
        return render_template("index.html", user_sim=user_sim, 
                die_type=die_type, roll_count=roll_count)
    else:
        return render_template("index.html")

@app.route('/debug-sentry')
def trigger_error():
    division_by_zero = 1 / 0

def errorhandler(e):
    """Handles error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return render_template("apology.html")

# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)

if __name__== '__main__':
    app.run()