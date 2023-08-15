import pandas as pd

filmes = [
    {"titulo": "O Senhor dos Anéis", "ano": 2001, "avaliacao": 8.8},
    {"titulo": "Matrix", "ano": 1999, "avaliacao": 9.3},
    {"titulo": "Interestelar", "ano": 2014, "avaliacao": 8.6}
]

df = pd.DataFrame.from_dict(filmes)
media = df['avaliacao'].mean()
maior_avaliacao = df['avaliacao'].max()
menor_avaliacao = df['avaliacao'].min()
filme_maior_avaliado = df.loc[(df['avaliacao']==maior_avaliacao), ['titulo','avaliacao']] #localiza título do filme maior avaliado
ano_menor_avaliacao = df.loc[(df['avaliacao']==menor_avaliacao), ['ano','avaliacao']] #localiza ano do filme menor avaliado
print("Média das avaliações dos filmes: " + str(media))
print("Título do filme com a maior avaliação: ")
print(filme_maior_avaliado)
print("Ano de lançamento do filme com a menor avaliação: ")
print(ano_menor_avaliacao)

df.to_csv('filmes.csv', index=False) #salva em arquivo csv