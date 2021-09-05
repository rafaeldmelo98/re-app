from flask import Flask, render_template

app = Flask(__name__)

BASEDIR = '/run/media/rafael/OS/Projetos/re-app/'

@app.route("/")
def ola():
    return render_template('pagina_inicial.html')

app.run(debug=True)
