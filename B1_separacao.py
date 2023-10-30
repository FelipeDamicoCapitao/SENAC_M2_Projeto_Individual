NCinza = "\033[1;30;1m"
NVermelho = "\033[1;31;1m"
NVerde = "\033[1;32;1m"
NAmarelo = "\033[1;33;1m"
NMagenta = "\033[1;34;1m"
NRosa = "\033[1;35;1m"
NCiano = "\033[1;36;1m"
NBranco = "\033[1;37;1m"
Corfim = "\033[m"

# ###########################################################################################################
# Função Cabeçalho de separação

#grande
def sep(X):
    L = 80

    Y = int(((L-len(X)))/2)
    Y2 = (" "*Y)
    print("")
    print(f"{NBranco}={Corfim}"*L)
    print(f"{Y2}{NBranco}{X}{Corfim}")
    print(f"{NBranco}={Corfim}"*L)
    print("")
#pequeno
def sep2(X):
    L = 40

    Y = int(((L-len(X)))/2)
    Y2 = (" "*Y)
    print("")
    print(f"{NBranco}={Corfim}"*L)
    print(Y2,X,Y2)
    print(f"{NBranco}={Corfim}"*L)
# divisão de uma linha
def sep3():
    L = 80
    Y2 = (" "*L)
    print("")
    print(f"{NCinza}={Corfim}"*L)