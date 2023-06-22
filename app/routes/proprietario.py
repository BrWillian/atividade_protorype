from app.models.proprietario import Proprietario
from flask import request, jsonify
from app import app, db


@app.route('/proprietarios', methods=['GET'])
def get_proprietarios():
    proprietarios = Proprietario.query.all()
    output = []
    for proprietario in proprietarios:
        proprietario_data = {
            'id': proprietario.cod_proprietario,
            'nome_proprietario': proprietario.nome_proprietario,
            'fone1': proprietario.fone1,
            'fone2': proprietario.fone2,
            'fone3': proprietario.fone3
        }
        output.append(proprietario_data)
    return jsonify({'proprietarios': output})


@app.route('/proprietarios/<id>', methods=['GET'])
def get_proprietario(id):
    proprietario = Proprietario.query.get(id)
    if not proprietario:
        return jsonify({'message': 'Proprietário não encontrado'}), 404
    proprietario_data = {
        'id': proprietario.cod_proprietario,
        'nome_proprietario': proprietario.nome_proprietario,
        'fone1': proprietario.fone1,
        'fone2': proprietario.fone2,
        'fone3': proprietario.fone3
    }
    return jsonify({'proprietario': proprietario_data}), 200


@app.route('/proprietarios', methods=['POST'])
def create_proprietario():
    data = request.get_json()
    if not data or 'nome_proprietario' not in data or 'fone1' not in data:
        return jsonify({'message': 'Dados inválidos para criar Proprietário'}), 400
    new_proprietario = Proprietario(
        nome_proprietario=data['nome_proprietario'],
        fone1=data['fone1'],
        fone2=data.get('fone2'),
        fone3=data.get('fone3')
    )
    db.session.add(new_proprietario)
    db.session.commit()
    return jsonify({'message': 'Proprietário criado com sucesso'}), 201


@app.route('/proprietarios/<id>', methods=['PUT'])
def update_proprietario(id):
    proprietario = Proprietario.query.get(id)
    if not proprietario:
        return jsonify({'message': 'Proprietário não encontrado'}), 404
    data = request.get_json()
    if not data or 'nome_proprietario' not in data or 'fone1' not in data:
        return jsonify({'message': 'Dados inválidos para atualizar Proprietário'}), 400
    proprietario.nome_proprietario = data['nome_proprietario']
    proprietario.fone1 = data['fone1']
    proprietario.fone2 = data.get('fone2')
    proprietario.fone3 = data.get('fone3')
    db.session.commit()
    return jsonify({'message': 'Proprietário atualizado com sucesso'}), 200


@app.route('/proprietarios/<id>', methods=['DELETE'])
def delete_proprietario(id):
    proprietario = Proprietario.query.get(id)
    if not proprietario:
        return jsonify({'message': 'Proprietário não encontrado'}), 404
    db.session.delete(proprietario)
    db.session.commit()
    return jsonify({'message': 'Proprietário excluído com sucesso'}), 200