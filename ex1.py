class AnimalAquatico:
    def nadando(self):
        pass

class peixe(AnimalAquatico):
    def nadando(self):
        print(super().nadando(),'O peixe esta nadando...')

class tartaruga(AnimalAquatico):
    def nadando(self):
        print(super().nadando(),'a tartaruga esta nadando...')

Aluno1= peixe()
Aluno1.nadando()

Aluno1= tartaruga()
Aluno1.nadando()