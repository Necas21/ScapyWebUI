from flask import render_template
from app.main import bp
from app.main.forms import InputForm
from scapy.all import *


@bp.route("/")
@bp.route("/index")
def index():
    return render_template("index.html")