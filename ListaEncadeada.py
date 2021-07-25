class ELEMENTO:
    
    def __init__(self, elemento, proximo):
        self.elemento = elemento
        self.proximo = proximo

class LISTA:
    
    def __init__(self):
        ELEMENTO.__init__(self, elemento = None, proximo = None)
        self.inicio = None
        self.tamanho = 0
        
    def __len__(self):
        return self.tamanho
    
    def Mostrar(self):
        listaAux = []
        add = None
        aux = self.inicio
        if (aux == None):
            return False
        else:
            while (aux != None):
                add = aux.elemento
                listaAux.append(add)
                aux = aux.proximo
            return listaAux
    
    def BuscarPos(self, valor):
        aux = self.inicio
        posição = 0
        contador = 0
        for i in range (self.tamanho):
            if (aux.elemento == valor):
                contador = 0
                return posição + 1
            else:
                contador += 1
            posição += 1
            aux = aux.proximo
        if (contador == 0):
            return posição + 1
        else:
            print("Valor Inexistente.")
            return None
        
    def BuscarElem(self, posição):
        aux = self.inicio
        contador = 0
        valor = 0
        if ((posição <= 0) or (posição > self.tamanho)):
            print("Posição Ivalida.")
            return False
        else:
            posição -= 1
            for i in range(posição + 1):
                if(contador == posição):
                    valor = aux.elemento
                    break
                else:
                    aux = aux.proximo
                    contador += 1
            return valor
    
    def Inserir(self, valor, posição):
        posição -= 1
        if ((posição < 0) or (posição > self.tamanho)):
            print ("Posição Invalida.")
            return False
        elif (posição == 0):
            self.inicio = ELEMENTO (valor, None)
        else:
            aux = self.inicio
            for i in range (1, posição):
                aux = aux.proximo
            aux.proximo = ELEMENTO (valor, aux.proximo)
        self.tamanho = self.tamanho + 1
        return True