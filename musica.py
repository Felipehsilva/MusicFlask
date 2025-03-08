from flask import Flask, render_template, request, redirect,session, flash

class Musica:
    def __init__(self, nome, artista, genero):
        self.nome = nome
        self.artista = artista
        self.genero = genero



musica01 = Musica('Temporal','Hungria','Rap')
musica02 = Musica('A sua','Raimundos','Rock')
musica03 = Musica('Vendaval','Fernando e  Sorocaba','Sertanejo')
lista = [musica01,musica02,musica03]

app = Flask(__name__)
'''
@app.route("/inicio")
def hello():
    return "<h1>Hello World</h1>"
'''
app.secret_key = 'aprendendodoiniciocomdaniel'

@app.route("/") # se colocar só / o inves de /musicas vira a homeage
def listarMusicas():

    return render_template('lista_musicas.html',
                           musicas = lista,
                           titulo = "Musicas cadastradas"
                           
                           )


@app.route("/cadastrar") 
def cadastrarMusicas():
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
    return redirect('/')

@app.route("/login") 
def Logar():
    return render_template('login.html',
                           
                           titulo = "Pagina de Login"
                           
                           )

@app.route('/autenticar',methods=['POST',]) 
def autenticar():
    if request.form['txtSenha'] == 'admin':
        session['usuario_logado'] = request.form['txtLogin']
        flash("Usuario Logado com sucesso!")
        return redirect('/')
    else:
        flash("Usuario/Senha invalida")
        return redirect("/login")
    
@app.route('/sair')
def sair():
    session['usuario_logado'] = None
    return redirect('/login')


app.run(debug=True)# debug = True evita ter que rodar manualmente o flask apos cada atualizacao no codigo