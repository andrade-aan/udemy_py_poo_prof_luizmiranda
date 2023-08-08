from abc import ABC, abstractmethod
import abc


class Conta(abc.ABC):

    def __init__(self, agencia: str, conta: str, saldo: float = 0) -> None:

        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor: float) -> float:

        self.saldo = valor - self.saldo
        self.detalhes(f'SAQUE R${valor}')

    def depositar(self, valor: float) -> float:

        self.saldo = valor + self.saldo
        self.detalhes(f'DEPÓSITO R${valor}')

    def detalhes(self, msg: str = '') -> str:
        print(f'\nOperação de {msg} realizada com sucesso!!!' +
              f'\nSeu saldo é de R${self.saldo:.2f}')
        
    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = f'{self.agencia}, {self.conta}, {self.saldo}\n'
        return f'{class_name} {attrs}'


class ContaPoupanca(Conta):

    def depositar(self, valor: float) -> float:
        self.saldo = valor + self.saldo
        self.detalhes(f'DEPÓSITO de R${valor}')

    def sacar(self, valor: float) -> float:

        valor_pos_saque = self.saldo - valor

        if valor_pos_saque >= 0:
            self.saldo = self.saldo - valor
            self.detalhes(f'SAQUE de R${valor}')
            return self.saldo

        else:
            print("\nSaque não realizado!!!")
            print(f"Seu saldo é de R${self.saldo:.2f}")
            return self.saldo


class ContaCorrente(Conta):

    def __init__(self, agencia: str,
                 conta: str, saldo: float = 0,
                 limite: float = 0) -> None:

        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor: float) -> float:

        valor_pos_saque = self.saldo - valor
        valor_limite_maximo = -1*(self.limite)

        if valor_pos_saque >= valor_limite_maximo:
            self.saldo = self.saldo - valor
            self.detalhes(f'SAQUE de R${valor}')
            return self.saldo
            print(f'Saldo Atual de R${self.saldo}')

        else:
            print("\nSaque não realizado!!!")
            print(f"Seu saldo é de R${self.saldo:.2f}")
            return self.saldo

    def depositar(self, valor: float) -> float:

        self.saldo = valor + self.saldo
        self.detalhes(f'DEPÓSITO de R${valor}')
        return self.saldo
    
    def __repr__(self):
        class_name = self.__class__.__name__
        attrs = f'{self.agencia!r}, {self.conta!r}, {self.saldo!r}, '\
            f'{self.limite!r} \n'
        
        return f'{class_name} {attrs}'


if __name__ == "__main__":

    # MOKING

    cp1 = ContaPoupanca('0001', '01-1')
    cp1.sacar(400)
    cp1.depositar(1600)
    cp1.sacar(170)

    cc1 = ContaCorrente('0001', '11-9', 0, 100)
    cc1.sacar(50)
    cc1.depositar(10)
    cc1.sacar(10)
