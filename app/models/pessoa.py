from app import db


class PessoaFisica(db.Model):
    __tablename__ = 'pessoa_fisica'

    cod_prop_pf = db.Column('cod_prop_pf', db.Integer, db.ForeignKey('proprietario.cod_proprietario'), primary_key=True)
    cpf_prop = db.Column('cpf_prop', db.Integer, unique=True)
    nome_pf = db.Column('nome_pf', db.String)
    dt_nasc_pf = db.Column('dt_nasc_pf', db.Date)
    rg_pf = db.Column('rg_pf', db.BigInteger)
    cod_prop_conjuge = db.Column('cod_prop_conjuge', db.Integer, db.ForeignKey('pessoa_fisica.cod_prop_pf'))


class PessoaJuridica(db.Model):
    __tablename__ = 'pessoa_juridica'

    cod_prop_pj = db.Column('cod_prop_pj', db.Integer, db.ForeignKey('proprietario.cod_proprietario'), primary_key=True)
    cnpj_prop = db.Column('cnpj_prop', db.Integer, unique=True)
    razao_social_pj = db.Column('razao_social_pj', db.String)
    dt_cria_pj = db.Column('dt_cria_pj', db.Date)
