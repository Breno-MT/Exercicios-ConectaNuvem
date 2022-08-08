from src.app.db import DB, MA

class Curso(DB.Model):
    __tablename__ = "cursos"

    cod_curso = DB.Column(DB.Integer, autoincrement=True, primary_key=True)
    nome_curso = DB.Column(DB.String(80), nullable=False)
    # cod_dpto = DB.Column(DB.Integer, DB.ForeignKey(Departamentos.id), nullable=False)

    def __init__(self, cod_curso, nome_curso):
        self.cod_curso = cod_curso
        self.nome_curso = nome_curso

class CursoSchema(MA.Schema):
    class Meta:
        fields = ('cod_curso', 'nome_curso')

curso_share_schema = CursoSchema()
cursos_share_schema = CursoSchema(many=True)
