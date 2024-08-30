# Reorganização da agenda dos artistas
agenda = [
    "Taylor",
    "Harry",
    "Justin",
    "Florence",
    "Gracie"
]
artista_cancelado = "Justin"
novo_artista = "Sabrina"
indice_cancelado = agenda.index(artista_cancelado)
print("O artista Justin saiu da agenda e a artista Sabrina entrou em seu lugar")
agenda.remove("Justin")
agenda.insert(indice_cancelado, novo_artista)
y = 1
print(y)
for x in agenda:
    print(y,"-",x)
    y = y + 1