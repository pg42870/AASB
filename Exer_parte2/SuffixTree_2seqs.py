# -*- coding: utf-8 -*-

class SuffixTree_2seqs:
    
    def __init__(self):
        self.nodes = { 0:(-1,{}) } # root node
        self.num = 0
        self.seq1 = ''
        self.seq2 = ''
    
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

    
    def suffix_tree_from_seq(self, seq1, seq2):
        """Funcao que adiciona todos os sufixos a' arvore
        
        Parameters
        ----------
        text : STR
            A sequencia para a qual queremos construir a arvore de sufixos

        Returns
        -------
        None.

        """
        seq1 = seq1+"$" #adiciona ao final da sequecia o simbolo $ que mostra que e' o fim da sequencia
        seq2 = seq2 + "#"
        for i in range(len(seq1)): #percorremos toda a sequencia mas sempre a avançar uma casa
            self.add_suffix(seq1[i:], i) #e' cada vez uma sequencoa mais pequena que sera adicionada, ou seja sao os sufixos da sequencia
        for j in range(len(seq2)):
            self.add_suffix(seq2[j:], j)
            
         
            
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
    
        
    def largestCommonSubstring (self):
        seq1 = self.seq1
        seq2 = self.seq2
        subs = ''
        for i in range(len(seq1)):
            for j in range(len(seq2)):
                k = 1
                while i+k <= len(seq1) and j+k <= len(seq2) and seq1[i:i+k]==seq2[j:j+k]:
                    if len(subs) <= len(seq1[i:i+k]):
                        subs = seq1[i:i+k]
                    k = k+1
        return subs
                
        pass

def test():
    seq1 = "TAC"
    seq2 =  "ATA"
    st = SuffixTree_2seqs()
    st.suffix_tree_from_seq(seq1,seq2)
    #st.print_tree()
    # print (st.find_pattern("TA"))
    # print(st.nodes_below(0))
    #print(st.matches_prefix("TA"))
    #print (st.find_pattern("ACG"))
    print(st.largestCommonSubstring())

def test2():
    seq = "TACTA"
    st = SuffixTree()
    st.suffix_tree_from_seq(seq)
    print (st.find_pattern("TA"))
    # print(st.repeats(2,2))

test()
print()
# test2()
        
            
    
    
