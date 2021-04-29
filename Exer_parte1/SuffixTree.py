# -*- coding: utf-8 -*-

class SuffixTree:
    
    def __init__(self):
        self.nodes = { 0:(-1,{}) } # root node
        self.num = 0
    
    def print_tree(self):
        for k in self.nodes.keys():
            if self.nodes[k][0] < 0:
                print (k, "->", self.nodes[k][1]) 
            else:
                print (k, ":", self.nodes[k][0])
                
    def add_node(self, origin, symbol, leafnum = -1):
        self.num += 1
        self.nodes[origin][1][symbol] = self.num
        self.nodes[self.num] = (leafnum,{})
        
    def add_suffix(self, p, sufnum):
        """Funcao que adiciona um sufixo a arvore
        
        Parameters
        ----------
        p : STR
            Uma string com o sufixo que queremos adicionar a´ arvore
            
        sufnum : INT
            O numero do sufixo, ou seja o numero da folha, que corresponde ao 
            inicio do sufixo na arvore
    
        Returns
        -------
        None.
        """
        nodulo= 0 #comecamos no nodulo 0
        for i in range(len(p)): #percorre todo o padrao
            if p[i] not in self.nodes[nodulo][1].keys(): #se o caracter do padrao nao estiver na arvore cria-se um nodulo novo para o adicionar
                if i == len(p)-1:
                   self.add_node(nodulo, p[i],sufnum) #se a posicao onde vamos a iterar for igual ao tamanho do padrao -1 adicionamos um nodulo, que sera a folha com o numero do inicio do sufixo
                else:
                    self.add_node(nodulo, p[i])  #adicionamos um nodulo onde o num do suf sera -1   
            nodulo = self.nodes[nodulo][1][p[i]]

    
    def suffix_tree_from_seq(self, text):
        """Funcao que adiciona todos os sufixos a' arvore
        
        Parameters
        ----------
        text : STR
            A sequencia para a qual queremos construir a arvore de sufixos

        Returns
        -------
        None.

        """
        t = text+"$" #adiciona ao final da sequecia o simbolo $ que mostra que e' o fim da sequencia
        for i in range(len(t)): #percorremos toda a sequencia mas sempre a avançar uma casa
            self.add_suffix(t[i:], i) #e' cada vez uma sequencoa mais pequena que sera adicionada, ou seja sao os sufixos da sequencia
            
    def find_pattern(self, pattern):
        """Funcao que procura por um padrao na arvore de sufixos

        Parameters
        ----------
        pattern : STR
            Padrao que queremos procurar na arvore de sufixos

        Returns
        -------
        LIST
            Lista com o(s) numero(s) do(s) nodulo(s) onde começa o nosso padra0
        None
            Quando o padrao nao existe na sequencia(text)

        """
        node = 0
        for pos in range(len(pattern)): #percorremos todo o padrao
            if pattern[pos] in self.nodes[node][1].keys(): #se o caracter do padrao estiver no dicionario dos nodulos
                node = self.nodes[node][1][pattern[pos]] #O proximo nodulo é o que corresponde ao nodulo que aparece na arvore para seguirmos
            else: return None #se nao estiver na arvore devolve none
        return self.get_leafes_below(node) #e' porque o padrao foi encontrado na arvore de sufixos, entao devolve uma lista com os os nodulos da arvore onde começa o nosso padrap
        

    def get_leafes_below(self, node):
        res = []
        if self.nodes[node][0] >=0: 
            res.append(self.nodes[node][0])            
        else:
            for k in self.nodes[node][1].keys():
                newnode = self.nodes[node][1][k]
                leafes = self.get_leafes_below(newnode)
                res.extend(leafes)
        return res
    
    def nodes_below(self,node): #exercicio 1 a
        res = []
        if self.nodes[node][0] < 0: # é um nó
            res.append(node) # adiciona o nó à lista
            for k in res: # vai À lista e percorre os nós guardado
                res.extend(list(self.nodes[k][1].values()))
            return res[1::]   # como o primeiro elemento da lista é o proprio nó apresenta-se apenas os seguintes valores 
    
    def matches_prefix(self,prefix): #exercicio 1 b
        res=[]
        pos= self.find_pattern(prefix)[0]
        nb = self.nodes_below(pos)
        #print("nb : ",nb)
        p = prefix[0]
        seq ="T"
        for i in nb:
            print(self.nodes_below(pos))
            if p in self.nodes[pos][1].keys():
                #print(self.nodes[pos][1].keys())
                pos = self.nodes[pos][1][p]
                #print("pos", pos)
                #print(self.nodes[pos][1] )
                if prefix[i] in self.nodes[pos][1]:
                    s = seq + prefix[i]
                    #print("s ",s)
                    seq = s
                    #print("seq", seq)
                    #print("res", res)
                    res.append(seq)
        return res
        

def test():
    seq = "TACTA"
    st = SuffixTree()
    st.suffix_tree_from_seq(seq)
    st.print_tree()
    # print (st.find_pattern("TA"))
    # print(st.nodes_below(0))
    print(st.matches_prefix("TA"))
    #print (st.find_pattern("ACG"))

def test2():
    seq = "TACTA"
    st = SuffixTree()
    st.suffix_tree_from_seq(seq)
    print (st.find_pattern("TA"))
    # print(st.repeats(2,2))

test()
print()
# test2()
        
            
    
    
