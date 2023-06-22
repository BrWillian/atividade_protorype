from app import db


class Proprietario(db.Model):
    __tablename__ = 'proprietario'

    cod_proprietario = db.Column('cod_proprietario', db.Integer, primary_key=True, autoincrement=True)
    nome_proprietario = db.Column('nome_proprietario', db.String)
    fone1 = db.Column('fone1', db.String)
    fone2 = db.Column('fone2', db.String)
    fone3 = db.Column('fone3', db.String)


class ProprietarioPropriedade(db.Model):
    __tablename__ = 'proprietario_propriedade'

    cod_propriedade = db.Column('cod_propriedade', db.Integer, db.ForeignKey('propriedade.cod_propriedade'), primary_key=True)
    cod_proprietario = db.Column('cod_proprietario', db.Integer, db.ForeignKey('proprietario.cod_proprietario'), primary_key=True)
    dt_aquisicao = db.Column('dt_aquisicao', db.Date)

class DonoPJ(db.Model):
    __tablename__ = 'dono_pj'

    cod_prop_pj = db.Column('cod_prop_pj', db.Integer, db.ForeignKey('pessoa_juridica.cod_prop_pj'), primary_key=True)
    cod_prop_pf = db.Column('cod_prop_pf', db.Integer, db.ForeignKey('pessoa_fisica.cod_prop_pf'), primary_key=True)
