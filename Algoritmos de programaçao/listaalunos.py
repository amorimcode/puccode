ALUNO = []

N = int(input('Número de alunos: '))
Soma = 0
for i in range(N) : 
    nome = input('Nome: ')
    nota = float(input('Nota: '))
    ALUNO.append([nome, nota])
Média = Soma/N
print(f'Média da Classe: {Média:.1f}')
for aluno in ALUNO:
    if aluno [1] >= Média:
        print(f'Nome: {ALUNO[0]} Nota: {aluno[1]:.1f}')