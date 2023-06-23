from flask import request, jsonify, render_template
from app.models.propriedade import Municipio
from app import db, app

@app.route('/municipio')
def index_municipios():
    return render_template('municipio.html')

@app.route('/municipios', methods=['GET'])
def get_municipios():
    municipios = Municipio.query.all()
    output = []
    for municipio in municipios:
        municipio_data = {
            'nome_municipio': municipio.nome_municipio,
            'uf_municipio': municipio.uf_municipio
        }
        output.append(municipio_data)
    return jsonify({'municipios': output}), 200


@app.route('/municipios/<nome_municipio>', methods=['GET'])
def get_municipio(nome_municipio):
    municipio = Municipio.query.filter_by(nome_municipio=nome_municipio).first()
    if not municipio:
        return jsonify({'message': 'Município não encontrado'}), 404
    municipio_data = {
        'nome_municipio': municipio.nome_municipio,
        'uf_municipio': municipio.uf_municipio
    }
    return jsonify({'municipio': municipio_data}), 200


@app.route('/municipios', methods=['POST'])
def create_municipio():
    data = request.get_json()
    if not data or 'nome_municipio' not in data or 'uf_municipio' not in data:
        return jsonify({'message': 'Dados do município ausentes ou inválidos'}), 400
    new_municipio = Municipio(
        nome_municipio=data['nome_municipio'],
        uf_municipio=data['uf_municipio']
    )
    db.session.add(new_municipio)
    db.session.commit()
    return jsonify({'message': 'Município criado com sucesso'}), 201


@app.route('/municipios/<nome_municipio>', methods=['PUT'])
def update_municipio(nome_municipio):
    municipio = Municipio.query.filter_by(nome_municipio=nome_municipio).first()
    if not municipio:
        return jsonify({'message': 'Município não encontrado'}), 404
    data = request.get_json()
    if not data or 'nome_municipio' not in data or 'uf_municipio' not in data:
        return jsonify({'message': 'Dados do município ausentes ou inválidos'}), 400
    municipio.nome_municipio = data['nome_municipio']
    municipio.uf_municipio = data['uf_municipio']
    db.session.commit()
    return jsonify({'message': 'Município atualizado com sucesso'}), 200


@app.route('/municipios/<nome_municipio>', methods=['DELETE'])
def delete_municipio(nome_municipio):
    municipio = Municipio.query.filter_by(nome_municipio=nome_municipio).first()
    if not municipio:
        return jsonify({'message': 'Município não encontrado'}), 404
    db.session.delete(municipio)
    db.session.commit()
    return jsonify({'message': 'Município excluído com sucesso'}), 200
