import hashlib
import time
import threading
import random

def calcular_hash_sha1(dados):
    return hashlib.sha1(dados.encode()).hexdigest()

def modificar_bloco(dados):
    novos_dados = dados + str(random.randint(1, 10))
    return novos_dados

bloco_dados = "Dados originais do bloco"
hash_original = calcular_hash_sha1(bloco_dados)
print(f"Hash original salvo (SHA-1): {hash_original}")

descarte = False

def thread_modificadora():
    global bloco_dados
    while not descarte:
        time.sleep(5)
        if random.random() < 0.5:
            bloco_dados = modificar_bloco(bloco_dados)
            print(f"Bloco modificado: {bloco_dados}")

def thread_verificadora():
    global hash_original
    while not descarte:
        time.sleep(5)
        novo_hash = calcular_hash_sha1(bloco_dados)
        print(f"Novo hash gerado (SHA-1): {novo_hash}")
        if novo_hash == hash_original:
            print("Nenhuma alteração feita.")
        else:
            print("O bloco foi modificado!")
            hash_original = novo_hash

t_modificadora = threading.Thread(target=thread_modificadora)
t_verificadora = threading.Thread(target=thread_verificadora)

t_modificadora.start()
t_verificadora.start()

try:
    while not descarte:
        time.sleep(1)
except KeyboardInterrupt:
    print("Encerrando a simulação.")
    descarte = True
