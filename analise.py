import pandas as pd
import matplotlib.pyplot as plt

# Função para carregar a planilha
def carregar_planilha(caminho):
    # Lê o arquivo Excel
    df = pd.read_excel(caminho)
    return df

# Função para gerar gráfico
def gerar_grafico(df, coluna_x, coluna_y, titulo='Gráfico'):
    plt.figure(figsize=(10, 6))
    plt.plot(df[coluna_x], df[coluna_y], marker='o')
    plt.title(titulo)
    plt.xlabel(coluna_x)
    plt.ylabel(coluna_y)
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Caminho do arquivo Excel
    caminho_planilha = 'exemplo_planilha.xlsx'

    # Carregar a planilha
    df = carregar_planilha(caminho_planilha)

    # Exibir as primeiras linhas da planilha para garantir que foi carregada corretamente
    print(df.head())

    # Gerar o gráfico com as colunas desejadas
    gerar_grafico(df, 'ColunaX', 'ColunaY', titulo='Meu Gráfico Personalizado')
