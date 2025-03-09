from flask import Flask, render_template, request, redirect,session, flash, url_for

class Musica:
    def __init__(self, nome, artista, genero):
        self.nome = nome
        self.artista = artista
        self.genero = genero



musica01 = Musica('Temporal','Hungria','Rap')
musica02 = Musica('A sua','Raimundos','Rock')
musica03 = Musica('Vendaval','Fernando e  Sorocaba','Sertanejo')
lista = [musica01,musica02,musica03]

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


app = Flask(__name__)  
'''
@app.route("/inicio")
def hello():
    return "<h1>Hello World</h1>"
'''
app.secret_key = 'aprendendodoiniciocomdaniel'

@app.route("/") # se colocar só / o inves de /musicas vira a homeage
def listarMusicas():
    if session['usuario_logado'] == None or 'usuario_logado' not in session:
        return redirect(url_for('logar'))
    
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
    name = request.form['txtNome']
    artista = request.form['txtArtista']
    genero = request.form['txtGenero']
    novaMusica = Musica(name,artista,genero)
    lista.append(novaMusica)
    return redirect(url_for('listarMusicas'))

@app.route("/login") 
def logar():
    return render_template('login.html',
                           
                           titulo = "Pagina de Login"
                           
                           )

@app.route('/autenticar',methods=['POST',]) 
def autenticar():
    if request.form['txtLogin'] in usuarios:
        usuarioEncontrado = usuarios[request.form['txtLogin']]
        if request.form['txtSenha'] == usuarioEncontrado.senha:
            session['usuario_logado'] = request.form['txtLogin']
            flash(f"Usuario {usuarioEncontrado.login} Logado com sucesso!")
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