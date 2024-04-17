professor = input('Digite o nome do professor: ').title()
aluno = input('Digite o nome do aluno: ').title()
curso = input('Digite o nome do curso: ').capitalize()
nota1 = float(input(f'Digite a primeira nota do aluno(Digite com ponto):').replace(",","."))
nota2 = float(input(f'Digite a primeira nota do aluno(Digite com ponto):'))
nota3 = float(input(f'Digite a primeira nota do aluno(Digite com ponto):'))
nota4 = float(input('Digite a primeira nota do aluno(Digite com ponto):'))
notas = [nota1, nota2, nota3, nota4]
media = sum(notas)/4
print(f'O professor {professor} seu aluno do  curso de {curso} teve a média de {media} para o aluno {aluno}')
if media >=7: 
    print ('\033[1;32mAprovado')
elif media <=6.9 and media >=5:
    print('\033[1;33mRecuperação')
else:
    print(f'Professor {professor} seu aluno {aluno} do curso {curso} foi \033[1;31mReprovado\033[0m com a média de {media}')

      

