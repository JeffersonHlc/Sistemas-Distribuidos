import hashlib
import time


def calcular_hash_sha1(dados):
    return hashlib.sha1(dados.encode()).hexdigest()


def salvar_hash_em_arquivo(hash_valor):
    with open('hash_bloco.txt', 'w') as arquivo:
        arquivo.write(hash_valor)


def carregar_hash_do_arquivo():
    with open('hash_bloco.txt', 'r') as arquivo:
        return arquivo.read()


def modificar_bloco(dados):
    novos_dados = 'X' + dados[1:]
    return novos_dados


def executar_simulacao():
    bloco_dados = "Dados originais do bloco"

    hash_inicial = calcular_hash_sha1(bloco_dados)
    salvar_hash_em_arquivo(hash_inicial)
    print(f"Hash original salvo (SHA-1): {hash_inicial}")

    time.sleep(3)

    bloco_dados_modificado = modificar_bloco(bloco_dados)
    print(f"Bloco modificado: {bloco_dados_modificado}")

    novo_hash = calcular_hash_sha1(bloco_dados_modificado)
    print(f"Novo hash gerado (SHA-1): {novo_hash}")

    hash_salvo = carregar_hash_do_arquivo()
    print(f"Hash salvo para comparação: {hash_salvo}")

    if novo_hash == hash_salvo:
        print("Nenhuma alteração feita.")
    else:
        print("O bloco foi modificado.")

executar_simulacao()
