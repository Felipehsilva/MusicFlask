from flask import Flask, render_template, request, redirect,session, flash, url_for
from flask_sqlalchemy import SQLAlchemy  


app = Flask(__name__)  

@app.route("/inicio")
def hello():
    return "<h1>Hello World</h1>"

app.secret_key = 'aprendendodoiniciocomdaniel'

app.config['SQLALCHEMY_DATABASE_URI'] = \
'{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
    SGBD = 'mysql+mysqlconnector',
    usuario = 'root',
    senha = '123456',
    servidor = 'localhost',
    database = 'playMusica'

)

db = SQLAlchemy(app)


class Musica(db.Model):
    # a variavel tem que ser o mesmo nome do campo da tabela
    id_musica = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_musica= db.Column(db.String(50), nullable=False)
    cantor_banda = db.Column(db.String(50), nullable=False)
    genero_musica = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name


class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome_usuario = db.Column(db.String(50), nullable=False)
    login_usuario = db.Column(db.String(20), nullable=False)
    senha_usuario  = db.Column(db.String(15), nullable=False)

    def __repr__(self):
        return '<Name %r>' % self.name

'''
class Usuario:
    def __init__(self, nome, login, senha):
        self.nome = nome
        self.login = login
        self.senha = senha

usuario01 = Usuario('Felipe','felipe','admin')
usuario02 = Usuario('Ze Ruela','zruela','1234')
usuario03 = Usuario('joao','joao','654321')

usuarios = {
    usuario01.login:usuario01,
    usuario02.login:usuario02,
    usuario03.login:usuario03
}
'''


@app.route("/") # se colocar só / o inves de /musicas vira a homeage
def listarMusicas():
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('logar'))
    
    lista  =Musica.query.order_by(Musica.id_musica)
    
    return render_template('lista_musicas.html',
                           musicas = lista,
                           titulo = "Musicas cadastradas"
                           
                           )


@app.route("/cadastrar") 
def cadastrarMusicas():
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('logar'))


    return render_template('cadastra_musica.html',
                           
                           titulo = "Cadastrar Musica"
                           
                           )


@app.route('/adicionar',methods=['POST'])
def adicionar_musica():
    nome = request.form['txtNome']
    artista = request.form['txtArtista']
    genero = request.form['txtGenero']


    musica = Musica.query.filter_by(nome_musica = nome).first() # esta sendo feita uma query no banco buscando para ver se existe um registro com o nome da variavel "nome", se tiver traz apenas o primeiro registro

    if musica: # verifica se a musica ja esta cadastrada (vamos limitar para nao ter duplicada)
        flash("Musica ja esta cadastrada")
        return redirect(url_for('listarMusicas'))
    nova_musica = Musica(nome_musica = nome, cantor_banda = artista, genero_musica = genero)
    db.session.add(nova_musica)
    db.session.commit()
    return redirect(url_for('listarMusicas'))


 
    

@app.route("/login") 
def logar():
    return render_template('login.html',
                           
                           titulo = "Pagina de Login"
                           
                           )

@app.route('/autenticar',methods=['POST',]) 
def autenticar():
    usuario = Usuario.query.filter_by(login_usuario = request.form['txtLogin']).first()


    if usuario:
        
        if request.form['txtSenha'] == usuario.senha_usuario:
            session['usuario_logado'] = request.form['txtLogin']
            flash(f"Usuario {usuario.login_usuario} Logado com sucesso!")
            return redirect(url_for('listarMusicas'))
        else:
            flash("Senha Invalida")
            return redirect(url_for('logar'))
    else:
        flash("Usuario/Senha invalida")
        return redirect(url_for('logar'))
    
@app.route('/sair')
def sair():
    session['usuario_logado'] = None
    return redirect(url_for('logar'))


app.run(debug=True)# debug = True evita ter que rodar manualmente o flask apos cada atualizacao no codigo