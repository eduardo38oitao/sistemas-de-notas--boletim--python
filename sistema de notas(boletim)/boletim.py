class BoletimEscolar:
    def __init__(self, aluno, disciplina, notas):
        # Atributos privados usando o '__'
        self.__aluno = aluno
        self.__disciplina = disciplina
        # Chama o método privado para validar as notas no inicio
        self.__notas = self.__validar_notas(notas)

    # 1. MÉTODO PRIVADO: Ajuda na validação
    def __validar_notas(self, notas) :
        if len(notas) == 4:
            return notas
        return [0.0, 0.0, 0.0, 0.0]

    # DECORADORES: Getters e Setters para colocar os atributos privados com segurança
    @property
    def aluno(self) :
        return self.__aluno

    @aluno.setter
    def aluno(self, novo_aluno):
        self.__aluno = novo_aluno

    @property
    def disciplina(self) :
        return self.__disciplina

    @property
    def notas(self) :
        return self.__notas

    @notas.setter
    def notas(self, novas_notações):
        self.__notas = self.__validar_notas(novas_notações)

    # 2. Não depende do 'self', analisa apenas o valor que recebe
    @staticmethod
    def definir_situacao(media):
        if media >= 6.0:
            return "APROVADO"
        elif media >= 4.0:
            return "RECUPERAÇÃO"
        else:
            return "REPROVADO"

    # 3.Calcula a média simples das notas
    def calcular_media(self) :
        return sum(self.__notas) / 4

    # 4. Gera o dicionário com o boletim completo
    def emitir_boletim(self, nota_recuperacao):
        media_final = self.calcular_media()
        
        if nota_recuperacao > media_final:
            media_final = (media_final + nota_recuperacao) / 2
            
        # Utiliza o método estático para descobrir a situação
        situacao = BoletimEscolar.definir_situacao(media_final)
        
        return {
            "Aluno": self.__aluno,
            "Disciplina": self.__disciplina,
            "Notas": self.__notas,
            "Média Final":(media_final, 1),
            "Situação": situacao
        }