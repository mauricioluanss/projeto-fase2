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
def transforma_matriz_em_dict(
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


def captura_data(msg_input, msg_erro):
    while True:
        data = input(f"{msg_input}: ")
        # vou ter que colocar as validações sobre mes e ano aqui dentro <--

        if data.isdigit():
            return data
        else:
            print(f"{msg_erro}")


def define_intervalo_data():
    while True:
        mes_inicial = captura_data(
            "Digite o mês inicial (MM): ", "Inválido. Digite o mês no formato (MM)"
        )
        ano_inicial = captura_data(
            "Digite o ano inicial (AAAA): ", "Inválido. Digite o ano no formato (AAAA)"
        )
        mes_final = captura_data(
            "Digite o mês final (MM):", "Inválido. Digite o mês no formato (MM)"
        )
        ano_final = captura_data(
            "Digite o ano final (AAAA): ", "Inválido. Digite o ano no formato (AAAA)"
        )

        # mover essa parte para dentro de captura data
        if not (1 <= int(mes_inicial) <= 12) or not (1 <= int(mes_final) <= 12):
            print("Intervalo dos meses deve estar entre 1 e 12. Tente novamente.")
            continue
        if int(ano_inicial) > int(ano_final):
            print("Ano inicial maior que ano final. Tente novamente.")
            continue
        if int(ano_inicial) not in range(1961, 2017) or int(ano_final) not in range(
            1961, 2017
        ):
            print("Ano deve estar entre 1961 e 2016. Tente novamente.")
            continue
        break
    data_inicial = f"{mes_inicial}/{ano_inicial}"
    data_final = f"{mes_final}/{ano_final}"

    return data_inicial, data_final


def main():
    caminho_arquivo = "dados_meteorologicos.csv"
    try:
        with open(caminho_arquivo, "r") as arquivo:
            matriz = cria_matriz(arquivo)
    except FileNotFoundError:
        print("Arquivo não encontrado. Verifique o caminho do arquivo.")
        exit()

    cabecalho = cabecalho_matriz(matriz)
    corpo = corpo_matriz(matriz)
    dados_meteorologicos = transforma_matriz_em_dict(cabecalho, corpo)
    print(define_intervalo_data())  # teste pra ver como ta saindo o intervalo das data


main()
