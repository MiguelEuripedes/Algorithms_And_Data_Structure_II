
results_csv = r'C:\Users\Miguel\Documents\SEMESTRE 2023.2 - Eng.Comp\AEDII\projeto2\AVL\implementations\results\results.csv'
import pandas as pd
import plotly.express as px

# Ler o CSV diretamente
df = pd.read_csv(results_csv)

# Filtrar o DataFrame para excluir entradas com algoritmo igual a "List"
df_filtered = df[df["algorithm"] != "List"]

# Criar o gráfico de barras usando Plotly com o DataFrame filtrado
fig = px.bar(df_filtered, x="algorithm", y="searchTime", color="archiveName",
             title="Tempo de Busca por Algoritmo e Livro (excluindo List)")

# Personalizar rótulos dos eixos
fig.update_xaxes(title_text="Algoritmo")
fig.update_yaxes(title_text="Tempo de Busca")

# Exibir o gráfico
fig.show()