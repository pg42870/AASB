# -*- coding: utf-8 -*-
"""
Joana Gabriel pg42870
"""
class Trie:
    
    def __init__(self):
        self.nodes = { 0:{} } # dictionary
        self.num = 0
    
    def print_trie(self):
        for k in self.nodes.keys():
            print (k, "->" , self.nodes[k]) 
    
    def add_node(self, origin, symbol):
        self.num += 1
        self.nodes[origin][symbol] = self.num
        self.nodes[self.num] = {}
    
    def add_pattern(self, p):
        """Funcao que adiciona um padrao a arvore
        

        Parameters
        ----------
        p : STR
            Uma string com o padrao que queremos adicionar a´ arvore

        Returns
        -------
        None.

        """
        nodulo= 0 #comecamos no nodulo 0
        for i in range(len(p)): #percorre todo o padrao
            if p[i] not in self.nodes[nodulo].keys(): #se o caracter do padrao nao estiver na arvore cria-se um nodulo novo para o adicionar
                self.add_node(nodulo,p[i])
                nodulo = len(self.nodes)-1
            else:
                nodulo = self.nodes[nodulo][p[i]]
                                                                
            
    def trie_from_patterns(self, pats):
        """Funcao que adiciona um padrao a arvore. Percorre todos os padroes da lista e adiciona a arvore

        Parametros
        ----------
        pats : List of STR
            lista com os padroes que queremos adicionar a´ arvore

        Returns
        -------
        None.

        """
        for p in pats:  
            self.add_pattern(p)
     
            
    def prefix_trie_match(self, text):
        """ Funcao que identifica um padroes como prefixos do texto
        
        Parametros
        ----------
            texto : STR
                texto do qual queremos ver se existe um prefixo do padrao ou nao
        
        Devolve
        -------
            None: None
                Se nao existir nenhum prefixo
            match: STR
                prefixo do padrao identificado no texto
        """
        pos = 0
        match = ""
        node = 0
        while pos < len(text): #percorrer o texto ate a posicao nao ser maior que o comprimento do texto
            if text[pos] in self.nodes[node].keys(): #se o caracter do texto estiver nas chaves do nodulo 'e porque esse caracter existe no padrao
                match += text[pos]  #adicionar o caracter ao match
                node = self.nodes[node][text[pos]] #mudar o nodulo para o nodulo proximo nodulo de acordo com a arvore do nosso padrao
                if self.nodes[node] == {}: #se o proximo nodulo for uma folha ou seja tiver um dicionario vazio 'e porque ate a´posicao i do texto temos um prefixo
                    return match #assim chegamos ao final do prefixo e a funcao devolve o match
                else:
                    pos += 1 #se ainda nao for o fim do padrao continuamos o nosso ciclo
            else:
                return None #se nao fizer parte da arvore e´ porque nao ha match           
        return None #se chegarmos ao fim do texto sem chegar a uma folha e´porque nao ha match

        
    def trie_matches(self, text):
        """ Funcao que recebe um texto e devolve uma lista de tuplos com o indice
        onde um prefico do padrao ocorre no texto e o tal prefixo.
        
        Parameters
        ----------
        text : STR
            

        Devolve
        -------
        res : LIST OF TUPLES
            Lista de tuplo com o formato (indice do texto onde começa o prefixo, o prefixo do padrao que aparece no texto)
        """
        res = []
        for i in range(len(text)): #percorre todo o comprimento do texto
            match = self.prefix_trie_match(text[i:]) #utiliza a funcao self.prefix_trie_match que devolve o padrao encontrado a apartir daquela posicao
            if match != None: #se o match nao for None e´ porque existe um prefixo do padrao no texto
                res.append((i,match)) #adicionamos o tuplo com o indice de inicio do match no texto e o match
        return res
        
          
def test():
    patterns = ["GAT", "CCT", "GAG"]
    t = Trie()
    t.trie_from_patterns(patterns)
    t.print_trie()

   
def test2():
    patterns = ["AGAGAT", "AGC", "AGTCC", "CAGAT", "CCTA", "GAGAT", "GAT", "TC"]
    t = Trie()
    t.trie_from_patterns(patterns)
    t.print_trie()
    print (t.prefix_trie_match("GAGATCCTA"))
    print (t.trie_matches("GAGATCCTA"))
    
test()
print()
test2()
