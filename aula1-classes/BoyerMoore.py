# -*- coding: utf-8 -*-

class BoyerMoore:
    
    def __init__(self, alphabet, pattern):
        self.alphabet = alphabet
        self.pattern = pattern 
        self.preprocess()

    def preprocess(self):
        self.process_bcr() #dicionario que resultou do preprocessamento do bcr
        self.process_gsr() #o mesmo mas para o gsr
        
    def process_bcr(self):
        """Implementacao do pre-processamento do BCR:
            cria um dicionario com a ultima posicao de cada caracter do alfabeto no padrao
        self.alphabet - letras que estão no padrão
        #pattern - padrao que queremos encontrar num sequencia
        """
        self.occ = {} #as keys sao as letras do alfabeto e os valores a ultima posicao onde o caracter ocorre no padrao
        for c in self.alphabet: # percorre todo o alfabeto e para cada caracter adiciona -1 ao dicionario
            self.occ[c]=-1  
        for i in range(len(self.pattern)): #percorre cada posicao do padrao
            self.occ[self.pattern[i]]=i #atualiza o dicionario com o indice do caracer no padrao
            #no final do ciclo o dicionario fica com o indice da ultima ocorrencia do caracter (do alfabeto) no padrao

            
    def process_gsr(self):
        """ Implementacao do pre processamento do good suffix rule"""
        self.f = [0] * (len(self.pattern)+1) #cria lista de zeros com o tamanho do padrao +1
        self.s = [0 for p in range(len(self.pattern)+1)] #criar lista de zeros com o tamanho do padrao +1, vai registar o indice da sequencia onde o padrao se inicia
        i = len(self.pattern) #tamanho do padrao
        j= i+1 #tamanho do padrao + 1
        self.f[i] = j #alterar a ultima posicao do self.f para j
        while i > 0: 
            while j <= len(self.pattern) and self.pattern[i-1] != self.pattern[j-1]:
                if self.s[j] == 0 : #se o dicionario na posicao j ainda tiver com zero
                    self.s[j]= j-i #substitui-mos pelo valor j-1
                j = self.f[j] #j 
            i -= 1   #sao a mesma coisa
            j = j-1
            self.f[i] = j
        j = self.f[0]
        for i in range(len(self.pattern)):
            if self.s[i] == 0:
                self.s[i] = j
            if i == j: j = self.f[j] #podemos fazer o if assim
                    
                
        
    def search_pattern(self, text):
        """ Procura de um padrao numa sequencia/texto
        text <- sequencia onde vamos procurar o nosso padrao (self.pattern)
        Devolve uma lista dos indices onde o padrao começa na sequencia
        """
        res = [] #começamos com uma lista vazia
        i = 0 #posicao na sequencia
        while i <= (len(text) - len(self.pattern)): #posiccao na sequencia ser menor ou igual ao tamnanho do texto menos o tamanho do padrao
            j = len(self.pattern)-1 #posicao no padrao
            while j >= 0 and self.pattern[j] == text[j+i]: #enquanto a posicao e existir um match entre o padrao e o texto
                j -= 1 #andamos uma casa para a esquerda
            if j < 0:  #significa que temos um match do padrao inteiro
                res.append(i) #adicionamos a posicao na sequencia onde começa o nosso padrao
                i += self.s[0] #vai adicionar o indice da sequencia onde o nosso padrao comeca
            else: # e porque temos um missmatch
                c = text[j+i] 
                i += max(self.s[j+1], j-self.occ[c])  # vai ver com qual das regras e' que consegue um maior avanço na sequencia
        return res

def test():
    bm = BoyerMoore("ACTG", "ACCA")
    print (bm.search_pattern("ATAGAACCAATGAACCATGATGAACCATGGATACCCAACCACC"))

test()

# result: [5, 13, 23, 37]
            
