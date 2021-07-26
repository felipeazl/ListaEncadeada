#Cria
#Insere (Valor, Posição)
#Remove (Posição)
#Posição (Valor)
#Valor (Posição)
#Destroi

class ELEMENTO: 
    def __init__(self, data):
        self.data = data
        self.proximo = None

class LISTA:
    def __init__(self): 
        self.inicio = None
        self.tamanho = 0
        
    def Inserir(self, elemento):
        if (self.inicio == None):           
            self.inicio = ELEMENTO(elemento) 
        else:
            aux = self.inicio
            while (aux.proximo):
                aux = aux.proximo
            aux.proximo = ELEMENTO(elemento)
            self.tamanho += 1 

    def Mostrar(self):
        if (self.inicio == None):
            print("Lista Inexistente")
        else:
            aux = self.inicio
            for i in range(self.tamanho):
                print(aux.data, end = ", ")
                aux = aux.proximo
            print("\n")
            
    def BuscarElemento(self, elemento):
        aux = self.inicio
        for i in range(self.tamanho):
            if (aux.data == elemento):
                print("Elemento: ",aux.data, "Na posição: ", i)
            aux = aux.proximo
            
    def BuscarPosição(self, posição):
        if (posição > self.tamanho - 1):
            print("Posição Invalida.")
        else:
            aux = self.inicio
            for i in range(posição):            
                aux = aux.proximo
            print("Elemento: ",aux.data, "Na posição: ", posição)

    def Remover(self, posição):
        posição -= 1
        aux = 0
        remover = 0
        if((posição < 0) or (posição >self.tamanho)):
            print("Posição Inválida.")
        elif(posição == 0):
            remover = self.inicio
            self.inicio = self.inicio
            self.tamanho = self.tamanho - 1
            return remover
        else:
            aux = self.inicio
            for i in range(1, posição):
                aux = aux.proximo
            remover = aux.proximo
            aux.proximo = aux.proximo
            self.tamanho = self.tamanho - 1
            return remover
        
    def Destruir(self):
        self.inicio = None
        self.tamanho = None


    #Um método que retorne o número de elementos;
    #Um método que receba uma segunda listas encadeada como argumento e retorne um valor lógico indicando se as listas são iguais;
    #Um método que imprima os valores de uma lista encadeada de trás para frente.

    def Length(self):
        print("\nTotal de elementos", self.tamanho + 1)

    def Comparar(self):
        ListaComparar = [15, 17, 21, 25, 3] # lista para ser comparada
        diferença = 0
        if (self.inicio == None):
            print("Lista Inexistente")
        else:
            aux = self.inicio            
            for i in range(self.tamanho):
                if (aux.data != ListaComparar):
                    diferença += 1                  
                aux = aux.proximo
            if (diferença == 0):
                print("As listas são iguais.")
            else: 
                print("As listas são diferentes.")

    def Contrario(self):          
        tamAux = self.tamanho   
        for i in range(tamAux):
            aux = self.inicio   
            tamAux = tamAux - 1
            for i in range(tamAux):
                aux = aux.proximo
            print(aux.data, end = ", ")
        