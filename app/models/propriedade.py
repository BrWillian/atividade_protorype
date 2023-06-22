from app import db


class Municipio(db.Model):
    __tablename__ = 'municipio'

    cod_municipio = db.Column('cod_municipio', db.Integer, primary_key=True, autoincrement=True)
    nome_municipio = db.Column('nome_municipio', db.String)
    uf_municipio = db.Column('uf_municipio', db.String(2))


class Propriedade(db.Model):
    __tablename__ = 'propriedade'

    cod_propriedade = db.Column('cod_propriedade', db.Integer, primary_key=True, autoincrement=True)
    nome_propriedade = db.Column('nome_propriedade', db.String)
    area = db.Column('area', db.Float)
    distancia_municipio = db.Column('distancia_municipio', db.Float)
    valor_aquisicao = db.Column('valor_aquisicao', db.Float)
