from src.app.db import DB, MA

class Departamento(DB.Model):
    cod_dpto = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
    nome_dpto = DB.Column(DB.String(84), nullable=False)

    def __init__(self, cod_dpto, nome_dpto):
        self.cod_dpto = cod_dpto
        self.nome_dpto = nome_dpto

class DepartamentoSchema(MA.Schema):
    class Meta:
        fields = ('cod_dpto', 'nome_dpto')

departamento_share_schema = DepartamentoSchema()
departamentos_share_schema = DepartamentoSchema(many=True)
