from Funções import LISTA

lista = LISTA()

lista.Inserir(10)
lista.Inserir(20)
lista.Inserir(30)
lista.Inserir(40)
lista.Inserir(50)
lista.Inserir(60)
lista.Inserir(70)
lista.Inserir(80)
lista.Inserir(90)
lista.Inserir(100)

lista.Mostrar()

lista.BuscarElemento(30)
lista.BuscarElemento(90)
print("\n")

lista.BuscarPosição(0)
lista.BuscarPosição(1)
lista.BuscarPosição(2)
lista.BuscarPosição(20)
print("\n")

lista.Remover(9)
lista.Mostrar()

print("\n")
lista.Destruir()
lista.Mostrar()