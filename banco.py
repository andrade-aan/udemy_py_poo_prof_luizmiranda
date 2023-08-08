import pessoas
import contas

class Banco:
    
    def __init__(
        self, 
        agencias: list[str] | None = None, 
        clientes: list[pessoas.Pessoa] | None = None,
        contas: list[contas.Conta] | None = None,
        ):
        
        self.agencias = agencias or []
        self.clientes = clientes or []
        self.contas = contas or []
        
    def _checar_cliente(self, cliente)-> bool:
       
        if cliente in self.clientes:
            return True
        else:
            return False
    
    def _checar_conta(self, conta)-> bool:
       
        if conta in self.contas:
            return True
        else:
            return False
        
    
    def _checar_agencia(self, agencia)-> bool:
       
        if agencia in self.agencias:
            return True
        else:
            return False
    
    def autenticar(self, conta, cliente)-> bool:
        
        return self._checar_agencia(conta) or \
            self._checar_cliente(cliente) or \
                self._checar_conta(conta)
    
    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f'{self.agencias}\n' \
            f'{self.clientes}\n' \
                f'{self.contas}\n' \
                
    
if __name__ == '__main__':
    c1 = pessoas.Cliente('Fabi', 25)
    c2 = pessoas.Cliente('Alex', 44)
    # cliente.
    b1 = Banco()
    c11 = contas.ContaCorrente('0001','10-1',0,0)
    c12 = contas.ContaPoupanca('0001','50-1',0)
    c22 = contas.ContaCorrente('0001','14-3',0,0)
    print(c1)
    print(c2.idade)
    print(c2._conta)
    b1.clientes.extend([c1,c2])
    b1.agencias.extend(['0001', '0002'])
    b1.contas.extend([c11,c12,c22])
    a = b1.autenticar(c1,c11)
    print(b1)
    print(a)