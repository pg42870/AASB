# -*- coding: utf-8 -*-


class Automata:
    
    def __init__(self, alphabet, pattern):
        self.numstates = len(pattern) + 1 #porque começamos no zero que nao pertence ao padrao por isso temos de adicionar +1 para chegarmos ao estado final
        self.alphabet = alphabet
        self.transitionTable = {}
        self.buildTransitionTable(pattern)        
    
    def buildTransitionTable(self, pattern):
        """ Construcao da tabela de transicao de estados
        q-> estado atual
        a -> caracter do alfabeto
        prefixo -> parte do padrao ate ao estado atual mais o caracter que estamos a avaliar
        overlap -> funcao que devolve  0 se nao  existir overlap, ou seja temos de voltar ao inicio da tabela,
                ou devolve o indice seguinte ao caracter do padrao ate onde existiu overlap (ou seja indicamos qual
                sera o proximo estado)
        
        Parameters
        ----------
        pattern : STR
            Padrao para o qual vamos construir a tabela de transicao de estados.
        
        """
        for q in range(self.numstates): #loop sobre os estados
            for a in self.alphabet:  
                prefixo = pattern[0:q] + a
                self.transitionTable[(q,a)] = overlap(prefixo,pattern)
       
    def printAutomata(self):
        print ("States: " , self.numstates)
        print ("Alphabet: " , self.alphabet)
        print ("Transition table:")
        for k in self.transitionTable.keys():
            print (k[0], ",", k[1], " -> ", self.transitionTable[k])
         
    def nextState(self, current, symbol):
        """
        Funcao que ao receber o estado currente e o proximo simbolo devolve
        qual sera o proximo estado, usa a tabela transitionTable

        Parameters
        ----------
        current : int
            estado atual
        symbol : str
            caractere que estamos a avaliar

        Returns
        -------
        next : int
            o proximo estado 

        """
        return self.transitionTable.get((current, symbol), "Erro: current ou symbol nao existem na tabela de transicao para o padrao") #usamos o get para se nao existir uma entrada [current, symbol] na tabela podermos devolver um valor por defeito
        
    def applySeq(self, seq):
        """
        Funcao que devolve uma lista com o numero dos estados que foram percorridos
        para analisar toda a sequencia ao compara-la ao padrao (neste caso ja usando
        a tabela de transicao)

        Parameters
        ----------
        seq : STR
            sequencia onde queremos encontrar o padrao

        Returns
        -------
        res : LIST
            Lista com os estados percorridos para analisar toda a sequencia

        """
        q = 0 #estado inicial
        res = [q] #lista onde serao adicionados os proximos estados
        for s in seq: #percorrer a sequencia
            q = self.nextState(q, s) #atualizar o q para corresponder ao novo estado
            res.append(q) #adicionar a lista o novo estado
        return res
        
    def occurencesPattern(self, text):
        """
        Funcao que devolve uma lista com os indices do text onde o padrao começa

        Parameters
        ----------
        text : STR
            sequencia de texto onde estamos a procura do padrao

        Returns
        -------
        res : LIST
            Lista com os indices do text onde se iniciam os padroes

        """
        q = 0 
        res = []
        for p in self.applySeq(text): #percorrer a lista dos estados percorridos
            if p == self.numstates-1: # se o estado corresponde ao estado final
                res.append(len(text[0:q]) - (self.numstates-1)) #adiciona a lista a posicao onde o padrao começa no texto.
            q += 1 
        return res

def overlap(s1, s2):
    """
    Funcao que devolve 0 se nao existe overlap e devolve o indice seguinte da 
    sequencia 2 ate onde ocorreu o overlap

    Parameters
    ----------
    s1 : STR
        prefixo
    s2 : STR
        Padrao 
    """
    maxov = min(len(s1), len(s2))
    for i in range(maxov,0,-1):
        if s1[-i:] == s2[:i]: return i
    return 0
               
def test():
    auto = Automata("AC", "ACA")
    auto.printAutomata()
    print (auto.applySeq("CACAACAA"))
    print (auto.occurencesPattern("CACAACAA"))

test()

#States:  4
#Alphabet:  AC
#Transition table:
#0 , A  ->  1
#0 , C  ->  0
#1 , A  ->  1
#1 , C  ->  2
#2 , A  ->  3
#2 , C  ->  0
#3 , A  ->  1
#3 , C  ->  2
#[0, 0, 1, 2, 3, 1, 2, 3, 1]
#[1, 4]



