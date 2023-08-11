from flask import render_template, url_for
from app.main import bp
from app.main.forms import InputForm
from scapy.layers.inet import traceroute
import os


@bp.route("/", methods=["GET", "POST"])
@bp.route("/index", methods=["GET", "POST"])
def index():
    form = InputForm()
    res = ""
    if form.validate_on_submit():
        file_path = f"{os.path.abspath(os.getcwd())}\\app\\static\\traceroute.svg"
        os.remove(file_path)
        res, _ = traceroute([form.domain.data], dport=443, maxttl=30)
        res.graph(target=file_path)
    return render_template("index.html", form=form, res=enumerate(res))
