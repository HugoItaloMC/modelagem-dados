# Funcões auxiliares
import math
import random
import string

from datetime import datetime
from math import log2, sqrt


def gerar_string(frase: bool = False) -> str:
    #  Gerar string aleatória
    tamanho = 10
    if frase:
        tamanho = 30
    texto: str = ''.join(random.choices(string.ascii_lowercase + string.digits, k=tamanho))

    texto = ''.join([c if c.isalpha() else ' ' for c in texto])
    return texto


def gerar_inteiros() -> int:
    valor: int = random.randint(1, 100)
    return valor


def gerar_float(digitios: int = 1) -> float:
    #  Funcão para gerar números reais (com pontos decimais) `aleatórios`
    # ATTR: `digitos` total de digítos para gerar o número aleatório
    # Lógica para gerar dezenas, centenas, milhares
    valor: float = 0
    #  randomicos com casas decimais utilizando os operadores `<<` e `>>`
    #  Lembrando que é para caso de estudos, está lógica ñ foi testada em aplicacões mais complexas (API's)
    if digitios == 1:
        valor = random.uniform(1000 >> 9, 1 << 3)  # Unidades
    elif digitios == 2:
        valor = random.uniform((400 >> 2) - 1, +10)  # Dezenas
    elif digitios == 3:
        valor = random.uniform((7 << 7) + (3 << 5), +10)  # Centenas
    else:
        valor = random.uniform((10 << 10) - (8 << 5), +1000)  # Milhares

    return round(valor, 2)  # Arrendondando 2 digitos após o ponto decimal


def data_para_string(data: datetime) -> str:
    #  Formatando dados do tipo `data` para o tipo `string`

    return data.strftime("%d/%m/%Y às %H:%M:%S")


def string_hexadecimal() -> str:
    return "#"+"".join([random.choice("123456789ABCDEF") for _ in range(6)])


if __name__ == '__main__':
    print(gerar_float())
    print(gerar_float(digitios=2))
    print(gerar_float(digitios=3))
    print(gerar_float(digitios=4))
    print(gerar_string())
    print(data_para_string(datetime.now()))
    print(string_hexadecimal())
    print(10 >> 2)
