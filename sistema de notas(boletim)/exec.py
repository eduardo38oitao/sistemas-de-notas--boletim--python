#importamos a arquivo boletim

from boletim import BoletimEscolar



    # Criando o objeto do aluno
boletim = BoletimEscolar("Carlos Silva", "Programação", [5.5, 6.0, 4.0, 5.0])

# Exibindo o boletim antes da recuperação
print("--- Antes da Recuperação ---")
print(boletim.emitir_boletim())

# Exibindo o boletim após uma nota de recuperação
print("\n--- Após a Recuperação ---")
print(boletim.emitir_boletim(nota_recuperacao=7.5))