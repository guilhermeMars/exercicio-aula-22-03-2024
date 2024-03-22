# https://colab.research.google.com/drive/1lwzcA6fe6bLEdrpYmPwTu-xjo-VJQlFi?usp=sharing

import pandas as pd

# URL do arquivo CSV com dados do IBGE no GitHub
url = "https://raw.githubusercontent.com/guilhermeMars/exercicio-aula-22-03-2024/main/Dados%20Tratados%20-%20EBT.csv"
# Carregar os dados em um DataFrame
df = pd.read_csv(url, sep=',', encoding='ISO-8859-1')
# Exibir as linhas do DataFrame usando display
df.head()

### CONTINUE E ATUALIZE O Código Python e CRIE OS GRAFICOS PARA ESSE DataSet com dados do IBGE no GitHub

### FAÇA UPLOAD (das atividades) NA PASTA DO TEAMS [Entrega-Aula05]

from matplotlib import pyplot as plt
import seaborn as sns

df_agrupado = df.groupby('uf')['nota'].sum().reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(x='uf', y='nota', data=df_agrupado, palette='viridis')
plt.title('Escala de Notas pelo Estado')
plt.xlabel('Estados')
plt.ylabel('Notas')
plt.xticks(rotation=45)  # Rotacionar os rótulos do eixo x para melhor legibilidade
plt.tight_layout()  # Ajustar layout para melhor visualização
plt.show()
