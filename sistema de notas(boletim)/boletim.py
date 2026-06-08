class Aluno:
    def __init__(self, nome, escola, idade, turma, nota):
        self.__escola = escola
        self.__nome = nome
        self.__idade = idade
        self.__turma = turma
        self.__nota = nota






    

    def notas1(self):
        if(self.__nota >= 6):
            print(f"{self.__nota} está acima da média")
        else:
            print(f"{self.__nota} está vermelha")
    def notas2(self):
        if(self.__nota >= 6):
            print(f"{self.__nota} está acima da média")
        else:
            print(f"{self.__nota} está vermelha")
    def notas3(self):
        if(self.__nota >= 6):
            print(f"{self.__nota} está acima da média")
        else:
            print(f"{self.__nota} está vermelha")
    
    
    

    def faltas(self, falta):
        if(falta >= 280):
            print(f"{falta} pela quantidade de ausencia {self.__nome} está reprovado")
        else:
            print(f"{falta} aceitavel")
    

    def mediaTrimestre(self):
        notasTrimestre = ()
        return notasTrimestre


    @property
    def nome(self):
        return self.__nome
    @property
    def escola(self):
        return self.__escola
    @property
    def idade(self):
        return self.__idade
    @property
    def turma(self):
        return self.__turma
    @property
    def nota(self):
        return  self.__nota