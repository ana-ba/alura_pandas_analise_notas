import pandas as pd

# Importando o dataset a partir de uma URL pública
url = "https://raw.githubusercontent.com/alura-cursos/pandas-conhecendo-a-biblioteca/main/desafios/alunos.csv"
alunos = pd.read_csv(url)

# Exibindo as 7 primeiras linhas do DataFrame
print(alunos.head(7))

# Exibindo as 5 últimas linhas do DataFrame
print(alunos.tail(5))

# Exibindo a quantidade de linhas e colunas do DataFrame
print(alunos.shape)

# Exibindo os nomes das colunas do DataFrame
print(alunos.columns)

# Gerando estatísticas descritivas para as colunas numéricas
print(alunos.describe())

# Verificando a quantidade de valores nulos em cada coluna
print(alunos.isnull().sum())

# Substituindo valores nulos por 0
alunos_nulos = alunos.fillna(0)

# Removendo linhas que contenham valores nulos
alunos.dropna(inplace=True)

# Removendo os alunos “Alice” e “Carlos” da base de dados
alunos.drop([7, 8], inplace=True)

# Selecionando alunos aprovados (condição booleana)
selecao = alunos['Aprovado'] == True
alunos_aprovados = alunos.replace(7.0, 8.0)

# Calculando pontos extras (40% da nota original)
alunos['Pontos_extras'] = alunos['Notas'] * 0.40

# Calculando a nota final somando pontos extras e limitando o valor máximo a 10
alunos['Nota_final'] = alunos['Notas'] + alunos['Pontos_extras']
alunos['Nota_final'] = alunos['Nota_final'].clip(lower=0, upper=10)

# Definindo a situação do aluno com base na nota final
alunos['Situação'] = alunos['Nota_final'].apply(lambda x: "Aprovado" if x > 7 else "Reprovado")

# Exibindo o DataFrame final com as novas colunas e ajustes
print(alunos)
