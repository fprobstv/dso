from funcionario import Funcionario


class Administrativo(Funcionario):
    def __init__(self, departamento, cpf):
        super().__init__(departamento, cpf, dias_de_emprestimo=10)

    def emprestar(self, titulo_livro: str):
        return "Funcionario administrativo " + super().emprestar(titulo_livro)

    def devolver(self, titulo_livro: str):
        return "Funcionario administrativo " + super().devolver(titulo_livro)
