aluno = []
media = []
nota = []
acum = 0
giros  = giros_para  = 0


def x (): #função para organização pessoal
    print ('-=' * 30)

while True:

    opcao = int (input ('\n#MENU#\n1 - Acessar Turmas\n2 - Sair do programa\nQual a sua opção [1/2]: ')) #menu e entrada
    x () #separar

    while opcao < 1 or opcao > 2: #verificar erro na digitação
        print ('Erro, Tente novamente') #informar erro
        x () #separar
        opcao = int (input ('\n#MENU#\n1 - Acessar Turmas\n2 - Sair do programa\nQual a sua opção [1/2]: ')) #perguntar novamente

    if opcao == 2: #consequência de parada
        print('Fim do programa')
        x ()    
        break        
            
    else: #se opção for 1. Acessar turmas
        ensino = int (input ('\nMenu\n1 - Ensino Fundamental\n2 - Ensino Médio\nQual sua opcão: ')) #menu e entrada
        x() #separar

        while ensino < 1 or ensino > 2: #verificar erro na digitação
            print ('Erro, Tente novamente') #informar erro 
            x () #separar
            ensino = int (input ('\nMenu\n1 - Ensino Fundamental\n2 - Ensino Médio\nQual sua opcão: ')) #perguntar novamente

        if ensino == 1: #verificar se é ensino fundamental
            turma = int (input ('Olá, gostaria de acessar qual turma: [6 ano até 9 ano] ')) #entrada da turma

            while turma < 6 or turma > 9: #verificar erro na digitação
                print ('Erro, Turma não encontrada') #informar erro
                x () #separar
                turma = int (input ('Olá, gostaria de acessar qual turma: [6 ano até 9 ano] ')) #perguntar novamente

        else: #verificar se é ensino médio
            turma = int (input ('Olá, gostaria de acessar qual turma: [1 ano até 3 ano] ')) #entrada da turma

            while turma < 1 or turma > 3: #verificar erro na digitação
                print ('Erro, Turma não encontrada') #informar erro
                x () #separar
                turma = int (input ('Olá, gostaria de acessar qual turma: [1 ano até 3 ano] ')) #perguntar novamente

    add = int (input ('Vai acessar quantos alunos? ')) #imformar quantos alunos vai ser acessando

    while giros_para < add: #consequecia de parada
        giros = 0 #zera para recomeçar
        giros_para += 1 #aumento no contador
        nome = input (f'Nome do {giros_para}° aluno da serie {turma}° ano: ') #entrada do nome do aluno
        aluno.append(nome) 

        nota = []
        while 5 > giros: #consequecia de parada
                               
            giros += 1 #aumento no contador
            nota.append (float (input (f'Digite a {giros} nota do(a) {nome}: '))) #entrada das notas             
            x ()

            if giros >= 5: #consequecia de parada
                print (f'O aluno {nome}, da turma {turma} ano\nSeguindo as notas add') #mostra o nome do aluno e a turma
                x ()
                for i, j in enumerate(nota): #pegar as nota se a posicao
                    print (f'nota {i + 1}: {j}')
                    acum += j #acumular as notas
                x ()
                media.append(acum / 5)
                acum = 0
                x ()
for i in range (len(aluno)):     
    print (f'Foi add os alunos {aluno[i]} com as media {media[i]:.1f} da serie {turma}°') #saida final