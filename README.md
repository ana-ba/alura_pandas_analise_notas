# 📊 Análise de Dados de Alunos com Pandas

Este projeto tem como objetivo explorar e manipular um conjunto de dados de alunos utilizando a biblioteca **Pandas**, aplicando técnicas de limpeza, transformação e análise de dados.


## 🧠 Objetivo

O script realiza uma análise exploratória simples e aplica transformações nos dados para:

* Identificar e tratar valores nulos.
* Remover registros específicos.
* Calcular pontos extras e notas finais.
* Classificar os alunos como **“Aprovado”** ou **“Reprovado”** com base na nota final.


## 🛠️ Tecnologias Utilizadas

* **Python 3**
* **Pandas**


## 📋 Etapas do Projeto

1. **Importação dos dados**

   * Leitura do dataset de alunos a partir de uma URL pública.

2. **Análise exploratória**

   * Visualização das primeiras e últimas linhas do DataFrame.
   * Verificação de dimensões, nomes de colunas e estatísticas descritivas.

3. **Tratamento de dados nulos**

   * Substituição e remoção de valores ausentes.

4. **Limpeza de registros**

   * Exclusão dos alunos “Alice” e “Carlos” da base.

5. **Cálculos e transformações**

   * Cálculo de pontos extras (40% da nota original).
   * Cálculo da nota final, limitando o valor máximo a 10.
   * Criação de uma nova coluna com a situação final do aluno.

6. **Visualização final**

   * Exibição do DataFrame atualizado com as novas colunas e resultados.



## 📈 Resultado Esperado

O script gera um DataFrame atualizado, contendo:

* Colunas adicionais com **pontos extras** e **nota final**.
* Classificação dos alunos em **“Aprovado”** ou **“Reprovado”**.


## 🧾 Licença

Este projeto foi desenvolvido para fins educacionais e de prática com a biblioteca **Pandas**.
Sinta-se à vontade para utilizar, modificar e aprimorar.

Quer que eu adicione uma parte final com o seu nome como autora (por exemplo, “Desenvolvido por Ana Elisa”) para deixar o README mais personalizado?
