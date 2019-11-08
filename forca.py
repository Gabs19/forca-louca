import random

palavras = {
    'bicho' : ['saguin','timbu','sabiá','piolho-de-cobra','bafomete','calango','lumbriga','tanajura','paimon'],
    'comida' : ['baiao-de-dois','cuscuz','buchada','tanajura']
}


def roda_roda(palavras):
        
    categoria = random.choice(list(palavras)) 
    palavra = random.choice(palavras[categoria])

    return categoria, palavra


def butar_tracinho(palavra):
    return len(palavra) * '_ '

    
def pesadao(palavra_secreta,categoria):
    print(rf"""/
        RODA RODA JEQUITÊ
======= DICA : {categoria} =======
_____
|     |
|     O
|    \|/    
|     |
|    /ç\
|
        {palavra_secreta}

""")



def troca_troca_jequete(indices, letra):
    pass
    
            
def pegar_indices(palavra, letra_escolhida):

    indices = []

    for indice, letra in enumerate(palavra):
        if letra == letra_escolhida:
            indices.append(indice)

    return indices    




categoria, palavra = roda_roda(palavras)
palavra_secreta = butar_tracinho(palavra)

pesadao(palavra_secreta, categoria)

print(palavra)
print(pegar_indices(palavra,'a'))









