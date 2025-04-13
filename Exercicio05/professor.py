from funcionario import Funcionario


class Professor(Funcionario):
    def __init__(self, departamento, cpf):
        super().__init__(departamento, cpf, dias_de_emprestimo=20)

    def emprestar(self, titulo_livro: str):
        return "Professor " + super().emprestar(titulo_livro)

    def devolver(self, titulo_livro: str):
        return "Professor " + super().devolver(titulo_livro)
