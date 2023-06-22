from app import db


class Produto(db.Model):
    __tablename__ = 'produto'

    cod_produto = db.Column('cod_produto', db.Integer, primary_key=True, autoincrement=True)
    desc_produto = db.Column('desc_produto', db.String)


class Producao(db.Model):
    __tablename__ = 'producao'

    cod_propriedade = db.Column('cod_propriedade', db.Integer, db.ForeignKey('propriedade.cod_propriedade'),
                                primary_key=True)
    cod_produto = db.Column('cod_produto', db.Integer, db.ForeignKey('produto.cod_produto'), primary_key=True)
    mes_ini_colheita_prov = db.Column('mes_ini_colheita_prov', db.Date)
    mes_fin_colheita_prov = db.Column('mes_fin_colheita_prov', db.Date)
    qtd_prov_colheita = db.Column('qtd_prov_colheita', db.Numeric(10, 2))
    mes_ini_colheita_real = db.Column('mes_ini_colheita_real', db.Date)
    mes_fin_colheita_real = db.Column('mes_fin_colheita_real', db.Date)
    qtd_real_colhida = db.Column('qtd_real_colhida', db.Numeric(10, 2))
