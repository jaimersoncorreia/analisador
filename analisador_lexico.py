'''
	========= Projeto Analisador Léxico ============

	Disciplina: Compiladores 
	Professor: Rayol Neto 

	Autor 1: 0zz1 - Oziel Senior
	Autor 2: Jay  - Jaimerson Correa
	Autor 3: Pach - Jheymisson Pacheco

	Linguagem: Topper 

	================================================

	################# Tokens #######################	

	Operadores Ok
		Adição	 		-		+ 
		Subtração		-		-
		Multiplicação	-		*
		Divisão 		-		/

		Maior que 		- 		>
		Menor que 		-		<
		Maior igual que	-		>=
		Menor igual que -		<=
		Igualdade 		-		==
		Diferença		-		!=

		Atribuição 		-		=

	Delimitadores Ok
		Final de instrução		-	;
		Inicio bloco comandos	-	inicio     
		Fim bloco comandos		- 	fim  	  
		Declaração de +1 var	-	,	
		Abertura Agrupamento expressão	-   ( 
		Fechamento agrupamento exp.		- 	)
	
	Palavras Reservadas Ok
		inteiro 				
		real
		letra
		palavra
		se 
		enquanto
		faca
		inicio 
		fim	
		leia
		escreva
	
	Tipos de dados (ER) Ok
		inteiro 		- 	[0-9]+ 
		real			-	[0-9]+.[0-9]+
		letra			-	[a-z|A-Z]
		Palavra 		-	[a-z|A-Z|0-9]+
	
	Identificadores (ER) Ok
		id 				- 	[_|a-z|A-Z][a-z|A-Z|0-9|_]*				
'''
import ply.lex as lex
import re


class AnalisadorLexico():
    def __init__(self):
        self.t_delimitadores = {";": "Final instrução",
                                ",": "Vírgula (,)",
                                "(": "Abertura de agrupamento",
                                ")": "Fechamento de agrupamento",
                                "inicio": "Inicio de bloco",
                                "fim": "Fim de bloco"
                                }
        self.t_operadores = {"+": "Soma",
                             "-": "Subtração",
                             "*": "Multiplicação",
                             "/": "Divisão",
                             ">": "Maior que",
                             "<": "Menor que",
                             ">=": "Maior igual",
                             "<=": "Menor igual",
                             "==": "Igualdade ",
                             "!=": "Diferença",
                             "=": "Atribuição"
                             }
        self.t_palavras_reservadas = "inteiro real letra palavra se enquanto faca inicio fim leia escreva".split(" ")

    def isDelimitador(self, s):
        delimitadores = self.t_delimitadores
        if s in delimitadores.keys():
            return True
        return False

    def isOperador(self, s):
        operadores = self.t_operadores
        if s in operadores.keys():
            return True
        return False

    def isPalavraReservada(self, s):
        palavras_reservadas = self.t_palavras_reservadas
        if s in palavras_reservadas:
            return True
        return False

    ######## Especificadores ############
    # \d 	->	[0-9]
    # \w	->  [a-z|A-Z|0-9|_]
    # \		->  Anula o significado especial do char seguinte

    ####### Quantificadores  ############
    # ?		->	0 ou 1 ocorrência (opcional)
    # + 	->  1 ou mais ocorrências (fecho positivo de kleane)
    # *		-> 	0 ou mais ocorrências (fecho de kleane)

    def isIdentificador(self, s):
        er = r'[a-zA-Z][_a-zA-Z0-9]*'
        if re.match(er, s) != None:
            return True
        return False

    def isInteiro(self, s):
        er = r'[0-9]+'
        if re.match(er, s) != None:
            return True
        return False

    def isReal(self, s):
        er = r'[0-9]+\.[0-9]+'
        if re.match(er, s) != None:
            return True
        return False

    def isLetra(self, s):
        er = r'\'[a-zA-Z]\''
        if re.match(er, s) != None:
            return True
        return False

    def isPalavra(self, s):
        er = r'\"\w*\"'
        if re.match(er, s) != None:
            return True
        return False

    def separa(self, s):
        linha = s.replace("\t", " ")
        linha = linha.replace("\n", " ")
        simbolos = ['>', '<', '>=', '<=', '==', '!=', '=', '+', '-', '*', '/', ',', ';', '(', ')']
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

    def getDescricao(self, dic, chave):
        for k, v in dic.items():
            if chave == k:
                return v
        return ''

    def analisar(self):

        tokens_validos = '\n==================================================='
        tokens_validos += '\n|{:15}|Tipo'.format('Token')
        tokens_validos += '\n===================================================\n'
        #print(self.isPalavraReservada("fim"))
        arquivo = open('pogs/pog_02.top', 'r')
        linhas = arquivo.readlines()

        for linha in linhas:
            #print(linha)
            tokens = self.separa(linha)
            for token in tokens:
                if self.isPalavraReservada(token):
                    tokens_validos += '\n|{:_<15}|Palavra Reservada'.format(token)
                elif self.isOperador(token):
                    tokens_validos += '\n|{:_<15}|Operador'.format(token)
                elif self.isDelimitador(token):
                    tokens_validos += '\n|{:_<15}|Delimitador'.format(token)
                elif self.isIdentificador(token):
                    tokens_validos += '\n|{:_<15}|Identificador'.format(token)
                elif self.isInteiro(token):
                    tokens_validos += '\n|{:_<15}|Tipo de dado'.format(token)
                elif self.isReal(token):
                    tokens_validos += '\n|{:_<15}|Tipo de dado'.format(token)
                elif self.isLetra(token):
                    tokens_validos += '\n|{:_<15}|Tipo de dado'.format(token)
                elif self.isPalavra(token):
                    tokens_validos += '\n|{:_<15}|Tipo de dado'.format(token)
                else:
                    tokens_validos += '\nToken inválido : '.format(token)
        arquivo.close()
        return tokens_validos

a = AnalisadorLexico()
print(a.analisar())
