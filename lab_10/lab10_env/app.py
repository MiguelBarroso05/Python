"""
### 2 Configuração do Flask ###
# 2.2.3 Configuração do Flask #
from flask import Flask

# Criar a aplicacao Flask
app = Flask(__name__)

# Definir a rota principal
@app.route('/')
def home():
    return "Olá, Flask!"

# Iniciar a aplicacao no modo de debug
if __name__ == '__main__':
    app.run(debug=True)


### 3 Construção de uma API ###
# 3.1.1 Operação GET #
@app.route('/produtos', methods=['GET'])
def get_produtos():
    # Retorna uma lista de produtos
    produtos = ["Produto1", "Produto2", "Produto3"]
    return {"produtos": produtos}


# 3.1.2 Operação POST #
@app.route('/produtos', methods=['POST'])
def add_produto():
    # Adiciona um novo produto
    novo_produto = {"nome": "Produto4", "preco": 20.0}
    return {"message": "Produto adicionado com sucesso!", "produto": novo_produto}, 201


# 3.1.3 Operação PUT #
@app.route('/produtos/<int:id>', methods=['PUT'])
def update_produto(id):
    # Atualiza as informacoes de um produto existente    
    produto_atualizado = {"id": id, "nome": "Produto Atualizado", "preco": 25.0}
    return {"message": "Produto atualizado com sucesso!", "produto": produto_atualizado}


# 3.1.4 Operação DELETE #
@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    # Apaga um produto com base no ID fornecido
    return {"message": f"Produto {id} apagado com sucesso!"}, 200
"""

### 4 Integração com Base de Dados ###
## 4.1 Instalação e configuração ##
# 4.1.2 Configurar o SQLAlchemy no Flask #
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask( __name__ )

# Configuracao do URI da base de dados
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #Desativa o historico de alterações

# Inicialização do SQLAlchemy
db = SQLAlchemy(app)




# 4.1.3 Definir um modelo (classe) para uma tabela #
class Produto(db.Model):
    # Definição das colunas da tabela
    id = db.Column(db.Integer, primary_key = True ) #Chave primária
    nome = db.Column(db.String(80), nullable = False ) #Nome do produto, não pode ser nulo
    
    def __repr__(self):
        return f'<Produto {self.nome}>'
    


@app.route('/')
def home():
    return "Olá, Flask!"

## 4.2 Operações CRUD com SQLAlchemy ##
# 4.2.1 Criar um Produto (POST) #
@app.route('/produtos', methods=['POST'])
def add_produto():
    nome = request.json.get('nome')
    novo_produto = Produto(nome=nome)
    db.session.add(novo_produto)
    db.session.commit()

    return {
        "message": "Produto adicionado com sucesso!",
        "produto": {"id": novo_produto.id, "nome": novo_produto.nome}
    }, 201


# 4.2.2 Ler Produtos (GET) #
@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    return {
        "produtos": [{"id": p.id, "nome": p.nome} for p in produtos]
    }


# 4.2.3 Atualizar um Produto (PUT) #
@app.route('/produtos/<int:id>', methods=['PUT'])
def update_produto(id):
    produto = Produto.query.get_or_404(id) #Obtém o produto com o id fornecido
    produto.nome = request.json.get('nome', produto.nome) #Atualiza o nome, se fornecido
    db.session.commit() #Guarda as alterações

    return {
        "message": "Produto atualizado com sucesso!",
        "produto": {"id": produto.id, "nome": produto.nome}
    }


# 4.2.4 Apagar um Produto (DELETE) #
@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    produto = Produto.query.get_or_404(id) #Obtém o produto com o id fornecido
    db.session.delete(produto) #Remove o produto
    db.session.commit() #Confirma a exclusão

    return {
        "message": f"Produto {id} apagado com sucesso!"
        }, 200

if __name__ == '__main__':
    # 4.1.4 Criar a Base de Dados #
    # Cria todas as tabelas na base de dados
    with app.app_context():
        db.create_all()

    app.run(debug=True)