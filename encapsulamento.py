class filme:
    def __init__(self, titulo, horas):
        self.__titulo = titulo
        self.__horas = horas
    
    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo
    
    @property
    def horas(self):
        return self.__qtdPag

    @qtdPag.setter
    def horas(self, qtdPag):
        self.__qtdPag = qtdPag

F = filme('black widow', 260)

print(F.titulo)
print(F.horas)

F.horas = '100'
F.titulo = 'o sobrinho do mago'

print(F.titulo)
print(F.horas)