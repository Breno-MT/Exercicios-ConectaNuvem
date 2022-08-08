from src.app.db import DB, MA

class Aluno(DB.Model):
    __tablename__ = "alunos"

    mat_alu = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
    name = DB.Column(DB.String(100), nullable=False)
    data_entrada = DB.Column(DB.DateTime, nullable=False)
    # cod_curso = DB.Column(DB.Integer, DB.ForeignKey(Curso.id), nullable=False)
    cotista = DB.Column(DB.Boolean, nullable=True)

    def __init__(self, mat_alu, name, data_entrada, cotista):
        self.mat_alu = mat_alu
        self.name = name
        self.data_entrada = data_entrada
        self.cotista = cotista

class AlunoSchema(MA.Schema):
    class Meta:
        fields = ('mat_alu', 'name', 'data_entrada', 'cotista')

aluno_share_schema = AlunoSchema()
alunos_share_schema = AlunoSchema(many=True)
