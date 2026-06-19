class Boletim:
    # Método Estático: Exibe o cabeçalho do colégio sem precisar criar um aluno antes
    @staticmethod
    def exibir_cabecalho():
        print( "////////// COLEGIO ESTADUAL ANTÔNIO DE MORAES BARROS ////////////" )
        print( "///////// SISTEMA DE LANÇAMENTO DE NOTAS ////////////" )

    # Construtor: Cria o boletim com atributos privados (USAM __)
    def __init__(self, aluno, nota1, nota2):
        self.__aluno = aluno    # Isso é um atributo privado
        self.__nota1 = nota1    # Isso é um atributo privado
        self.__nota2 = nota2    # Isso é um atributo privado

    # Decorador @property: Permite ler o nome do aluno de forma segura
    @property
    def aluno(self):
        return self.__aluno
    
    # Decorador @property: Permite ler a primeira nota
    @property
    def nota1(self):
        return self.__nota1
    
    # Decorador @property: Permite ler a segunda nota
    @property
    def nota1(self):
        return self.__nota1
    

 
    

  # Método Privado: Valida se a nota está entre 0 e 10 (regra interna)
    def __nota_e_valida(self, nota):
        if 0 <= nota <= 10:
            return True
        else:
            print("Erro: A nota digitada deve ser entre 0 e 10!")
            return False

    # Método Público: Calcula a média do aluno
    def calcular_media(self):
        # Valida as duas notas antes de fazer o cálculo
        if self.__nota_e_valida(self.__nota1) and self.__nota_e_valida(self.__nota2):
            media = (self.__nota1 + self.__nota2) / 2
            return media
        return 0

    # Método Público: Mostra a situação (Aprovado ou Recuperação)
    def exibir_situacao(self):
        media_final = self.calcular_media()
        print(f"Média Final: {media_final:.1f}")
       
        # Se a média for 6 ou mais, está aprovado
        if media_final >= 6.0:
            print("Situação: APROVADO(A)!")
        else:
            print("Situação: EM RECUPERAÇÃO!")


