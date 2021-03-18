# Calculadora Civil Python
#######################
 
## Perguntar pro usuario qual das 5 operações se deseja calcular
## Imprimi o resultado na tela
 
while True:
    
    print('___________________________________________________________________________________________')
    print('------>>>>>>>BEM VINDO A CALCULADORA CIVIL!<<<<<<<<----------')
    operacao = input('\nQual operação você deseja realizar?\n(1)Tensão Normal\n(2)Tensão Cisalhante\n(3)Fator de Segurança - Normal\n(4)Fator de Segurança - Cisalhante\n(5)Fator de Segurança na Junta Colada\n(c)Limpar Tela\n(s)Sair\n')

    if operacao == 's' or operacao == 'S': #sair do programa
        break

    elif operacao == 'c' or operacao == 'C': #limpar tela
        import os
        os.system('cls') or None

    elif operacao == '1': #calcula tensão normal
        print('\nTensão Normal Escolhida com Sucessso!\n')
        cargap = float(input('\nDigite o valor da carga P em (N): '))
        largura = float(input('\nDigite o valor da largura da estrutura em (mm): '))
        espessura = float(input('\nDigite o valor da espessura da estrutura em (mm): '))
        angulo = str(input('\nDigite a letra que corresponde ao valor do angulo 0 desejado:\n(a)5°\t(b)10°\t(c)15°\t(d)20°\n(e)25°\t(f)30°\t(g)35°\t(h)40°\n(i)45°\t(j)50°\t(k)55°\t(l)60°\n(m)65°\t(n)70°\t(o)75°\t(p)80°\n(q)85°\t(r)Outro Valor\n'))
        
        #transforma a letra em um grau correspondente
        if angulo == 'a':
            numero = 5
        elif angulo == 'b':
            numero = 10
        elif angulo == 'c':
            numero = 15
        elif angulo == 'd':
            numero = 20
        elif angulo == 'e':
            numero = 25
        elif angulo == 'f':
            numero = 30
        elif angulo == 'g':
            numero = 35
        elif angulo == 'h':
            numero = 40
        elif angulo == 'i':
            numero = 45
        elif angulo == 'j':
            numero = 50
        elif angulo == 'k':
            numero = 55
        elif angulo == 'l':
            numero = 60
        elif angulo == 'm':
            numero = 65
        elif angulo == 'n':
            numero = 70
        elif angulo == 'o':
            numero = 75
        elif angulo == 'p':
            numero = 80
        elif angulo == 'q':
            numero = 85
        elif angulo == 'r':
            numero = float(input('\nDigite o valor do angulo 0: '))
        else:
            print('Operacao Inválida!')  

        import math
        pi = 3.14159265359
        radiano = (numero * pi)/180

        resultado1 = (cargap * (math.sin(radiano))**2) / (largura * espessura)
        
        print('\nFormula de Operação (cargap * (math.sin(radiano))**2) / (largura * espessura)')
        print('\nA Tensão Normal da estrutura é de: %.4f MPa'%resultado1) 


    elif operacao == '2':
        print('\nA Tensão Cisalhante escolhida com sucessso!\n')
        import math
        
        cargap = float(input('\nDigite o valor da carga P em (N): '))
        largura = float(input('\nDigite o valor da largura da estrutura em (mm): '))
        espessura = float(input('\nDigite o valor da espessura da estrutura em (mm): '))
        angulo = str(input('\nDigite a letra que corresponde ao valor do angulo 0 desejado:\n(a)5°\t(b)10°\t(c)15°\t(d)20°\n(e)25°\t(f)30°\t(g)35°\t(h)40°\n(i)45°\t(j)50°\t(k)55°\t(l)60°\n(m)65°\t(n)70°\t(o)75°\t(p)80°\n(q)85°\t(r)Outro Valor\n'))
        if angulo == 'a':
            numero = 5
        elif angulo == 'b':
            numero = 10
        elif angulo == 'c':
            numero = 15
        elif angulo == 'd':
            numero = 20
        elif angulo == 'e':
            numero = 25
        elif angulo == 'f':
            numero = 30
        elif angulo == 'g':
            numero = 35
        elif angulo == 'h':
            numero = 40
        elif angulo == 'i':
            numero = 45
        elif angulo == 'j':
            numero = 50
        elif angulo == 'k':
            numero = 55
        elif angulo == 'l':
            numero = 60
        elif angulo == 'm':
            numero = 65
        elif angulo == 'n':
            numero = 70
        elif angulo == 'o':
            numero = 75
        elif angulo == 'p':
            numero = 80
        elif angulo == 'q':
            numero = 85
        elif angulo == 'r':
            numero = float(input('\nDigite o valor do angulo 0: '))
        else:
            print('Operacao Inválida!') 

        pi = 3.14159265359
        radiano = (numero * pi)/180

        resultado2 = (cargap * (math.sin(radiano)) * (math.cos(radiano))) / (largura * espessura)
        print('\nFormula de Operação: (cargap * (math.sin(radiano)) * (math.cos(radiano))) / (largura * espessura)')
        print('\nA Tensão Cisalhante da estrutura é de: %.4f MPa'%resultado2) 


    elif operacao == '3':
        print('\nFator de Segurança Normal escolhido com sucesso!\n')
        madeira = str(input('\nEscolha um dos tipos de madeira:\n(1)Aroeira-do-Sertão[14.75 MPa]\n(2)Ipê-roxo[13.53 MPa]\n(3)Eucalipto[10.20 MPa]\n(4)Peroba[8.34 MPa]\n(5)Outro Valor\n'))
        
        arroeiran = 14.75
        ipen = 13.53
        eucalipton = 10.20
        peroban = 8.34
        
        if madeira == '1':
            print('\nAroeira-do-Sertão escolhido com sucesso\n')
            csn1 = resultado1 / arroeiran
            print('\nO Fator de Segurança para Tensão Normal é de: %.4f MPa'%csn1)

        elif madeira == '2':
            print('\nIpê-Roxo escolhido com sucesso!\n')
            csn1 = resultado1 / ipen
            print('\nO Fator de Segurança para tensão Normal é de: %.4f MPa'%csn1)

        elif madeira == '3':
            print('\nEucalipto escolhido com sucesso\n')
            csn1 = resultado1 / eucalipton
            print('\nO Fator de Segurança para Tensão Normal da Peroba é de: %.4f MPa'%csn1)

        elif madeira == '4':
            print('\nPeroba escolhido com sucesso!\n')
            csn1 = resultado1 / peroban
            print('\nO Fator de Segurança para Tensão Normal da Peroba é de: %.4f MPa'%csn1)

        elif madeira == '5':
            mad = float(input('\nDigite o valor do Fator desejado da madeira: '))
            csn1 = resultado1 / mad
            print('\nO Fator de Segurança para Tensão Normal da madeira especificada é de: %.4f MPa'%csn1)

        else:
            print('Operacao inválida!')  
        print('\nFormula de Operação: (tensaoNormal/tensaoMadeira)')

    elif operacao == '4':
        print('\nFator de Segurança Cisalhante escolhido com sucesso!\n')
        madeira = str(input('\nEscolha um dos tipos de madeira:\n(1)Aroeira-do-Sertão[14.75 MPa]\n(2)Ipê-roxo[13.53 MPa]\n(3)Eucalipto[10.20 MPa]\n(4)Peroba[8.34 MPa]\n(5)Outro Valor\n'))
        
        arroeiran = 14.75
        ipen = 13.53
        eucalipton = 10.20
        peroban = 8.34
        
        if madeira == '1':
            print('\nAroeira-do-Sertão escolhido com sucesso\n')
            csn2 = resultado2 / arroeiran
            print('\nO Fator de Segurança para Tensão Normal é de: %.4f MPa'%csn2)

        elif madeira == '2':
            print('\nIpê-Roxo escolhido com sucesso!\n')
            csn2 = resultado2 / ipen
            print('\nO Fator de Segurança para tensão Normal do Ipê-Roxo é de: %.4f MPa'%csn2)

        elif madeira == '3':
            print('\nEucalipto escolhido com sucesso\n')
            csn2 = resultado2 / eucalipton
            print('\nO Fator de Segurança para Tensão Normal da Peroba é de: %.4f MPa'%csn2)

        elif madeira == '4':
            print('\nPeroba escolhido com sucesso!\n')
            csn2 = resultado2 / peroban
            print('\nO Fator de Segurança para Tensão Normal da Peroba é de: %.4f MPa'%csn2)

        elif madeira == '5':
            mad2 = float(input('\nDigite o valor do Fator desejado da madeira: '))
            csn2 = resultado2 / mad2
            print('\nO Fator de Segurança para Tensão Normal da madeira especificada é de: %.4f MPa'%csn2)

        else:
            print('Operacao inválida!')  
        
        print('\nFormula de Operação: (tensaoCisalhante/tensaoMadeira)')


    elif operacao == '5':
        print('\nO Fator de Segurança na Junta Colada escolhido com sucesso!\n')
        print('FSN:',csn1)
        print('FSC:',csn2)
        fsjc = min(csn1,csn2)    
        print('\nO Fator de Segurança na Junta Colada é de: %.4f MPa que é o menor valor entre FSN e FSC!\n'%fsjc)

    else:
        print('Operacao Inválida!')
 








    