#importamos a arquivo boletim

from boletim import Boletim



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