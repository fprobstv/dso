from cliente import Cliente


class ClienteFidelidade(Cliente):
    def __init__(self, desconto, codigo_fidelidade, nome, cpf, endereco, telefone):
        super().__init__(cpf, nome, endereco, telefone)
        self.__desconto = desconto
        self.__codigo_fidelidade = codigo_fidelidade

    @property
    def desconto(self):
        return self.__desconto

    @desconto.setter
    def desconto(self, desconto):
        self.__desconto = desconto

    @property
    def codigo_fidelidade(self):
        return self.__codigo_fidelidade

    @codigo_fidelidade.setter
    def codigo_fidelidade(self, codigo_fidelidade):
        self.__codigo_fidelidade = codigo_fidelidade
