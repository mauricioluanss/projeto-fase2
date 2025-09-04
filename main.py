# aqui eu to criando a matriz para poder manipular os dados
def cria_matriz(arquivo) -> list[str]:
    try:
        matriz = []
        for linha in arquivo:
            nova_linha = linha[:-1]
            matriz.append(nova_linha.split(","))
        return matriz
    except Exception as e:
        print(f"Erro ao converter o csv para matriz: {e}")
        exit()


# retorno so a linha de cabeçalho da matriz
def cabecalho_matriz(matriz) -> list[str]:
    return matriz[0]


# retorno todas as linhas do corpo da matriz, exceto a primeira, qu é o cabeçalho
def corpo_matriz(matriz) -> list[list[str]]:
    return matriz[1:]


# retorna uma lista de dicionarios, onde cada elemento representa uma linha do csv original.
# as chaves são os nomes das colunas e os valores são os valores das colunas.
def cria_dicionario(
    coluna: list[str], linhas: list[list[str]]
) -> list[dict[str, str | float]]:
    dados_meteorologicos = []
    try:
        for elemento in linhas:
            dados_meteorologicos.append(
                {
                    coluna[0]: elemento[0],  # "data": "01/01/1961",
                    coluna[1]: float(elemento[1]),  # "precip": 8.6
                    coluna[2]: float(elemento[2]),  # ...
                    coluna[3]: float(elemento[3]),
                    coluna[4]: float(elemento[4]),
                    coluna[5]: float(elemento[5]),
                    coluna[6]: float(elemento[6]),
                    coluna[7]: float(elemento[7]),
                }
            )
        return dados_meteorologicos
    except IndexError as indexError:
        print(f"Erro: Coluna/linha com número insuficiente de elementos: {indexError}")
    except TypeError as typeError:
        print(f"Erro: tipo de dado inválido em coluna ou linha: {typeError}")
    except ValueError as valueError:
        print(f"Erro: valor inválido na conversão para float: {valueError}")
        # exit()? <- devo colocar exit em cada execpet? nao quero que o prgrama continue se tiver erro


def main():
    caminho_arquivo = "dados_meteorologicos.csv"
    with open(caminho_arquivo, "r") as arquivo:
        matriz = cria_matriz(arquivo)

    cabecalho = cabecalho_matriz(matriz)
    corpo = corpo_matriz(matriz)
    dados_meteorologicos = cria_dicionario(cabecalho, corpo)

    print(dados_meteorologicos)


main()
