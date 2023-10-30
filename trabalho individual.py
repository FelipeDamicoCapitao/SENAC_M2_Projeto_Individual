# entrevista
# teste teorico
# teste pratico
# avaliação em soft skills

# passo 1 - criar uma lista para armazenar resultados
# passo 2 - função que busca candidato 
# 	Nota minima de e,t,p,s

######################################################################################################################################################
# Importações
from time import sleep as espera #fazer o programa não apresentar os resultados instantaneament

from B1_separacao import sep # separação de cabeçalhos principal - grande
from B1_separacao import sep2 # separação de cabeçalhos secundário - médio
from B1_separacao import sep3 # separação de prontilhados


######################################################################################################################################################
# Comandos repetitivos padronizados

def padrao_espera():#fazer o programa não apresentar os resultados instantaneamente - 0.4 segundos de espera
    espera(0.4)
def padrao_espera_longo():#fazer o programa não apresentar os resultados instantaneamente - 0.4 segundos de espera
    espera(1.6)

######################################################################################################################################################
# Cores
# \033[style; text; back m
NCinza = "\033[1;30;1m"
NVermelho = "\033[1;31;1m"
NVerde = "\033[1;32;1m"
NAmarelo = "\033[1;33;1m"
NMagenta = "\033[1;34;1m"
NRosa = "\033[1;35;1m"
NCiano = "\033[1;36;1m"
NBranco = "\033[1;37;1m"
Corfim = "\033[m"

######################################################################################################################################################
# primeiro passo: inserção de dados
# eX_tX_pX_sX (sendo que cada X é substituído pela avaliação da pessoa em 

#cria-se uma lista vazia de candidatos
lista_candidatos = []

#função para inserir um candidato
def candidato(lista_candidatos):
    """
    Pede o nome e as 4 notas de cada candidatos
    """
    padrao_espera()

    #cabeçalho
    X = (f"Insira o nome e as notas do {len(lista_candidatos)+1}º candidato")
    sep(X)

    nome= input(f"{NVerde}Digite o nome do Candidato: {Corfim}")
    
    # entrevista
    while True:
        try:
            e = float(input(f"{NAmarelo}Digite a nota do Candidaton {nome} na entrevista: {Corfim}"))
            if e >= 0 and e <= 10:
                break
            else:
                print(f"{NVermelho} Digite um numero entre 0 e 10:")
        except:
            print(f"{NVermelho} Digite um numero entre 0 e 10:")
    
    # teste teorico
    while True:
        try:
            t = float(input(f"{NAmarelo}Digite a nota do Candidaton {nome} no teste teorico: {Corfim}"))
            if t >= 0 and t <= 10:
                break
            else:
                print(f"{NVermelho} Digite um numero entre 0 e 10:")
        except:
            print(f"{NVermelho} Digite um numero entre 0 e 10:")
        
    # teste pratico
    while True:
        try:
            p = float(input(f"{NAmarelo}Digite a nota do Candidaton {nome} no teste pratico: {Corfim}"))
            if p >= 0 and p <= 10:
              break
            else:
                print(f"{NVermelho} Digite um numero entre 0 e 10:")
        except:
            print(f"{NVermelho} Digite um numero entre 0 e 10:")
    
    # avaliação em soft skills
    while True:
        try:
            s = float(input(f"{NAmarelo}Digite a nota do Candidaton {nome} na valiação em soft skills: {Corfim}"))
            if t >= 0 and t <= 10:
                break
            else:
                print(f"{NVermelho} Digite um numero entre 0 e 10:")
        except:
            print(f"{NVermelho} Digite um numero entre 0 e 10:")

    nota = f"e{e}_t{t}_p{p}_s{s}"

    tupla_candidato = (nome, nota)
    lista_candidatos.append(tupla_candidato)
    return lista_candidatos

######################################################################################################################################################
# Função que define notas minimas:

def minimas():
    """
    Define as notas minimas para um candidato ser aprovado
    """
    padrao_espera()

    #cabeçalho
    X = (f"Definição de notas mínimas: ")
    sep(X)
    
    while True:
        try:   
            be = float(input(f"{NAmarelo}Digite a nota minima na entrevista: {Corfim}"))
            if be >= 0 and be <= 10:
                break
            else:
                print(f"{NVermelho} Digite um numero entre 0 e 10:")
        except:
            print(f"{NVermelho} Digite um numero entre 0 e 10:")        
    # teste teorico
    while True:
        try:  
            bt = float(input(f"{NAmarelo}Digite a nota minima no teste teorico: {Corfim}"))
            if bt >= 0 and bt <= 10:
                break
            else:
                print(f"{NVermelho} Digite um numero entre 0 e 10:")
        except:
            print(f"{NVermelho} Digite um numero entre 0 e 10:")
    # teste pratico
    while True:
        try:  
            bp = float(input(f"{NAmarelo}Digite a nota minima no teste pratico: {Corfim}"))
            if bp >= 0 and bp <= 10:
                break
            else:
                print(f"{NVermelho} Digite um numero entre 0 e 10:")
        except:
            print(f"{NVermelho} Digite um numero entre 0 e 10:")
    # avaliação em soft skills
    while True:
        try:  
            bs = float(input(f"{NAmarelo}Digite a nota minima na valiação em soft skills: {Corfim}"))
            if bs >= 0 and bs <= 10:
                break
            else:
                print(f"{NVermelho} Digite um numero entre 0 e 10:")
        except:
            print(f"{NVermelho} Digite um numero entre 0 e 10:")

    padrao_espera()

    return(be,bt,bp,bs)

######################################################################################################################################################
# Definição de Aprovados e Reprovados

def busca():
    """
    Função que fatia a String e avalia se cada dandidato passou ou não adionando à uma lista.
    """
    X = (f"Apresentação de Aprovados")
    sep(X)        

    print(f"{NVerde}As Notas de Corte definidas foram: {Corfim}")
    print(f"{NAmarelo}Entrevista: {NBranco}{be}\n{NAmarelo}Teste Teórico: {NBranco}{bp}\n{NAmarelo}Teste pratico {NBranco}{bp}\n{NAmarelo}Avaliação em soft skills: {NBranco}{bs}{Corfim}")

    aprovados = []
    reprovados = []

    for i in range(len(lista_candidatos)):
        e_index = lista_candidatos[i][1].index("e")
        t_index = lista_candidatos[i][1].index("t")
        p_index = lista_candidatos[i][1].index("p")
        s_index = lista_candidatos[i][1].index("s")

        e_nota = float(lista_candidatos[i][1][e_index+1:t_index-1])
        t_nota = float(lista_candidatos[i][1][t_index+1:p_index-1])
        p_nota = float(lista_candidatos[i][1][p_index+1:s_index-1])
        s_nota = float(lista_candidatos[i][1][s_index+1:])


        if e_nota >= be and t_nota >= bt and p_nota >= bp and s_nota >= bs:
            aprovados.append(lista_candidatos[i])
        else:
            reprovados.append(lista_candidatos[i])

    if len(aprovados) == 0:
        print(f"{NVermelho}\nNão houve candidatos aprovados {Corfim}")

    else:
        print(f"{NVerde}\nOs candidatos aprovados foram: {Corfim}")
        print(f"{NCiano}(em ordem amfabética) {Corfim}")

        aprovados.sort()

        for i in range(len(aprovados)):
            print (f"{NAmarelo}{aprovados[i][0]} - {NCinza}{aprovados[i][1]}{Corfim}")

######################################################################################################################################################
# Exclui um candidato

def exclusao():
    X = (f"Exclusão de candidato")
    sep(X)   

    print(f"{NVerde}\nConfira a lista dos candidatos inseridos até o momento:{Corfim}")
    for i, nome in enumerate(lista_candidatos):
        print (f"{NAmarelo}{i+1} - {nome[0]} - {NCinza}{nome[1]}{Corfim}")

    while True:
        try:
            excluido = int(input(f"\n{NCiano}Selecione o candidato a ser excluido pelo incice acima: {Corfim}"))
            excluido = excluido - 1
            break
        except:
            print(f"{NVermelho} Digite apenas numeros inteiros:")
            
            
    if excluido in range(len(lista_candidatos)):
        print(f"{NAmarelo}O candidato: {lista_candidatos[i][0]} será excluido{Corfim}")
        while True:
            excluido = input(f"{NVermelho}\nConfirma a excluisão de {lista_candidatos[i][0]}? [S/N]: {Corfim}").upper()
            if excluido == "N":

                print(f"{NVerde}O candidato {lista_candidatos[i][0]} não foi excluido {Corfim}")
                break
            elif excluido =="S":
                print(f"{NVerde} O candidato {lista_candidatos[i][0]} foi excluido {Corfim}")
                lista_candidatos.pop(i)
                
                break
            else:  
                print(f"{NVermelho}Digite apenas S para sim ou N para não{Corfim}")


######################################################################################################################################################
######################################################################################################################################################
# Executa a inserção dos candidatos

#Rodar o primeiro Candidato
lista_candidatos = candidato(lista_candidatos)

#Rodar do segundo candidato à frente
while True:
    resp1 = input(f"{NCiano}Deseja inserir mais um candidato? [S/N] {Corfim}")
    resp1= resp1.upper()
    if resp1 == "S": # Se Sim
        candidato(lista_candidatos)
        
    elif resp1 == "N": #se não
        break
    
    else: # bug
        print(f"{NVermelho}Digite apenas S para sim ou N para não{Corfim}")

######################################################################################################################################################
# Execução a definicação de cortes

be,bt,bp,bs = minimas()
busca()

######################################################################################################################################################
# Execução Secundária - Alteração de dados e finalização 

while True:
    sep3()

    print(f"{NCiano}\nSelecione entre as 3 opções abaixo: {Corfim}")
    print(f"{NAmarelo}1 - Inserir novos candidato{Corfim}" )
    print(f"{NAmarelo}2 - Excluir um candidato{Corfim}" )
    print(f"{NAmarelo}3 - Redefinir Notas de Corte{Corfim}")
    print(f"{NAmarelo}4 - Imprimir Aprovados{Corfim}")
    print(f"{NAmarelo}5 - Sair do programa{Corfim}")
    decisao = input(f"{NVerde}Selecione a ação desejada: {Corfim}")

    if decisao == "1":
        candidato(lista_candidatos)

    if decisao == "2":
        exclusao()


    elif decisao == "3":
        be,bt,bp,bs = minimas()
        busca()
    elif decisao == "4":
        busca()
    elif decisao == "5":
        X = (f"Obrigado por usar nosso programa")
        sep(X)
        break
    else:
        print(f"{NVermelho}Digite apenas 1, 2 ou 3{Corfim}")
        





