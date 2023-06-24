from app import db


class PessoaFisica(db.Model):
    __tablename__ = 'pessoa_fisica'

    cpf_prop = db.Column('cpf_prop', db.BigInteger, unique=True, primary_key=True)
    nome_pf = db.Column('nome_pf', db.String)
    dt_nasc_pf = db.Column('dt_nasc_pf', db.Date)
    rg_pf = db.Column('rg_pf', db.BigInteger)
    cod_prop_conjuge = db.Column('cod_conjuge', db.BigInteger, db.ForeignKey('pessoa_fisica.cpf_prop'), nullable=True)


class PessoaJuridica(db.Model):
    __tablename__ = 'pessoa_juridica'

    cnpj_prop = db.Column('cnpj_prop', db.BigInteger, unique=True, primary_key=True)
    razao_social_pj = db.Column('razao_social_pj', db.String)
    dt_cria_pj = db.Column('dt_cria_pj', db.Date)