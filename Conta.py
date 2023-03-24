class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = 0
        self.numero = numero
        self.titular = titular

        @property
        def get_saldo(self):
            return self._saldo

        @saldo.setter
        def set_saldo(self, saldo):
            if(saldo<0):
                print("O saldo não pode ser negativo")
            else:
                self._saldo = saldo

        @saque.setter
        def saque(self, valor):
            if(self.saldo>=valor):
                self.saldo-=valor
                print("Saque realizado com sucesso")
            else:
                print("Saldo Insuficiente")

        @deposita.setter
        def deposita (self, valor):
            self.saldo+=valor

        @extrato.setter
        def extrato(self):
            print("cliente: ", self._titular, "Saldo Atual: ", self._saldo)