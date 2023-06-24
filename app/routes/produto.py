from app.models.produto import Produto, Producao
from app.models.propriedade import Propriedade
from app.models.proprietario import ProprietarioPropriedade, Proprietario, DonoPJ
from flask import request, jsonify, render_template
from sqlalchemy import func
from datetime import datetime
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
        mes_ini_colheita_prov=datetime.strptime(data['mes_ini_colheita_prov'], '%d/%m/%Y'),
        mes_fin_colheita_prov=datetime.strptime(data['mes_fin_colheita_prov'], '%d/%m/%Y'),
        qtd_prov_colheita=data['qtd_prov_colheita'],
        mes_ini_colheita_real=datetime.strptime(data['mes_ini_colheita_real'],'%d/%m/%Y'),
        mes_fin_colheita_real=datetime.strptime(data['mes_fin_colheita_real'],'%d/%m/%Y'),
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
    producao.mes_ini_colheita_prov = datetime.strptime(data['mes_ini_colheita_prov'], '%d/%m/%Y')
    producao.mes_fin_colheita_prov = datetime.strptime(data['mes_fin_colheita_prov'], '%d/%m/%Y')
    producao.qtd_prov_colheita = data['qtd_prov_colheita']
    producao.mes_ini_colheita_real = datetime.strptime(data['mes_ini_colheita_real'], '%d/%m/%Y')
    producao.mes_fin_colheita_real = datetime.strptime(data['mes_fin_colheita_real'], '%d/%m/%Y')
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


@app.route('/maior_rendimento_milho', methods=['GET'])
def maior_rendimento_milho():
    # Query to retrieve the properties with the highest corn harvest yield in 2022
    query = db.session.query(
        Propriedade.nome_propriedade,
        Proprietario.cod_proprietario,
        (db.func.sum(Producao.qtd_real_colhida)).label('rendimento')
    ).join(ProprietarioPropriedade, Propriedade.cod_propriedade == ProprietarioPropriedade.cod_propriedade) \
     .join(Proprietario, ProprietarioPropriedade.cod_proprietario == Proprietario.cod_proprietario) \
     .join(Producao, Propriedade.cod_propriedade == Producao.cod_propriedade) \
     .join(Produto, Producao.cod_produto == Produto.cod_produto) \
     .filter(db.extract('year', Producao.mes_ini_colheita_real) == 2022) \
     .filter(Produto.desc_produto == 'Milho') \
     .group_by(Propriedade.nome_propriedade, Proprietario.cod_proprietario) \
     .all()

    print(query)

    # Prepare the response
    response = []
    for row in query:
        property_data = {
            'nome_propriedade': row.nome_propriedade,
            'nome_proprietario': row.cod_proprietario,
            'rendimento': float(row.rendimento)
        }
        response.append(property_data)

    return jsonify(response)


@app.route('/producao_anual', methods=['GET'])
def get_producao_anual_2023():
    producao_anual = db.session.query(
        Propriedade.nome_propriedade,
        Propriedade.area,
        Produto.desc_produto,
        func.sum(Producao.qtd_real_colhida).label('qtd_total_colhida'),
        func.min(Producao.mes_ini_colheita_real).label('mes_ini_colheita_real'),
        func.max(Producao.mes_fin_colheita_real).label('mes_fin_colheita_real')
    ).join(Producao, Propriedade.cod_propriedade == Producao.cod_propriedade) \
        .join(Produto, Produto.cod_produto == Producao.cod_produto) \
        .filter(Producao.mes_ini_colheita_real >= '2023-01-01', Producao.mes_fin_colheita_real <= '2023-12-31') \
        .group_by(Propriedade.nome_propriedade, Propriedade.area, Produto.desc_produto).all()

    result = []

    for item in producao_anual:
        result.append({
            'nome_propriedade': item.nome_propriedade,
            'tamanho': item.area,
            'desc_produto': item.desc_produto,
            'qtd_total_colhida': float(item.qtd_total_colhida),
            'data_colheita': str(item.mes_ini_colheita_real) + ' - ' + str(item.mes_fin_colheita_real)
        })
    return jsonify(result)
