from app.models.propriedade import Propriedade
from flask import request, jsonify
from app import app, db


@app.route('/propriedades', methods=['GET'])
def get_propriedades():
    propriedades = Propriedade.query.all()
    output = []
    for propriedade in propriedades:
        propriedade_data = {
            'id': propriedade.id,
            'nome_propriedade': propriedade.nome_propriedade,
            'area': propriedade.area,
            'cod_mun': propriedade.cod_mun,
            'valor_aquisicao': propriedade.valor_aquisicao
        }
        output.append(propriedade_data)
    return jsonify({'propriedades': output})


@app.route('/propriedades/<id>', methods=['GET'])
def get_propriedade(id):
    propriedade = Propriedade.query.get(id)
    if not propriedade:
        return jsonify({'message': 'Propriedade não encontrada'}), 404
    propriedade_data = {
        'id': propriedade.cod_propriedade,
        'nome_propriedade': propriedade.nome_propriedade,
        'area': propriedade.area,
        'cod_mun': propriedade.cod_municipio,
        'valor_aquisicao': propriedade.valor_aquisicao
    }
    return jsonify({'propriedade': propriedade_data}), 200


@app.route('/propriedades', methods=['POST'])
def create_propriedade():
    data = request.get_json()
    if not data or 'nome_propriedade' not in data or 'area' not in data or 'cod_mun' not in data or 'valor_aquisicao' not in data:
        return jsonify({'message': 'Dados inválidos para criar Propriedade'}), 400
    new_propriedade = Propriedade(
        nome_propriedade=data['nome_propriedade'],
        area=data['area'],
        cod_municipio=data['cod_mun'],
        valor_aquisicao=data['valor_aquisicao']
    )
    db.session.add(new_propriedade)
    db.session.commit()
    return jsonify({'message': 'Propriedade criada com sucesso'}), 201


@app.route('/propriedades/<id>', methods=['PUT'])
def update_propriedade(id):
    propriedade = Propriedade.query.get(id)
    if not propriedade:
        return jsonify({'message': 'Propriedade não encontrada'}), 404
    data = request.get_json()
    if not data or 'nome_propriedade' not in data or 'area' not in data or 'cod_mun' not in data or 'valor_aquisicao' not in data:
        return jsonify({'message': 'Dados inválidos para atualizar Propriedade'}), 400
    propriedade.nome_propriedade = data['nome_propriedade']
    propriedade.area = data['area']
    propriedade.cod_municipio = data['cod_mun']
    propriedade.valor_aquisicao = data['valor_aquisicao']
    db.session.commit()
    return jsonify({'message': 'Propriedade atualizada com sucesso'}), 200


@app.route('/propriedades/<id>', methods=['DELETE'])
def delete_propriedade(id):
    propriedade = Propriedade.query.get(id)
    if not propriedade:
        return jsonify({'message': 'Propriedade não encontrada'}), 404
    db.session.delete(propriedade)
    db.session.commit()
    return jsonify({'message': 'Propriedade excluída com sucesso'}), 200
