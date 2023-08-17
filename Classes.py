import random
class Cliente:

    def sacar(self, valor,saldo):
        if valor > saldo:
            print("Não é possível sacar esse valor")
        else:
            self.saldo -= valor
            print("Valor sacado com sucesso! O saldo agora é de R$", self.saldo)

    def depositar(self, valor):
        self.saldo += valor
        print("Valor depositado com sucesso! O saldo agora é de R$", self.saldo)

    def transferencia(self, num_conta1, num_conta2, valor):
        num_conta1.saldo=self.saldo - valor
        num_conta2.saldo=self.saldo + valor
        return num_conta1.saldo, num_conta2.saldo

class Banco:

    def adicionar_conta(self):
        self.num_conta = random.randint(1000,9999)
        self.nome = ""
        self.idade = 0
        self.cpf = 0
        self.saldo = 0

    def getNome(self):
        return self.nome
    
    def setNome(self,x):
        self.nome = x
        



clientes = []