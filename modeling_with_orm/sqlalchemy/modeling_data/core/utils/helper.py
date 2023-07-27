# Funcões auxiliares

import random
import string

from datetime import datetime


def gerar_string(frase: bool = False) -> str:
    #  Gerar string aleatória
    tamanho = 10
    if frase:
        tamanho = 30
    texto: str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=tamanho))

    texto = ''.join([c if c.isalpha() else ' ' for c in texto])
    return texto


def gerar_inteiros() -> int:
    valor: int =  random.randint(1, 100)
    return valor


def gerar_float(digitios: int = 1) -> float:
    #  Funcão para gerar números reais (com pontos decimais) `aleatórios`

    # Lógica para gerar dezenas, centenas, milhares
    valor: float = 0
    if digitios == 1:
        valor = random.uniform(1, 9)
    elif digitios == 2:
        valor = random.uniform(10, 99)
    elif digitios == 3:
        valor = random.uniform(100, 999)
    else:
        valor = random.uniform(1000, 9999)

    return round(valor, 2)  # Arrendondando 2 digitos após o ponto decimal


def data_para_string(data: datetime) -> str:
    #  Formatando dados do tipo `data` para o tipo `string`

    return data.strftime("%d/%m/%Y às %H:%M:%S")
