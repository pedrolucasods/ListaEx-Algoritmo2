# 2 - Um serviço de streaming tem seu catálogo representado por uma lista de tuplas
# (titulo_filme, ano_lancamento, genero, avaliacao_usuarios). Você também receberá
# como parâmetro um genero_alvo (string) e uma nota_corte (float).
# Você deve extrair dados com base em múltiplos parâmetros de entrada e encontrar o
# "menor valor" (mais antigo) dentro de um subconjunto específico.
# Retorno Exigido: Uma lista apenas com os títulos dos filmes que batem com o gênero
# alvo e possuem nota igual ou superior ao corte, e uma tupla com o (titulo_filme,
# ano_lancamento) do filme mais antigo dessa lista filtrada.
# Na Main: Construa uma lista estática com pelo menos 4 filmes misturando gêneros e
# notas. Defina variáveis para o seu gênero alvo e sua nota de corte. Invoque a função e
# imprima a lista final de filmes aprovados, seguida de uma mensagem informando qual é
# o filme mais antigo dentre os que foram filtrados.


class Filmes:
    def __init__(self,catalago):
        self.__catalago = catalago

    def ver_todos(self):
        return self.__catalago

    def buscar_por_genero_e_corte(self,genero,corte):
        filmes = self.__filtro_por_genero(genero,corte)
        mais_antigos = self.__mais_antigo(filmes)
        dados = {
            "Filmes":filmes if len(filmes) else "Filme Não Encontrado!",
            "Mais Antigo":mais_antigos if len(filmes) else "Filme Não Encontrado!"
        }

        return dados 

    def __filtro_por_genero(self,genero,corte):
        busca_filme = []
        catalogo = self.__catalago
        for filme in catalogo:
            if(filme[2] == genero and (filme[3]>=corte)):
                busca_filme.append(filme[0])
        return busca_filme

    def __mais_antigo(self,lista):
        mais_antigo = []
        if(len(lista)):
            ano_mais_antigo = lista[0]
            for filme in self.__catalago:
                if(filme[0] == ano_mais_antigo):
                    ano_mais_antigo = filme[1]
                if(filme in lista and filme[0]!=lista[0]):
                    if(filme[1]<ano_mais_antigo):
                        ano_mais_antigo = filme[1]

            for filme in self.__catalago:
                if filme[1] == ano_mais_antigo:
                    mais_antigo.append((filme[0],filme[1]))
        return mais_antigo


catalogo = [
    ("O Poderoso Chefão", 1972, "Drama", 9.2),
    ("Toy Story", 1995, "Animação", 8.3),
    ("Matrix", 1999, "Ficção Científica", 8.7),
    ("A Origem", 2010, "Ficção Científica", 8.8),
    ("Interestelar", 2014, "Ficção Científica", 8.6),
    ("Pulp Fiction: Tempo de Violência", 1994, "Crime", 8.9),
    ("O Senhor dos Anéis: A Sociedade do Anel", 2001, "Fantasia", 8.8),
    ("Clube da Luta", 1999, "Drama", 8.8),
    ("Forrest Gump: O Contador de Histórias", 1994, "Drama", 8.8),
    ("Batman: O Cavaleiro das Trevas", 2008, "Ação", 9.0),
    ("A Viagem de Chihiro", 2001, "Animação", 8.6),
    ("Cidade de Deus", 2002, "Crime", 8.6),
    ("Gladiador", 2000, "Ação", 8.5),
    ("Os Vingadores", 2012, "Ação", 8.0),
    ("Parasita", 2019, "Thriller", 8.5),
    ("O Rei Leão", 1994, "Animação", 8.5),
    ("De Volta para o Futuro", 1985, "Ficção Científica", 8.5),
    ("Star Wars: Episódio V - O Império Contra-Ataca", 1980, "Ficção Científica", 8.7),
    ("O Poderoso Chefão: Parte II", 1974, "Drama", 9.0),
    ("O Resgate do Soldado Ryan", 1998, "Guerra", 8.6),
    ("À Espera de um Milagre", 1999, "Drama", 8.6),
    ("Os Bons Companheiros", 1990, "Crime", 8.7),
    ("Whiplash: Em Busca da Perfeição", 2014, "Drama", 8.5),
    ("Bastardos Inglórios", 2009, "Aventura", 8.3),
    ("Coringa", 2019, "Drama", 8.4),
    ("Homem-Aranha: No Aranhaverso", 2018, "Animação", 8.4),
    ("Divertida Mente", 2015, "Animação", 8.1),
    ("WALL-E", 2008, "Animação", 8.4),
    ("O Silêncio dos Inocentes", 1991, "Thriller", 8.6),
    ("Seven: Os Sete Crimes Capitais", 1995, "Crime", 8.6)
]


cinema_1 = Filmes(catalogo)
filmes_especifico = cinema_1.buscar_por_genero_e_corte("Aventura",8)

for key,value in filmes_especifico.items():
    print(f"{key}:{value}")
