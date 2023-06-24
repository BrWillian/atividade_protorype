from app.models.proprietario import Proprietario, ProprietarioPropriedade, DonoPJ
from app.models.pessoa import PessoaFisica
from app.models.propriedade import Propriedade
from flask import request, jsonify, render_template
from datetime import datetime
from app import app, db



@app.route('/proprietario')
def index_proprietarios():
    return render_template('proprietario.html')


@app.route('/proprietario', methods=['POST'])
def create_proprietario():
    data = request.json  # Assuming JSON payload

    # Extract data from the request
    cod_prop_pj = data.get('cod_prop_pj') if data.get('cod_prop_pj') else None
    cod_prop_pf = data.get('cod_prop_pf') if data.get('cod_prop_pf') else None
    fone1 = data.get('fone1')
    fone2 = data.get('fone2') if data.get('fone2') else None
    fone3 = data.get('fone3') if data.get('fone3') else None

    # Create a new Proprietario instance
    proprietario = Proprietario(
        cod_prop_pj=cod_prop_pj,
        cod_prop_pf=cod_prop_pf,
        fone1=fone1,
        fone2=fone2,
        fone3=fone3
    )

    # Save the new Proprietario to the database
    db.session.add(proprietario)
    db.session.commit()

    return jsonify({'message': 'Proprietario created successfully.'}), 201

# Get information about a specific Proprietario
@app.route('/proprietario/<int:cod_proprietario>', methods=['GET'])
def get_proprietario(cod_proprietario):
    # Retrieve the Proprietario from the database
    proprietario = Proprietario.query.get(cod_proprietario)

    if not proprietario:
        return jsonify({'error': 'Proprietario not found.'}), 404

    # Serialize the Proprietario object
    proprietario_data = {
        'cod_proprietario': proprietario.cod_proprietario,
        'cod_prop_pj': proprietario.cod_prop_pj,
        'cod_prop_pf': proprietario.cod_prop_pf,
        'fone1': proprietario.fone1,
        'fone2': proprietario.fone2,
        'fone3': proprietario.fone3
    }

    return jsonify(proprietario_data), 200

# Update information of a specific Proprietario
@app.route('/proprietario/<int:cod_proprietario>', methods=['PUT'])
def update_proprietario(cod_proprietario):
    data = request.json  # Assuming JSON payload

    # Retrieve the Proprietario from the database
    proprietario = Proprietario.query.get(cod_proprietario)

    if not proprietario:
        return jsonify({'error': 'Proprietario not found.'}), 404

    # Update the Proprietario attributes
    proprietario.cod_prop_pj = data.get('cod_prop_pj', proprietario.cod_prop_pj)
    proprietario.cod_prop_pf = data.get('cod_prop_pf', proprietario.cod_prop_pf)
    proprietario.fone1 = data.get('fone1', proprietario.fone1)
    proprietario.fone2 = data.get('fone2', proprietario.fone2)
    proprietario.fone3 = data.get('fone3', proprietario.fone3)

    # Save the updated Proprietario to the database
    db.session.commit()

    return jsonify({'message': 'Proprietario updated successfully.'}), 200

# Delete a specific Proprietario
@app.route('/proprietario/<int:cod_proprietario>', methods=['DELETE'])
def delete_proprietario(cod_proprietario):
    # Retrieve the Proprietario from the database
    proprietario = Proprietario.query.get(cod_proprietario)

    if not proprietario:
        return jsonify({'error': 'Proprietario not found.'}), 404

    # Delete the Proprietario from the database
    db.session.delete(proprietario)
    db.session.commit()

    return jsonify({'message': 'Proprietario deleted successfully.'}), 200

# Create a new ProprietarioPropriedade relation
@app.route('/proprietario_propriedade', methods=['POST'])
def create_proprietario_propriedade():
    data = request.json  # Assuming JSON payload

    # Extract data from the request
    cod_propriedade = data.get('cod_propriedade')
    cod_proprietario = data.get('cod_proprietario')
    dt_aquisicao = datetime.strptime(data.get('dt_aquisicao'), '%d/%m/%y')

    # Create a new ProprietarioPropriedade instance
    proprietario_propriedade = ProprietarioPropriedade(
        cod_propriedade=cod_propriedade,
        cod_proprietario=cod_proprietario,
        dt_aquisicao=dt_aquisicao
    )

    # Save the new ProprietarioPropriedade to the database
    db.session.add(proprietario_propriedade)
    db.session.commit()

    return jsonify({'message': 'ProprietarioPropriedade created successfully.'}), 201

# Create a new DonoPJ relation
@app.route('/dono_pj', methods=['POST'])
def create_dono_pj():
    data = request.json  # Assuming JSON payload

    # Extract data from the request
    cod_prop_pj = data.get('cod_prop_pj')
    cod_prop_pf = data.get('cod_prop_pf')

    print(data)

    # Create a new DonoPJ instance
    dono_pj = DonoPJ(
        cod_prop_pj=cod_prop_pj,
        cod_prop_pf=cod_prop_pf
    )

    # Save the new DonoPJ to the database
    db.session.add(dono_pj)
    db.session.commit()

    return jsonify({'message': 'DonoPJ created successfully.'}), 201

# Get properties of Pessoa Juridica and their owners
@app.route('/propriedades_pj', methods=['GET'])
def listar_propriedades_pj():
    # Retrieve properties of Pessoa Juridica and their owners

    propriedades_pj = db.session.query(DonoPJ, ProprietarioPropriedade, Proprietario, Propriedade, PessoaFisica)\
    .join(ProprietarioPropriedade, Propriedade.cod_propriedade == ProprietarioPropriedade.cod_propriedade)\
    .join(Proprietario, Proprietario.cod_proprietario == ProprietarioPropriedade.cod_proprietario).join(DonoPJ, DonoPJ.cod_prop_pj == Proprietario.cod_prop_pj)\
    .join(PessoaFisica, PessoaFisica.cpf_prop == DonoPJ.cod_prop_pf).all()

    # Serialize the properties and owners
    propriedades_data = []
    for dono_pj, propriedade_pj, proprietario, propriedade, pessoa_fisica in propriedades_pj:
        propriedade_data = {
            'cod_propriedade': propriedade.cod_propriedade,
            'nome_propriedade': propriedade.nome_propriedade,
            'area': propriedade.area,
            'cod_municipio': propriedade.cod_municipio,
            'valor_aquisicao': propriedade.valor_aquisicao,
            'dono': pessoa_fisica.nome_pf,

        }
        propriedades_data.append(propriedade_data)

    return jsonify(propriedades_data), 200
