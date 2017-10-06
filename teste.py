
def separa(s,contlinha):

    linha = s.replace("\t", " ")
    linha = linha.replace("\n", " ")
    simbolos = ['>', '<', '>=', '<=', '==', '!=', '=', '+', '-', '*', '/', ',', ';', '(', ')']
    lista = []
    palavra = ''
    #print('Linha_{}: {}'.format(contlinha,s))
    for caracter in linha:
        if caracter in [' ']:
            lista.append('{}'.format(palavra))
            palavra = ''
            continue

        elif caracter in simbolos:
            lista.append('{}'.format(palavra))
            lista.append('{}'.format(caracter))
            palavra = ''
            continue
        palavra += caracter
        #print('||{}||'.format(palavra))
    lista.append('{}'.format(palavra))
    while '' in lista:
        lista.remove('')

    return lista

arquivo = open('pogs/pog_03.top', 'r')
linhas = arquivo.readlines()
contlinha = 0
for linha in linhas:
    contlinha += 1
    print(separa(linha,contlinha))






'''
    def separa(self, s):
        linha = s.replace("\t", "")
        linha = linha.replace("\n", "")
        #print("Linha : ", linha)
        simbolos = [">", "<", ">=", "<=", "==", "!=", '=', '+', '-', '*', '/', ',', ';', '(', ')']
        lista = []
        p = ''
        for c in linha:
            if c in [' ', '']:
                lista.append(p)
                p = ''
                continue
            elif c in simbolos:
                lista.append(p)
                lista.append(c)
                p = ''
                continue
            p += c
        while '' in lista:
            lista.remove('')
        #print(lista)
        return lista
'''
