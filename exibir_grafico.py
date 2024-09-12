from analise import carregar_planilha, gerar_grafico

# Caminho da planilha de exemplo
caminho_planilha = 'exemplo_planilha.xlsx'

# Carregar a planilha
df = carregar_planilha(caminho_planilha)

# Exibir as primeiras linhas para verificar os dados
print(df.head())

# Gerar o gráfico
gerar_grafico(df, 'ColunaX', 'ColunaY', titulo='Gráfico Exibido na Tela')
