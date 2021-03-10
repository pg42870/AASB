# -*- coding: utf-8 -*-

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
        nodulo= 0
        for i in range(len(p)):
            if p[i] not in self.nodes[nodulo].keys():
                self.add_node(nodulo,p[i])
                nodulo = len(self.nodes)-1
            else:
                nodulo = self.nodes[nodulo][p[i]]
                                                                
            
    def trie_from_patterns(self, pats):
        for p in pats:
            self.add_pattern(p)
     
            
    def prefix_trie_match(self, text):
        pos = 0
        match = ""
        node = 0
        while pos < len(text):
            # ...
        return None

        
    def trie_matches(self, text):
        res = []
        for i in range(len(text)):
            #...
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
    print (t.prefix_trie_match("GAGATCCTA"))
    print (t.trie_matches("GAGATCCTA"))
    
test()
print()
test2()
