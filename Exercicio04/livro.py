from editora import Editora
from autor import Autor
from capitulo import Capitulo

class Livro:
    def __init__ (self, codigo: int, titulo: str, ano:int, editora: Editora, autor: Autor, numero_capitulo: int, titulo_capitulo: str):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor 
        self.__editora = editora
        self.__numero_capitulo = numero_capitulo
        self.__titulo_capitulo = titulo_capitulo
        self.__autores = [autor]
        self.__capitulo = []

    @property
    def codigo(self):
         return self.__codigo
        
    @codigo.setter
    def codigo(self, codigo):
         self.__codigo = codigo

    @property
    def titulo(self):
        return self.__titulo
        
    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
        
    @property
    def ano(self):
        return self.__ano
        
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    @property
    def autor(self):
        return self.__autor
        
    @autor.setter
    def autor(self, autor):
        self.__autor = autor
        
    @property
    def editora(self):
        return self.__editora
        
    @editora.setter
    def editora(self, editora):
        self.__editora = editora

    @property
    def autores(self):  
        return self.__autores

    def incluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):    
            if autor not in self.__autores:
                self.__autores.append(autor)

    def excluir_autor(self, autor: Autor):
        if isinstance(autor, Autor):
            if autor in self.__autores:
                self.__autores.remove(autor)
        
    def incluir_capitulo(self, numero:int, titulo:str):
        if isinstance(titulo, str) and isinstance(numero, int):
            for capitulo in self.__capitulo:
                if capitulo.numero == numero:
                    cadastrado = True
                    break
            else:
                capitulo = Capitulo(numero, titulo)
                self.__capitulo.append(capitulo)

    def excluir_capitulo(self, titulo:str):
        if isinstance(titulo, str):
            for capitulo in self.__capitulo:
                if capitulo.titulo == titulo:
                    self.__capitulo.remove(capitulo)
                break
        
    def find_capitulo_by_titulo(self, titulo:str):
        for capitulo in self.__capitulo:
            if capitulo.titulo == titulo:
                return capitulo

a1 = Autor(1, "Emily")
e1 = Editora(1, "Mundo")
l1 = Livro(1, "Happy Place", 2023, e1, a1, 1, "Capitulo 1")
print(l1.autor.nome)