from flask import Flask, render_template, flash, redirect, request
from database import db
from flask_migrate import Migrate
from models import Imoveis

app = Flask(__name__)
app.config["SECRET_KEY"] = "9970626666560a32465d4ce10d28f3233365af833e15eed59884d9477862c379"

conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/bd_imoveis" # meu banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template("index.html")

@app.route("/imoveis")
def imoveis():
    i = Imoveis.query.all()
    return render_template("imoveis.html", dados=i)

@app.route("/imoveis/add")
def imoveis_add():
    return render_template("imoveis_add.html")

@app.route("/imoveis/save", methods=["POST"])
def save():
    endereco = request.form.get("endereco")
    tipo = request.form.get("tipo")
    valor = request.form.get("valor")
    if endereco and tipo and valor:
        imoveis = Imoveis(endereco, tipo, valor)
        db.session.add(imoveis)
        db.session.commit()
        flash("Imóvel cadastrado")
        return redirect('/imoveis')
    else:
        flash("Preencha todos os campos")
        return redirect('/imoveis/add')
    
@app.route("/imoveis/remove/<int:id>")
def imoveis_remove(id):
    imoveis = Imoveis.query.get(id)
    if imoveis:
        db.session.delete(imoveis)
        db.session.commit()
        flash("Imóvel removido!!")
        return redirect("/imoveis")
    else:
        flash("Caminho Incorreto!!")
        return redirect("/imoveis")

@app.route("/imoveis/edit/<int:id>")
def imoveis_edit(id):
    try:
        imoveis = Imoveis.query.get(id)
        return render_template("imoveis_edit.html", dados=imoveis)
    except:
        flash("Imóvel Inválido")
        return redirect("/imoveis")
    
@app.route("/imoveis/editsave", methods=["POST"])
def imoveis_edit_save():
    id = request.form.get("id")
    endereco = request.form.get("endereco")
    tipo = request.form.get("tipo")
    valor = request.form.get("valor")
    if id and endereco and tipo and valor:
        imoveis = Imoveis.query.get(id)
        imoveis.endereco = endereco
        imoveis.tipo = tipo
        imoveis.valor = valor
        db.session.commit()
        flash("Dados alterados com sucesso!!")
        return redirect("/imoveis")
    else:
        flash("Preencha todas as informações")
        return redirect("/imoveis")

if __name__ == '__main__':
    app.run()