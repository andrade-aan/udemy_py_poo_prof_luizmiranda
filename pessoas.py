import contas

class Pessoa:
    def __init__(self, nome:str, idade:int) -> None:
        
        self._nome = nome
        self._idade = idade
    
    @property
    def nome(self) -> str:
        return self._nome
    
    @nome.setter
    def nome(self, nome:str) -> None:
        return self._nome
    
    @property
    def idade(self) -> int:
        return self._idade
    
    @idade.setter
    def idade(self, idade:int) -> None:
        return self._idade
    
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{class_name}({self.nome}, {self.idade})'
    
        
class Cliente(Pessoa):
    def __init__(self, nome:str, idade:int) -> None:
        super().__init__(nome, idade)
        self._conta: contas = []
    
    @property
    def conta(self) -> list:
        return self._conta
    
    @conta.setter
    def conta(self, conta) -> None:
        self._conta.append(conta)
        

if __name__ == '__main__':
    cliente = Cliente('Maria', 25)
    # cliente.
    cliente.conta= contas.ContaCorrente('0001','10-1',0,0)
    cliente.conta= contas.ContaPoupanca('0001','50-1',0)
    cliente.conta= contas.ContaCorrente('0001','14-3',0,0)
    print(cliente)
    print(cliente.idade)
    print(cliente._conta)