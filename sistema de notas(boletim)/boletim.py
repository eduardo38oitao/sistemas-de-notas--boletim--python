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
    
 # Metodo privado: Valida se a nota está entre 0 e 10 
    def __nota_e_validade(self, nota):
        if media_final >= 6.0:
            print("Situação: APROVADO(A)!")
        else:
            print("Situação: EM RECUPERAÇÃO!")
# Método Público: Calcula a média do aluno
    def calcular_media(self):
        # Valida as duas notas antes de fazer o cálculo
        if self.__nota_e_valida(self.__nota1) and self.__nota_e_valida(self.__nota2):
            media = (self.__nota1 + self.__nota2) / 2
            return media
        return 0


   class Boletim:
    # Método Estático: Exibe o cabeçalho do colégio sem precisar criar um aluno antes
    @staticmethod
    def exibir_cabecalho():
        print("=== COLÉGIO ESTADUAL ANTÔNIO DE MORAES BARROS ===")
        print("=== SISTEMA DE LANÇAMENTO DE NOTAS ===")

    # Construtor: Cria o boletim com atributos privados (usam __)
    def __init__(self, aluno, nota1, nota2):
        self.__aluno = aluno       # Atributo privado
        self.__nota1 = nota1       # Atributo privado
        self.__nota2 = nota2       # Atributo privado

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
    def nota2(self):
        return self.__nota2

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


# === TESTANDO O SISTEMA (Demonstração para a turma) ===







# 1. Chamando o método estático
Boletim.exibir_cabecalho()
print()

# 2. Criando o boletim de um aluno (Instanciando a classe)
boletim_alex = Boletim("Alex Silva", 7.5, 8.5)

# 3. Usando os decoradores @property para mostrar os dados
print(f"Aluno: {boletim_alex.aluno}")
print(f"Nota 1: {boletim_alex.nota1}")
print(f"Nota 2: {boletim_alex.nota2}")

# 4. Chamando os métodos públicos para ver o resultado
print("\n--- Resultado Final ---")
boletim_alex.exibir_situacao()

# 5. Testando um caso de recuperação para demonstrar o sistema funcionando
print("\n" + "="*40 + "\n")
boletim_lucas = Boletim("Lucas Lima", 4.0, 5.5)
print(f"Aluno: {boletim_lucas.aluno}")
boletim_lucas.exibir_situacao()