from flask import Blueprint, render_template, request, session
from .engine import AviatorEngine

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():

    resultado = None

    if "saldo" not in session:
        session["saldo"] = 100

    engine = AviatorEngine(session["saldo"])

    if request.method == "POST":

        aposta = float(request.form["aposta"])
        cashout = float(request.form["cashout"])

        resultado = engine.rodada(aposta, cashout)

        session["saldo"] = engine.saldo

    return render_template(
        "index.html",
        saldo=session["saldo"],
        resultado=resultado
    )