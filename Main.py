class Main:
    pass

print("testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1 = Cliente ("Higor", "(21)97700-5823")
#Conta = Conta(c1.nome, 6565, 0)
Conta = Conta(c1.get_nome(), 1222)

Conta.deposita(100)
Conta.saque(50)
Conta.extrato()


#print(Conta.titular, "Numero: ", Conta.numero, "Seu saldo: ", Conta.saldo);

