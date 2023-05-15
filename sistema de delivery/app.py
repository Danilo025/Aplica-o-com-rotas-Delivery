from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template("paginas/index.html", \
        titulo_pagina="Página inicial")
    
@app.route("/sobre")
def sobre():
    return render_template("paginas/sobre.html", \
        titulo_pagina="Sobre mim")

@app.route('/contato')
def contato():
    return render_template("paginas/contato.html", \
        titulo_pagina="contato" )

@app.route('/cardapio')
def cardapio():
    return render_template("paginas/cardapio.html", \
        titulo_pagina="cardapio" )

@app.route('/pedidos')
def pedidos():
    return render_template("paginas/pedidos.html", \
        titulo_pagina="pedidos" )

@app.route("/teste")
def teste():
    return "teste"
    
if __name__ == "__main__":
    app.run(debug=True)