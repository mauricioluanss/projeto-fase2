import matplotlib.pyplot as plt


def cria_matriz(arquivo) -> list[str]:
    """Lê o arquivo CSV e o transforma em uma matriz (lista de listas)."""
    try:
        matriz = []
        for linha in arquivo:
            nova_linha = linha[:-1]
            matriz.append(nova_linha.split(","))
        return matriz
    except Exception as e:
        print(f"Erro ao converter o csv para matriz: {e}")
        exit()


def cabecalho_matriz(matriz) -> list[str]:
    """Retorna a primeira linha da matriz, que é o cabeçalho."""
    return matriz[0]


def corpo_matriz(matriz) -> list[list[str]]:
    """Retorna todas as linhas da matriz, exceto o cabeçalho."""
    return matriz[1:]


def transforma_matriz_em_dict(
    coluna: list[str], linhas: list[list[str]]
) -> list[dict[str, str | float]]:
    """Converte a matriz de dados em uma lista de dicionários."""
    dados_meteorologicos = []
    try:
        for elemento in linhas:
            dados_meteorologicos.append(
                {
                    coluna[0]: elemento[0],
                    coluna[1]: float(elemento[1]),
                    coluna[2]: float(elemento[2]),
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


def captura_data(
    msg_input: str, msg_erro: str, valor_minimo: int, valor_maximo: int
) -> str:
    """Pede um dado ao usuário e garante que seja um número dentro de um intervalo válido."""
    while True:
        data_str = input(f"{msg_input}: ")
        if not data_str.isdigit():
            print(msg_erro)
            continue

        data_int = int(data_str)
        if not (valor_minimo <= data_int <= valor_maximo):
            print(
                f"Valor inválido. O número deve estar entre {valor_minimo} e {valor_maximo}."
            )
            continue

        return data_str


def define_intervalo_data() -> tuple[str, str]:
    """Captura e valida o intervalo de datas (inicial e final) informado pelo usuário."""
    while True:
        mes_inicial = captura_data(
            "Digite o mês inicial (MM)", "Inválido. Apenas números.", 1, 12
        )
        ano_inicial = captura_data(
            "Digite o ano inicial (AAAA)", "Inválido. Apenas números.", 1961, 2016
        )
        mes_final = captura_data(
            "Digite o mês final (MM)", "Inválido. Apenas números.", 1, 12
        )
        ano_final = captura_data(
            "Digite o ano final (AAAA)", "Inválido. Apenas números.", 1961, 2016
        )

        ano_inicial_int = int(ano_inicial)
        ano_final_int = int(ano_final)
        mes_inicial_int = int(mes_inicial)
        mes_final_int = int(mes_final)

        if ano_inicial_int > ano_final_int or (
            ano_inicial_int == ano_final_int and mes_inicial_int > mes_final_int
        ):
            print("O período inicial não pode ser posterior ao período final.")
            continue
        break

    data_inicial_formatada = f"{mes_inicial}/{ano_inicial}"
    data_final_formatada = f"{mes_final}/{ano_final}"

    return data_inicial_formatada, data_final_formatada


def captura_filtro_visualizacao() -> str:
    """Mostra as opções de visualização e captura a escolha do usuário."""
    while True:
        print("\nQual tipo de dado você deseja visualizar?")
        print("1. Todos os dados")
        print("2. Apenas Precipitação")
        print("3. Apenas Temperaturas (máxima e mínima)")
        print("4. Apenas Umidade e Vento")

        escolha = input(">> Escolha uma opção de visualização: ")
        if escolha in ["1", "2", "3", "4"]:
            return escolha
        else:
            print("\nOpção inválida. Por favor, escolha um número de 1 a 4.")


def filtrar_dados_por_periodo(
    dados: list[dict], data_inicial_str: str, data_final_str: str
) -> list[dict]:
    """Filtra a lista completa de dados para um período de tempo específico."""
    dados_filtrados = []

    mes_inicial, ano_inicial = data_inicial_str.split("/")
    limite_inicial = int(ano_inicial) * 100 + int(mes_inicial)
    mes_final, ano_final = data_final_str.split("/")
    limite_final = int(ano_final) * 100 + int(mes_final)

    for registro in dados:
        data_do_registro_str = registro["data"]
        dia_str, mes_str, ano_str = data_do_registro_str.split("/")
        data_registro_num = int(ano_str) * 100 + int(mes_str)

        if limite_inicial <= data_registro_num <= limite_final:
            dados_filtrados.append(registro)
    return dados_filtrados


def exibir_dados(
    dados_filtrados: list[dict], filtro_visualizacao: str, cabecalho: list[str]
):
    """Exibe os dados filtrados em formato de tabela no console."""
    if not dados_filtrados:
        print("\nNenhum registro encontrado para o período e filtro informados.")
        return

    headers_a_exibir = []
    if filtro_visualizacao == "1":
        headers_a_exibir = cabecalho
    elif filtro_visualizacao == "2":
        headers_a_exibir = [cabecalho[0], cabecalho[1]]  # data, precip
    elif filtro_visualizacao == "3":
        headers_a_exibir = [
            cabecalho[0],
            cabecalho[2],
            cabecalho[3],
        ]  # data, maxima, minima
    elif filtro_visualizacao == "4":
        headers_a_exibir = [
            cabecalho[0],
            cabecalho[6],
            cabecalho[7],
        ]  # data, um_relativa, vel_vento

    print("-" * 80)
    print("".join([f"{h:<18}" for h in headers_a_exibir]))
    print("-" * 80)

    for registro in dados_filtrados:
        valores_da_linha = []
        for header in headers_a_exibir:
            valor_str = f'{str(registro.get(header, "N/A")):<18}'
            valores_da_linha.append(valor_str)
        print("".join(valores_da_linha))

    print("-" * 80)
    print(f"Total de {len(dados_filtrados)} registros exibidos.")


def encontrar_mes_mais_chuvoso(dados: list[dict]) -> tuple[str, float]:
    """Calcula e encontra o mês com o maior volume de chuva em todo o período."""
    precipitacao_por_mes = {}
    for registro in dados:
        data_str = registro["data"]
        mes_ano_chave = data_str[3:]

        precipitacao_dia = registro.get("precip", 0.0)

        if mes_ano_chave in precipitacao_por_mes:
            precipitacao_por_mes[mes_ano_chave] += precipitacao_dia
        else:
            precipitacao_por_mes[mes_ano_chave] = precipitacao_dia

    if not precipitacao_por_mes:
        return "Nenhum dado", 0.0

    mes_mais_chuvoso = max(precipitacao_por_mes, key=precipitacao_por_mes.get)
    maior_precipitacao = precipitacao_por_mes[mes_mais_chuvoso]

    return mes_mais_chuvoso, maior_precipitacao


def calcular_media_temp_minima_mensal(dados: list[dict]) -> dict:
    """Calcula a média de temperatura mínima para um mês específico entre 2006 e 2016."""
    print("\nMédia da Temperatura Mínima de um Mês (2006-2016)")
    mes_str = captura_data(
        "Digite o mês que deseja analisar (01-12)", "Mês inválido.", 1, 12
    )

    temps_por_mes_ano = {}

    for registro in dados:
        dia_str, mes_registro_str, ano_registro_str = registro["data"].split("/")
        ano_registro_int = int(ano_registro_str)

        if 2006 <= ano_registro_int <= 2016 and mes_registro_str == mes_str:
            chave = f"{mes_registro_str}/{ano_registro_str}"
            temp_minima = registro.get("minima", 0.0)

            if chave not in temps_por_mes_ano:
                temps_por_mes_ano[chave] = []
            temps_por_mes_ano[chave].append(temp_minima)

    medias_finais = {}
    for chave, lista_de_temps in temps_por_mes_ano.items():
        if lista_de_temps:
            media = sum(lista_de_temps) / len(lista_de_temps)
            medias_finais[chave] = media

    return medias_finais, mes_str


def gerar_grafico_medias_mensais(dados_medias: dict, mes_analisado: str):
    """Gera e exibe um gráfico de barras com as médias de temperatura."""
    if not dados_medias:
        print("Não há dados para gerar o gráfico. Execute a opção 3 primeiro.")
        return

    anos_ordenados = sorted(dados_medias.keys())
    rotulos_anos = [ano[3:] for ano in anos_ordenados]
    valores_medias = [dados_medias[ano] for ano in anos_ordenados]

    plt.figure(figsize=(10, 6))
    plt.bar(rotulos_anos, valores_medias, color="skyblue")

    plt.xlabel("Ano")
    plt.ylabel("Temperatura Mínima Média (°C)")
    plt.title(f"Média da Temperatura Mínima para o Mês {mes_analisado} (2006-2016)")
    plt.xticks(rotation=45)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.tight_layout()

    print("\nExibindo o gráfico...")
    plt.show()


def calcular_media_geral(dados_medias: dict) -> float:
    """Calcula a média geral a partir de um dicionário com médias anuais."""
    medias_anuais = dados_medias.values()
    if not medias_anuais:
        return 0.0

    media_geral = sum(medias_anuais) / len(medias_anuais)
    return media_geral


def main():
    """Função principal que inicializa os dados e executa o menu da aplicação."""
    caminho_arquivo = (
        "Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv"
    )
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            matriz = cria_matriz(arquivo)
    except FileNotFoundError:
        print(f"ERRO FATAL: Arquivo '{caminho_arquivo}' não encontrado.")
        print(
            "Verifique se o arquivo está na mesma pasta que o programa e tente novamente."
        )
        exit()

    cabecalho = cabecalho_matriz(matriz)
    corpo = corpo_matriz(matriz)
    dados_meteorologicos = transforma_matriz_em_dict(cabecalho, corpo)

    if not dados_meteorologicos:
        print("Não foi possível carregar os dados do arquivo.")
        exit()

    dados_media_temp = None
    mes_analisado_para_grafico = None

    # Menu principal
    while True:
        print("\nAnálise de Dados Meteorológicos de Porto Alegre")
        print("1. Visualizar dados por período")
        print("2. Encontrar o mês mais chuvoso")
        print("3. Calcular a média da temperatura mínima de um mês (2006-2016)")
        print("4. Gerar gráfico de barras das médias")
        print("5. Calcular média geral da temperatura mínima de um mês (2006-2016)")
        print("6. Sair")

        escolha = input(">> Escolha uma opção: ")
        if escolha == "1":
            print("\nVisualização de Dados por Período")
            data_inicial, data_final = define_intervalo_data()
            filtro_escolhido = captura_filtro_visualizacao()
            dados_do_periodo = filtrar_dados_por_periodo(
                dados_meteorologicos, data_inicial, data_final
            )
            exibir_dados(dados_do_periodo, filtro_escolhido, cabecalho)
            input("Pressione Enter para voltar ao menu...")

        elif escolha == "2":
            print("\nMês Mais Chuvoso em Todo o Período")
            mes, total_chuva = encontrar_mes_mais_chuvoso(dados_meteorologicos)
            print(
                f"O mês mais chuvoso foi {mes} com um total de {total_chuva:.2f} mm de precipitação."
            )
            input("\nPressione Enter para voltar ao menu...")

        elif escolha == "3":
            dados_media_temp, mes_analisado_para_grafico = (
                calcular_media_temp_minima_mensal(dados_meteorologicos)
            )

            if not dados_media_temp:
                print(
                    f"Nenhum dado encontrado para o mês {mes_analisado_para_grafico} entre 2006 e 2016."
                )
            else:
                print(f"\nResultados para o mês {mes_analisado_para_grafico}:")
                for mes_ano, media in sorted(dados_media_temp.items()):
                    print(f" - {mes_ano}: Média de {media:.2f}°C")

            input("\nPressione Enter para voltar ao menu...")

        elif escolha == "4":
            if dados_media_temp is None:
                print(
                    "\nErro: Você precisa executar a opção 3 primeiro para gerar os dados do gráfico."
                )
            else:
                gerar_grafico_medias_mensais(
                    dados_media_temp, mes_analisado_para_grafico
                )

            input("\nPressione Enter para voltar ao menu...")

        elif escolha == "5":
            if dados_media_temp is None:
                print(
                    "\nErro: Você precisa executar a opção 3 primeiro para gerar os dados."
                )
            else:
                media_geral = calcular_media_geral(dados_media_temp)
                print("\nMédia Geral da Temperatura Mínima")
                print(
                    f"A média geral da temperatura mínima para o mês {mes_analisado_para_grafico} no período de 2006-2016 foi de {media_geral:.2f}°C."
                )

            input("\nPressione Enter para voltar ao menu...")

        elif escolha == "6":
            print("Encerrando o programa.")
            break

        else:
            print("\nOpção inválida. Por favor, escolha um número de 1 a 6.")
            input("Pressione Enter para tentar novamente...")


main()
