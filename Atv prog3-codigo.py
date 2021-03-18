
while True:    
    print('___________________________________________________________________________________________')
    print('------>>>>>>>BEM VINDO A CALCULADORA R1!<<<<<<<<----------')
    operacao = input('\nQual operação você deseja realizar?\n(1)Hiper\n(2)Problema 9.16\n(3)Problema Iso\n(c)Limpar Tela\n(s)Sair\n')

    if operacao == 's' or operacao == 'S': #sair do programa
        break

    elif operacao == 'c' or operacao == 'C': #limpar tela
        import os
        os.system('cls') or None

    elif operacao == '1': #hiper
        import time
        print('\nPROBLEMA HIPER!\n')
        time.sleep(2)

        L = float(input('Digite o Comprimento [L] da viga(mm): '))
        deltaL= float(input('Digite a variação de comprimento gradual(mm): '))
        w = float(input('Digite a carga [w] em (N/mm): '))
        E = float(input('Digite o módulo de Elasticidade [E] em (MPa): '))
        
        I = 554000000
        print('\nSendo o corpo da viga do tipo W460 x 113, sue momento de inércia 554.10^6 mm^4')
        time.sleep(2)
        print('\nPara o cálculo da reação dos apoios usaremos o método da superposição,\nde modo que a deflexão provocada pela carga distribuida [w] e a provocada pelo apoio rolante em D devem ser iguais.\n')
        time.sleep(2)

        tetaB = -((w *(L**3))/(6*E*I))
        Yb =  -((w *(L**4))/(8*E*I))

        print('O valor da inclinação [Ob] = ', tetaB)
        print('O valor da deflexão [Yb] = ', Yb, '\n\n')

        aux = 0
        a=[]
        tetaBlinha = []
        Yblinha = []
        print( 'a','\t\t','tetaBlinha+tetaB','\t','Yblinha+Yb','\n')
        print( aux,'\t\t',round(tetaB,5),'\t\t',round(Yb,5),'\n')
        aux = aux + deltaL

        for i in range(14):
            a.append(aux)
            yDw=-(w/(24*E*I))*((a[i]**4)-(4*L*(a[i]**3))+(6*L**2*(a[i]**2)))
            P = ((3*E*I) / (a[i]**3)) * yDw
            tetaBlinha.append((P*(a[i]**2)) / (2*E*I))
            Yblinha.append(((P*(a[i]**3)) / (3*E*I)) + (((L-a[i])*P*(a[i]**2)) / (2*E*I)))
            print(round(a[i],0),'\t\t',round(tetaBlinha[i]+tetaB,5),'\t\t',round(Yblinha[i]+Yb,5),'\n')
            aux = aux + deltaL

        time.sleep(3)

    elif operacao == '2':
        import time
        print('\nPROBLEMA 9.16!\n')
        print('Para o cálculo das reações nos apoios, consideramos a simetria e utilizamos a porção ABC .')
        time.sleep(2)
        print('São duas cargas P verticais para baixo, sendo duas reações:RA e RE')
        time.sleep(2)
        print('RA=RB=P\n')
        time.sleep(2)

        L = float(input('Digite o Comprimento [L] da viga(m): '))
        P = float(input('Digite o Valor da carga [P] em (N): '))
        E = float(input('Digite o Módulo de elasticidade [E] em (MPa): '))
        I = float(input('Digite o Valor do Momento de Inércia: '))
        a = float(input('Digite o ponto onde se quer calcular a inclinação: '))

        yc=-((P*a)/(E*I)) * ((L**2)/8 - (a**2)/6)
        print(yc,'m')

    elif operacao == '3':#problema iso
        import time
        print('\nPROBLEMA ISO!\n')
        time.sleep(2)

        E = float(input('Digite o Módulo de Elasticidade [E] em (Pa): '))
        I = float(input('Digite o Valor do Momento de Inércia [I] em (m^4): '))
        nP = float(input('Digite o número de cargas [n] que deseja: '))
        L = float(input('Digite o Comprimento da viga(m): '))
        q = float(input('Digite o valor da carga [q] em (N): '))

        RA = (q * nP) / 2

        print('\nPrecisamos definir qual é o ponto da estrutura que queremos calcular a inclinação e deflexão')
        intervalo = L / (nP+1)
        an = intervalo * nP
        x = float(input('Digite o valor do ponto [x] que deseja calcular: '))

        if x <= an:
            O = (1/(E*I)) * (0.5 * RA * (x**2))
            y = (1/(E*I)) * ((1/6) * RA * (x**3))
        
        elif x > an:
            O = (1/(E*I)) * (0.5 * RA * (x**2)) - (0.5 * q *((x-an)**2))
            y = (1/(E*I)) * ((1/6) * RA * (x**3)) - ((1/6) * q *((x-an)**3))
        else:
            break
        print('teta: ',O)
        print('y: ', y)

        
            
