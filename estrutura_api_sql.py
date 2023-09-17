from flask import Flask # Este modulo nos permitira criar a API Flask
from flask_sqlalchemy import SQLAlchemy # Este modulo nos permitira criar o banco de dados

# Criar uma api flask
app = Flask(__name__)

# Criar uma instancia de SQLAlchemy
app.config['SECRET_KEY'] = '@J@o@a@o!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'

db = SQLAlchemy(app) # Funcionalidades do banco de dados
db: SQLAlchemy # Definindo estaticamente o tipo da variavel

# Difinir a estrutura da tabela postagem
class Postagem(db.Model): # id_postagem, titulo, autor
    # Definindo o nome da tabela
    __tabblename__ = 'postagem'
    id_postagem = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String)
    id_autor = db.Column(db.Integer, db.ForeignKey('autor.id_autor')) # ForeignKey -> Chave estrangeira


# Difinir a estrutura da tabela autor    
class Autor(db.Model): # id_autor, nome, email, senha, admin, postagens
    __tablename__ = 'autor'
    id_autor = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)
    Postagens = db.relationship('Postagem')


def inicializar_banco():
    # Executar o comando para executar o banco de dados
    with app.app_context():
        db.create_all()


    with app.app_context():
        # Criar usuarios administradores
        autor = Autor(nome='Joao', email='joao@gmail.com', senha='1234', admin=True)
        db.session.add(autor) # Adicionando usuario
        db.session.commit() # Salvando os dados
        
if __name__ == "__main__":
    inicializar_banco()

