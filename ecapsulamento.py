arquivo=open('questionario.txt', 'w')
arquivo.write('\nolá, bem vindo ao questionario')
 
class perguntas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    
        