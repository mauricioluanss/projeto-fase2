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
def cabecalho_matriz(matriz):
    return matriz[0]


# retorno todas as linhas do corpo da matriz, exceto a primeira, qu é o cabeçalho
def corpo_matriz(matriz):
    return matriz[1:]


# eu preciso fazer com que cada linha da matriz vire um dicionario, onde a chave é o nome da coluna e o valor é o elemento
def cria_dicionario(coluna, linhas):
    dados_meteorologicos = []
    for linha in linhas:
        dados_meteorologicos.append(
            {
                coluna[0]: linha[0],  # "data": "01/01/1961",
                coluna[1]: linha[1],  # "precip": "8.6" <-ja converto pra float aqui?
                coluna[2]: linha[2],  # ...
                coluna[3]: linha[3],
                coluna[4]: linha[4],
                coluna[5]: linha[5],
                coluna[6]: linha[6],
                coluna[7]: linha[7],
            }
        )
    # criei este aquivo só pra ver como os dados estão sendo salvos
    # APAGAR DEPOIS KKK
    with open("dicionario.txt", "w") as arquivo:
        arquivo.write(str(dados_meteorologicos))
    print(dados_meteorologicos)


def main():
    caminho_arquivo = "dados_meteorologicos.csv"
    with open(caminho_arquivo, "r") as arquivo:
        matriz = cria_matriz(arquivo)
        cabecalho = cabecalho_matriz(matriz)
        corpo = corpo_matriz(matriz)
        cria_dicionario(cabecalho, corpo)


main()
