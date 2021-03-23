# -*- coding: utf-8 -*-

class BWT:
    
    def __init__(self, seq = "", buildsufarray = False):
        self.bwt = self.build_bwt(seq, buildsufarray) 
    
    def set_bwt(self, bw):
        self.bwt = bw

    def build_bwt(self, text, buildsufarray = False):
        ls = []
        for i in range(len(text)): 
            l = ""
            l+= text[i:]
            k = 0
            while len(l) != len(text):
                  l+= text[k]
                  k += 1
            ls.append(l)
        ls.sort()
        res=""
        for m in range(len(text)):
            res += ls[m][-1]
        if buildsufarray:
            self.sa = []
            for i in range(len(ls)):
                stpos = ls[i].index("$")
                self.sa.append(len(text)-stpos-1)  
        return res
    
    def inverse_bwt(self):
        """Funcao que devolve a sequencia original da bwt

        Returns
        -------
        res : STR
            Sequencia que originou a sequencia da bwt.

        """
        firstcol = self.get_first_col() #primeira coluna da matriz
        res = "" #onde vamos adicionar a sequencia original
        c = "$" 
        occ = 1
        for i in range(len(self.bwt)):
            p = find_ith_occ(self.bwt, c, occ) #devolve a posicao na bwt do caracter c na ocurrencia occ
            occ= 1
            c = firstcol[p] #o caracter passa a ser o elemento da primeira coluna com o indice que obtivemos em p
            k = p - 1 
            for i in range(len(firstcol)): #como  podemos ter caracteres repetidos temos de contar as ocurrencias desses caracteres para escolhermos a posicao certa
                if c == firstcol[k]:
                    occ += 1
                    k -= 1
            res += c #adiciona o caracter c à sequencia
        return res        
 

    def get_first_col (self):
        firstcol = []
        for i in self.bwt: #percorre todas as linhas da matriz (lista de listas)
            firstcol.append(i) #adiciona a primeira posição (que na matriz corresponde a coluna)
        firstcol.sort() #ordenar por ordem lexical
        return firstcol
        
    def last_to_first(self):
        """Funcao que devolve uma lista que corresponde ao indices da ultima coluna na primeira coluna
        
        Returns
        -------
        res : LIST
            Lista com os indices dos caracteres da ultima coluna da bwt na primeira coluna
        """
        res = []
        fc=  self.get_first_col()
        for i in range(len(self.bwt)):
            oc = self.bwt[:i].count(self.bwt[i])+1
            p = find_ith_occ(fc, self.bwt[i], oc)
            res.append(p)
        return res

    def bw_matching(self, patt):
        lf = self.last_to_first()
        res = []
        top = 0
        bottom = len(self.bwt)-1
        flag = True
        while flag and top <= bottom:
            if patt != "":
                symbol = patt[-1]
                patt = patt[:-1]
                lmat = self.bwt[top:(bottom+1)]
                if symbol in lmat:
                    topIndex = lmat.index(symbol) + top
                    bottomIndex = bottom - lmat[::-1].index(symbol)
                    top = lf[topIndex]
                    bottom = lf[bottomIndex]
                else: flag = False
            else: 
                for i in range(top, bottom+1): res.append(i)
                flag = False            
        return res        
 
    def bw_matching_pos(self, patt):
        res = []
        match = self.bw_matching(patt)
        for m in range(len(match)):
            res.append(self.sa[match[m]])
        res.sort()
        return res
 
#auxiliary
 
def find_ith_occ(l, elem, index):
    k=0
    for i in range(len(l)):
        if l[i] == elem:
            k += 1
            if k == index: return i
    return -1 
#print("1: ", find_ith_occ([1,2,3,4,5,6,7,8,9], 4, 3))

      
def test():
    seq = "TAGACAGAGA$"
    bw = BWT(seq)
    print (bw.bwt)
    print (bw.last_to_first())
    print (bw.bw_matching("AGA"))


def test2():
    bw = BWT("")
    bw.set_bwt("ACG$GTAAAAC")
    print (bw.inverse_bwt())

def test3():
    seq = "TAGACAGAGA$"
    bw = BWT(seq, True)
    print("Suffix array:", bw.sa)
    print(bw.bw_matching_pos("AGA"))

# test()
# test2()
test3()

