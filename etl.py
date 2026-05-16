# no google pesquisar sempre em ingles ex 'pandas documentation read json file'
import pandas as pd
import os  # para usar comandos igual ao terminal e do computador - para me comunicar com meu sistema operacional
import glob  # para usar comandos igual ao terminal e do computador
# Uma função de extrect que le e concatena os jsons de uma pasta e retorna um dataframe
# >>>>> pd.read_json(path_or_buf=)
pasta = 'data'
# glob.glob() retorna uma lista de arquivos que correspondem ao padrão especificado
# arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
# df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
# df_total = pd.concat(df_list, ignore_index=True)
# print(df_total)

# Uma função de extract que le e concatena os jsons de uma pasta e retorna um dataframe


# def extract_data(pasta):
#    arquivos_json = glob.glob(os.path.join(pasta, '*.json'))
#    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
#    df_total = pd.concat(df_list, ignore_index=True)
#    return df_total


# print(extract_data(pasta))

# OR
def extrair_dados_e_consolidar(path: str) -> pd.DataFrame:
    arquivos_json = glob.glob(os.path.join(path, '*.json'))
    df_list = [pd.read_json(arquivo) for arquivo in arquivos_json]
    df_total = pd.concat(df_list, ignore_index=True)
    return df_total


# print(extrair_dados_e_consolidar(path=pasta))

# Uma função que transforma
def calcular_kpi_de_total_de_vendas(df: pd.DataFrame) -> pd.DataFrame:
    df['total'] = df['Quantidade'] * df['Venda']
    return df

# Uma função que da load dos dados para um arquivo csv ou parquet


def carregar_dados(df: pd.DataFrame, format_saida: list):
    """parametro que vai ser csv ou parque ou os dois 

    """
    print(format_saida)
    for formato in format_saida:
        if formato == 'csv':
            df.to_csv('data/dados.csv')
        if formato == 'parquet':
            df.to_parquet('data/dados.parquet')
    return 'Dados carregados com sucesso!'


def pipeline_calcular_kpi_de_vendas_consolidado(pasta_argumento: str, format_saida: list):
    data_frame = extrair_dados_e_consolidar(pasta_argumento)
    data_frame_calculado = calcular_kpi_de_total_de_vendas(df=data_frame)
    carregar_dados(df=data_frame_calculado, format_saida=format_saida)


# if __name__ == "__main__":
#    pasta_argumento = 'data'
#    print(extrair_dados_e_consolidar(path=pasta_argumento))
#    print(calcular_kpi_de_total_de_vendas(
#        extrair_dados_e_consolidar(path=pasta_argumento)))
#    format_saida = ['csv', 'parquet']
#    print(carregar_dados(df=calcular_kpi_de_total_de_vendas(
#        extrair_dados_e_consolidar(path=pasta_argumento)), format_saida=format_saida))
