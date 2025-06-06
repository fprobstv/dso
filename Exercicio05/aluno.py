from abc import ABC, abstractmethod
from usuario_BU import UsuarioBU


class Aluno(UsuarioBU):
    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int, matricula: int):
        super().__init__(cpf, dias_de_emprestimo)
        self.__matricula = matricula

    @property
    def matricula(self):
        return self.__matricula

    @matricula.setter
    def matricula(self, matricula: int):
        self.__matricula = matricula

    def emprestar(self, titulo_livro: str):
        return(
            f'Aluno de matricula "{self.matricula}" '
            f'pegou emprestado o livro: {titulo_livro} com '
        )

    def devolver(self, titulo_livro: str):
        return(
            f'Aluno de matricula "{self.matricula}" '
            f'devolveu o livro: {titulo_livro}'
        )
