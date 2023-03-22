import time

def pot_conj(n):
    pot = []
    for subconj in range(2**(n*n)):
        pot.append(conjPares(subconj,n))
    return pot
    
def conjPares(s, n):
    conj = []
    for i in range(n):
        for j in range(n):
            if bitLigado(i,j,n,s):
                conj.append((i+1, j+1))
    return conj

def bitLigado(i,j,n,s):
    return s&(1<<(i*n+j))!=0

def simetrica(subconj):
    for a, b in subconj:
        if (b, a) not in subconj:
            return False
    return True

def transitiva(subconj):
    for a, b in subconj:
        for c, d in subconj:
            if b == c and (a, d) not in subconj:
                return False
    return True

def reflexiva(subconj, n):
    for i in range(1, n+1):
        if (i, i) not in subconj:
            return False
    return True

def irreflexiva(subconj):
    for a, b in subconj:
        if a == b:
            return False
    return True

def equivalente(subconj, n):
    return simetrica(subconj) and transitiva(subconj) and reflexiva(subconj, n)

def injetora(subconj):
    valores_imagem = set()
    for _, imagem in subconj:
        if imagem in valores_imagem:
            return False
        valores_imagem.add(imagem)
    return True

def sobrejetora(subconj, n):
    valores_imagem = set()
    for _, imagem in subconj:
        valores_imagem.add(imagem)
    return len(valores_imagem) == n

def bijetora(subconj, n):
    return injetora(subconj) and sobrejetora(subconj, n)

def gerar_caracteristicas(n):
    resultado = pot_conj(n)
    caracteristicas = []
    for subconj in resultado:
        car = ''
        if simetrica(subconj):
            car += 'S'
        if transitiva(subconj):
            car += 'T'
        if reflexiva(subconj, n):
            car += 'R'
        if irreflexiva(subconj):
            car += 'I'
        if equivalente(subconj, n):
            car += 'E'
        if injetora(subconj):
            car += 'Fi'
        if sobrejetora(subconj, n):
            car += 'Fs'
        if bijetora(subconj, n):
            car += 'Fb'
        caracteristicas.append((list(subconj), car))
    return caracteristicas

caracteristicas = gerar_caracteristicas(int(input("Qual a quantidade de elementos no conjunto?")))

inicio = time.time()

with open('resultados.txt', 'w') as arquivo:
    for subconj, car in caracteristicas:
        arquivo.write(str(subconj) + ' ' + car + '\n')

fim = time.time()
tempoTotal = fim - inicio

print('O tempo para execucao foi de {:.3f}s'.format(tempoTotal))

with open('resultados.txt', 'a') as arquivo:
    arquivo.write("O tempo para a conclusão do programa foi de: {:.3f} segundos".format(tempoTotal))
