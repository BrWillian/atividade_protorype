from app.models.produto import Produto, Producao
from flask import request, jsonify, render_template
from app import app, db


@app.route('/produto')
def index_produto():
    return render_template('produto.html')


@app.route('/produtos', methods=['GET'])
def get_produtos():
    produtos = Produto.query.all()
    output = []
    for produto in produtos:
        produto_data = {
            'cod_produto': produto.cod_produto,
            'desc_produto': produto.desc_produto
        }
        output.append(produto_data)
    return jsonify({'produtos': output})


@app.route('/produtos/<int:id>', methods=['GET'])
def get_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404
    produto_data = {
        'cod_produto': produto.cod_produto,
        'desc_produto': produto.desc_produto
    }
    return jsonify({'produto': produto_data}), 200


@app.route('/produtos', methods=['POST'])
def create_produto():
    data = request.get_json()
    if not data or 'desc_produto' not in data:
        return jsonify({'message': 'Dados inválidos para criar Produto'}), 400
    new_produto = Produto(
        desc_produto=data['desc_produto']
    )
    db.session.add(new_produto)
    db.session.commit()
    return jsonify({'message': 'Produto criado com sucesso'}), 201


@app.route('/produtos/<int:id>', methods=['PUT'])
def update_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404
    data = request.get_json()
    if not data or 'desc_produto' not in data:
        return jsonify({'message': 'Dados inválidos para atualizar Produto'}), 400
    produto.desc_produto = data['desc_produto']
    db.session.commit()
    return jsonify({'message': 'Produto atualizado com sucesso'}), 200


@app.route('/produtos/<int:id>', methods=['DELETE'])
def delete_produto(id):
    produto = Produto.query.get(id)
    if not produto:
        return jsonify({'message': 'Produto não encontrado'}), 404
    db.session.delete(produto)
    db.session.commit()
    return jsonify({'message': 'Produto excluído com sucesso'}), 200


@app.route('/producoes', methods=['GET'])
def get_producoes():
    producoes = Producao.query.all()
    output = []
    for producao in producoes:
        producao_data = {
            'cod_propriedade': producao.cod_propriedade,
            'cod_produto': producao.cod_produto,
            'mes_ini_colheita_prov': producao.mes_ini_colheita_prov,
            'mes_fin_colheita_prov': producao.mes_fin_colheita_prov,
            'qtd_prov_colheita': producao.qtd_prov_colheita,
            'mes_ini_colheita_real': producao.mes_ini_colheita_real,
            'mes_fin_colheita_real': producao.mes_fin_colheita_real,
            'qtd_real_colhida': producao.qtd_real_colhida
        }
        output.append(producao_data)
    return jsonify({'producoes': output}), 200


@app.route('/producoes/<int:id>', methods=['GET'])
def get_producao(id):
    producao = Producao.query.get(id)
    if not producao:
        return jsonify({'message': 'Produção não encontrada'}), 404
    producao_data = {
        'cod_propriedade': producao.cod_propriedade,
        'cod_produto': producao.cod_produto,
        'mes_ini_colheita_prov': producao.mes_ini_colheita_prov,
        'mes_fin_colheita_prov': producao.mes_fin_colheita_prov,
        'qtd_prov_colheita': producao.qtd_prov_colheita,
        'mes_ini_colheita_real': producao.mes_ini_colheita_real,
        'mes_fin_colheita_real': producao.mes_fin_colheita_real,
        'qtd_real_colhida': producao.qtd_real_colhida
    }
    return jsonify({'producao': producao_data}), 200


@app.route('/producoes', methods=['POST'])
def create_producao():
    data = request.get_json()
    if not data or 'cod_propriedade' not in data or 'cod_produto' not in data or 'mes_ini_colheita_prov' not in data or 'mes_fin_colheita_prov' not in data or 'qtd_prov_colheita' not in data or 'mes_ini_colheita_real' not in data or 'mes_fin_colheita_real' not in data or 'qtd_real_colhida' not in data:
        return jsonify({'message': 'Dados inválidos para criar Produção'}), 400
    new_producao = Producao(
        cod_propriedade=data['cod_propriedade'],
        cod_produto=data['cod_produto'],
        mes_ini_colheita_prov=data['mes_ini_colheita_prov'],
        mes_fin_colheita_prov=data['mes_fin_colheita_prov'],
        qtd_prov_colheita=data['qtd_prov_colheita'],
        mes_ini_colheita_real=data['mes_ini_colheita_real'],
        mes_fin_colheita_real=data['mes_fin_colheita_real'],
        qtd_real_colhida=data['qtd_real_colhida']
    )
    db.session.add(new_producao)
    db.session.commit()
    return jsonify({'message': 'Produção criada com sucesso'}), 201


@app.route('/producoes/<int:id>', methods=['PUT'])
def update_producao(id):
    producao = Producao.query.get(id)
    if not producao:
        return jsonify({'message': 'Produção não encontrada'}), 404
    data = request.get_json()
    if not data or 'cod_propriedade' not in data or 'cod_produto' not in data or 'mes_ini_colheita_prov' not in data or 'mes_fin_colheita_prov' not in data or 'qtd_prov_colheita' not in data or 'mes_ini_colheita_real' not in data or 'mes_fin_colheita_real' not in data or 'qtd_real_colhida' not in data:
        return jsonify({'message': 'Dados inválidos para atualizar Produção'}), 400
    producao.cod_propriedade = data['cod_propriedade']
    producao.cod_produto = data['cod_produto']
    producao.mes_ini_colheita_prov = data['mes_ini_colheita_prov']
    producao.mes_fin_colheita_prov = data['mes_fin_colheita_prov']
    producao.qtd_prov_colheita = data['qtd_prov_colheita']
    producao.mes_ini_colheita_real = data['mes_ini_colheita_real']
    producao.mes_fin_colheita_real = data['mes_fin_colheita_real']
    producao.qtd_real_colhida = data['qtd_real_colhida']
    db.session.commit()
    return jsonify({'message': 'Produção atualizada com sucesso'}), 200


@app.route('/producoes/<int:id>', methods=['DELETE'])
def delete_producao(id):
    producao = Producao.query.get(id)
    if not producao:
        return jsonify({'message': 'Produção não encontrada'}), 404
    db.session.delete(producao)
    db.session.commit()
    return jsonify({'message': 'Produção excluída com sucesso'}), 200
