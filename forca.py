import random
import emojis

palavras = {
    'bicho' : ['saguin','timbu','sabiá','piolho-de-cobra','bafomete','calango','lumbriga','tanajura','paimon'],
    'comida' : ['baiao-de-dois','cuscuz','buchada','tanajura']
}


def roda_roda(palavras):
        
    categoria = random.choice(list(palavras)) 
    palavra = random.choice(palavras[categoria])

    return categoria, palavra


def butar_tracinho(palavra):
    return len(palavra) * ' '

    
def pesadao(palavra_secreta, categoria):
    print(emojis.encode(rf"""
     RODA RODA JEQUITÊ
======= DICA: {categoria.upper()} ==========
___________
|          |
|    :gun:з= :santa: =ε/̵͇̿̿/’̿’̿ ̿ 
|        ( . )  
|       _//🍆\\_  
|    
|     
|        {' '.join(list(palavra_secreta))}
         {len(palavra_secreta) * "_ "}
"""))



def troca_troca_jequete(indices, letra, palavra_secreta):

    nova_palavra_secreta = list(palavra_secreta)

    for index in indices:
        nova_palavra_secreta[index] = letra

    return ''.join(nova_palavra_secreta)
    
    
            
def pegar_indices(palavra, letra_escolhida):

    indices = []

    for indice, letra in enumerate(palavra):
        if letra == letra_escolhida:
            indices.append(indice)

    return indices    




categoria, palavra = roda_roda(palavras)
palavra_secreta = butar_tracinho(palavra)

for i in range(10):
    
    pesadao(palavra_secreta, categoria)
    letra_escolhida = input('Informe uma letra: ').lower()

    indices = pegar_indices(palavra, letra_escolhida)
    palavra_secreta = troca_troca_jequete(indices, letra_escolhida, palavra_secreta)

