

def separa(linha_arquivo):
    linha = linha_arquivo.replace("\t", " ")
    linha = linha.replace("\n", " ")
    simbolos = ['!', '=', '=', '+', '-', '*', '/', ',', ';', '(', ')', '>', '<']
    cadeia = []
    caracteres = ''
    for caracter in linha:
        if caracter in simbolos:
            caracteres += caracter
            continue
        cadeia.append(caracter)
    print(caracteres)
    print('{} - {}'.format(cadeia,len(cadeia)))

arquivo = open('pogs/teste.top', 'r')
linhas = arquivo.readlines()

for linha in linhas:
    #print(separa(linha))
    separa(linha)