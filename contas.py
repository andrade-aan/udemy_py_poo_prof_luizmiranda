#from abc import ABC, abstractmethod
import abc

class Conta(abc.ABC):
    
    def __init__(self, agencia, conta, saldo=0):
        
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    @abc.abstractmethod
    def sacar(self, valor):
        
        self.saldo = valor - self.saldo
        self.detalhes(f'SAQUE R${valor}')

    def depositar(self, valor):
        
        self.saldo = valor + self.saldo
        self.detalhes(f'DEPÓSITO R${valor}')
        
    def detalhes(self, msg=''):
        print(f'\nOperação de {msg} realizada com sucesso!!!\nSeu saldo é de R${self.saldo:.2f}')
        
class ContaPoupanca(Conta):
    
    def depositar(self, valor):
        self.saldo = valor + self.saldo
        self.detalhes(f'DEPÓSITO de R${valor}')
    
    def sacar(self, valor):
        
        valor_pos_saque = self.saldo - valor
        
        if valor_pos_saque >= 0:
            self.saldo = self.saldo - valor
            self.detalhes(f'SAQUE de R${valor}')
            return self.saldo
        
        print("\nSaque não realizado!!!")
        print(f"Seu saldo é de R${self.saldo:.2f}")
        
        
class ContaCorrente(Conta):

    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite
        
    def sacar(self, valor):
        
        valor_pos_saque = self.saldo - valor
        valor_limite_maximo = -1*(self.limite)
        
        if valor_pos_saque >= valor_limite_maximo:
            self.saldo = self.saldo - valor
            self.detalhes(f'SAQUE de R${valor}')
            # print(f'Saldo Atual de R${self.saldo}')
        
        else:
            print("\nSaque não realizado!!!")
            print(f"Seu saldo é de R${self.saldo:.2f}")
      
    def depositar(self, valor):
        self.saldo = valor + self.saldo
        self.detalhes(f'DEPÓSITO de R${valor}')
     

if __name__ == "__main__":
    
    # cp1 = ContaPoupanca('0001','01-1')
    # cp1.sacar(400)
    # cp1.depositar(1600)
    # cp1.sacar(170)
    
    cc1 = ContaCorrente('1','1',0,100)
    cc1.sacar(50)
    cc1.depositar(10)
    cc1.sacar(10)