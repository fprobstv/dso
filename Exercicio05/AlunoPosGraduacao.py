from aluno import Aluno


class AlunoPosGraduacao(Aluno):
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        self.__elaborando_tese = False
        super().__init__(cpf, dias_de_emprestimo, matricula)

    @property
    def elaborando_tese(self):
        return self.__elaborando_tese

    @elaborando_tese.setter
    def elaborando_tese(self, elaborando_tese: bool):
        self.__elaborando_tese = elaborando_tese

    def emprestar(self, titulo_livro):
        prazo = super().dias_de_emprestimo
        if self.__elaborando_tese is True:
            prazo = prazo * 2
        return super().emprestar(titulo_livro) + f"{prazo} dias de prazo"

    def devolver(self, titulo_livro):
        return super().devolver(titulo_livro)
