
def separa(linha_arquivo, contlinha):

    linha = linha_arquivo.replace("\t", " ")
    linha = linha.replace("\n", " ")
    simbolos = ['>=', '<=', '==', '!=', '=', '+', '-', '*', '/', ',', ';', '(', ')','>', '<']
    lista = []
    palavra = ''
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
    lista.append('{}'.format(palavra))
    while '' in lista:
        lista.remove('')
    return lista

arquivo = open('pogs/pog_02.top', 'r')
linhas = arquivo.readlines()
contlinha = 0
for linha in linhas:
    contlinha += 1
    print(separa(linha, contlinha))
