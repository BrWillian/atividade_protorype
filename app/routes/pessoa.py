from flask import request, jsonify, render_template
from app.models.pessoa import PessoaFisica, PessoaJuridica
from app import db, app
import datetime


@app.route('/pessoa')
def index_pessoas():
    return render_template('pessoa.html')


@app.route('/pessoas_fisicas', methods=['GET'])
def get_pessoas_fisicas():
    pessoas_fisicas = PessoaFisica.query.all()
    output = []
    for pessoa_fisica in pessoas_fisicas:
        pessoa_fisica_data = {
            'cod_prop_pf': pessoa_fisica.cod_prop_pf,
            'cpf_prop': pessoa_fisica.cpf_prop,
            'nome_pf': pessoa_fisica.nome_pf,
            'dt_nasc_pf': pessoa_fisica.dt_nasc_pf.strftime('%Y-%m-%d'),
            'rg_pf': pessoa_fisica.rg_pf,
            'cod_prop_conjuge': pessoa_fisica.cod_prop_conjuge
        }
        output.append(pessoa_fisica_data)
    return jsonify({'pessoas_fisicas': output}), 200


@app.route('/pessoas_fisicas/<id>', methods=['GET'])
def get_pessoa_fisica(id):
    pessoa_fisica = PessoaFisica.query.get(id)
    if not pessoa_fisica:
        return jsonify({'message': 'Pessoa Física não encontrada'}), 404
    pessoa_fisica_data = {
        'cod_prop_pf': pessoa_fisica.cod_prop_pf,
        'cpf_prop': pessoa_fisica.cpf_prop,
        'nome_pf': pessoa_fisica.nome_pf,
        'dt_nasc_pf': pessoa_fisica.dt_nasc_pf.strftime('%Y-%m-%d'),
        'rg_pf': pessoa_fisica.rg_pf,
        'cod_prop_conjuge': pessoa_fisica.cod_prop_conjuge
    }
    return jsonify({'pessoa_fisica': pessoa_fisica_data}), 200


@app.route('/pessoas_fisicas', methods=['POST'])
def create_pessoa_fisica():
    data = request.get_json()
    if not data or 'cod_prop_pf' not in data or 'cpf_prop' not in data or 'nome_pf' not in data or 'dt_nasc_pf' not in data or 'rg_pf' not in data:
        return jsonify({'message': 'Dados da Pessoa Física ausentes ou inválidos'}), 400
    new_pessoa_fisica = PessoaFisica(
        cod_prop_pf=data['cod_prop_pf'],
        cpf_prop=data['cpf_prop'],
        nome_pf=data['nome_pf'],
        dt_nasc_pf=datetime.datetime.strptime(data['dt_nasc_pf'], '%Y-%m-%d').date(),
        rg_pf=data['rg_pf'],
        cod_prop_conjuge=data['cod_prop_conjuge']
    )
    db.session.add(new_pessoa_fisica)
    db.session.commit()
    return jsonify({'message': 'Pessoa Física criada com sucesso'}), 201


@app.route('/pessoas_fisicas/<id>', methods=['PUT'])
def update_pessoa_fisica(id):
    pessoa_fisica = PessoaFisica.query.get(id)
    if not pessoa_fisica:
        return jsonify({'message': 'Pessoa Física não encontrada'}), 404
    data = request.get_json()
    if not data or 'cod_prop_pf' not in data or 'cpf_prop' not in data or 'nome_pf' not in data or 'dt_nasc_pf' not in data or 'rg_pf' not in data:
        return jsonify({'message': 'Dados da Pessoa Física ausentes ou inválidos'}), 400
    pessoa_fisica.cod_prop_pf = data['cod_prop_pf']
    pessoa_fisica.cpf_prop = data['cpf_prop']
    pessoa_fisica.nome_pf = data['nome_pf']
    pessoa_fisica.dt_nasc_pf = datetime.datetime.strptime(data['dt_nasc_pf'], '%Y-%m-%d').date()
    pessoa_fisica.rg_pf = data['rg_pf']
    pessoa_fisica.cod_prop_conjuge = data['cod_prop_conjuge']
    db.session.commit()
    return jsonify({'message': 'Pessoa Física atualizada com sucesso'}), 200


@app.route('/pessoas_fisicas/<id>', methods=['DELETE'])
def delete_pessoa_fisica(id):
    pessoa_fisica = PessoaFisica.query.get(id)
    if not pessoa_fisica:
        return jsonify({'message': 'Pessoa Física não encontrada'}), 404
    db.session.delete(pessoa_fisica)
    db.session.commit()
    return jsonify({'message': 'Pessoa Física excluída com sucesso'}), 200


@app.route('/pessoas_juridicas', methods=['GET'])
def get_pessoas_juridicas():
    pessoas_juridicas = PessoaJuridica.query.all()
    output = []
    for pessoa_juridica in pessoas_juridicas:
        pessoa_juridica_data = {
            'cod_prop_pj': pessoa_juridica.cod_prop_pj,
            'cnpj_prop': pessoa_juridica.cnpj_prop,
            'razao_social_pj': pessoa_juridica.razao_social_pj,
            'dt_cria_pj': pessoa_juridica.dt_cria_pj.strftime('%Y-%m-%d')
        }
        output.append(pessoa_juridica_data)
    return jsonify({'pessoas_juridicas': output}), 200


@app.route('/pessoas_juridicas/<id>', methods=['GET'])
def get_pessoa_juridica(id):
    pessoa_juridica = PessoaJuridica.query.get(id)
    if not pessoa_juridica:
        return jsonify({'message': 'Pessoa Jurídica não encontrada'}), 404
    pessoa_juridica_data = {
        'cod_prop_pj': pessoa_juridica.cod_prop_pj,
        'cnpj_prop': pessoa_juridica.cnpj_prop,
        'razao_social_pj': pessoa_juridica.razao_social_pj,
        'dt_cria_pj': pessoa_juridica.dt_cria_pj.strftime('%Y-%m-%d')
    }
    return jsonify({'pessoa_juridica': pessoa_juridica_data}), 200


@app.route('/pessoas_juridicas', methods=['POST'])
def create_pessoa_juridica():
    data = request.get_json()
    if not data or 'cod_prop_pj' not in data or 'cnpj_prop' not in data or 'razao_social_pj' not in data or 'dt_cria_pj' not in data:
        return jsonify({'message': 'Dados da Pessoa Jurídica ausentes ou inválidos'}), 400
    new_pessoa_juridica = PessoaJuridica(
        cod_prop_pj=data['cod_prop_pj'],
        cnpj_prop=data['cnpj_prop'],
        razao_social_pj=data['razao_social_pj'],
        dt_cria_pj=datetime.datetime.strptime(data['dt_cria_pj'], '%Y-%m-%d').date()
    )
    db.session.add(new_pessoa_juridica)
    db.session.commit()
    return jsonify({'message': 'Pessoa Jurídica criada com sucesso'}), 201


@app.route('/pessoas_juridicas/<id>', methods=['PUT'])
def update_pessoa_juridica(id):
    pessoa_juridica = PessoaJuridica.query.get(id)
    if not pessoa_juridica:
        return jsonify({'message': 'Pessoa Jurídica não encontrada'}), 404
    data = request.get_json()
    if not data or 'cod_prop_pj' not in data or 'cnpj_prop' not in data or 'razao_social_pj' not in data or 'dt_cria_pj' not in data:
        return jsonify({'message': 'Dados da Pessoa Jurídica ausentes ou inválidos'}), 400
    pessoa_juridica.cod_prop_pj = data['cod_prop_pj']
    pessoa_juridica.cnpj_prop = data['cnpj_prop']
    pessoa_juridica.razao_social_pj = data['razao_social_pj']
    pessoa_juridica.dt_cria_pj = datetime.datetime.strptime(data['dt_cria_pj'], '%Y-%m-%d').date()
    db.session.commit()
    return jsonify({'message': 'Pessoa Jurídica atualizada com sucesso'}), 200


@app.route('/pessoas_juridicas/<id>', methods=['DELETE'])
def delete_pessoa_juridica(id):
    pessoa_juridica = PessoaJuridica.query.get(id)
    if not pessoa_juridica:
        return jsonify({'message': 'Pessoa Jurídica não encontrada'}), 404
    db.session.delete(pessoa_juridica)
    db.session.commit()
    return jsonify({'message': 'Pessoa Jurídica excluída com sucesso'}), 200
