# aqui eu to criando a matriz para poder manipular os dados
def remove_newline(string) -> list[str]:
    nova_string = string[:-1]
    return nova_string


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


def colunas_matriz(matriz):
    colunas = matriz[0]
    return colunas


def main():
    caminho_arquivo = "dados_meteorologicos.csv"
    with open(caminho_arquivo, 'r') as arquivo:
        matriz = cria_matriz(arquivo)
        colunas = colunas_matriz(matriz)
        print(matriz)


main()
