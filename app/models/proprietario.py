from app import db


class Proprietario(db.Model):
    __tablename__ = 'proprietario'

    cod_proprietario = db.Column('cod_proprietario', db.BigInteger, primary_key=True, autoincrement=True)
    cod_prop_pj = db.Column('cod_prop_pj', db.BigInteger, db.ForeignKey('pessoa_juridica.cnpj_prop'), primary_key=True)
    cod_prop_pf = db.Column('cod_prop_pf', db.BigInteger, db.ForeignKey('pessoa_fisica.cpf_prop'), primary_key=True)
    fone1 = db.Column('fone1', db.String)
    fone2 = db.Column('fone2', db.String)
    fone3 = db.Column('fone3', db.String)


class ProprietarioPropriedade(db.Model):
    __tablename__ = 'proprietario_propriedade'

    cod_propriedade = db.Column('cod_propriedade', db.BigInteger, db.ForeignKey('propriedade.cod_propriedade'), primary_key=True)
    cod_proprietario = db.Column('cod_proprietario', db.BigInteger, db.ForeignKey('proprietario.cod_proprietario'), primary_key=True)
    dt_aquisicao = db.Column('dt_aquisicao', db.Date)

class DonoPJ(db.Model):
    __tablename__ = 'dono_pj'

    cod_prop_pj = db.Column('cod_prop_pj', db.BigInteger, db.ForeignKey('pessoa_juridica.cnpj_prop'), primary_key=True)
    cod_prop_pf = db.Column('cod_prop_pf', db.BigInteger, db.ForeignKey('pessoa_fisica.cpf_prop'), primary_key=True)