from flask import Flask
from flask import render_template
from analysis import Analyzer

app = Flask(__name__)
analyzer = Analyzer()

@app.route("/")
def hello():
	return render_template("index.html")

@app.route("/confirmados")
def confirmados():
  	return analyzer.confirmados

@app.route("/obitos")
def obitos():
	return analyzer.obitos

@app.route("/tx_obitos")
def tx_obitos():
    return analyzer.tx_obitos

@app.route("/recuperados")
def recuperados():
    return analyzer.recuperados

@app.route("/tx_recuperados")
def tx_recuperados():
    return analyzer.tx_recuperados

@app.route("/isolamento")
def isolamento():
    return analyzer.isolamento

@app.route("/tx_isolamento")
def tx_isolamento():
    return analyzer.tx_isolamento

@app.route("/enfermaria")
def enfermaria():
    return analyzer.enfermaria

@app.route("/leitos_enf")
def leitos_enf():
    return analyzer.leitos_enf

@app.route("/tx_oc_enf")
def tx_oc_enf():
    return analyzer.tx_oc_enf

@app.route("/tx_enfermaria")
def tx_enfermaria():
    return analyzer.tx_enfermaria

@app.route("/uti")
def uti():
    return analyzer.uti

@app.route("/leitos_uti")
def leitos_uti():
    return analyzer.leitos_uti

@app.route("/tx_uti")
def tx_uti():
    return analyzer.tx_uti

@app.route("/tx_oc_uti")
def tx_oc_uti():
    return analyzer.tx_oc_uti

@app.route("/testes_novos")
def testes_novos():
    return analyzer.testes_novos

@app.route("/testes_acumulados")
def testes_acumulados():
    return analyzer.testes_acumulados

@app.route("/tx_testes")
def tx_testes():
    return analyzer.tx_testes
