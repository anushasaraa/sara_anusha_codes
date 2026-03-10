class Solution:
    def isNumber(self, s: str) -> bool:
        dfa = [{'space': 0, 'sign': 1, 'digit': 2, '.': 3}, #state 0 - leading space
               {'digit': 2, '.': 3},                        #state 1 - sign
               {'digit': 2, '.': 4, 'e': 5, 'space': 8},    #state 2 - digit (terminal)
               {'digit': 4},                                #state 3 - dot
               {'digit': 4, 'e': 5, 'space': 8},            #state 4 - digit post dot (terminal)
               {'sign': 6, 'digit': 7},                     #state 5 - exponential 
               {'digit': 7},                                #state 6 - sign post exponential 
               {'digit': 7, 'space': 8},                    #state 7 - digit post exponential (terminal)
               {'space': 8}                                 #state 8 - trailing space (terminal)
              ]
        
        state = 0
        for c in s.lower(): 
            if c in "0123456789": c = "digit"
            elif c == " ":  c = "space"
            elif c in "+-": c = "sign"
            if c not in dfa[state]: return False 
            state = dfa[state][c]
        return state in [2, 4, 7, 8]
