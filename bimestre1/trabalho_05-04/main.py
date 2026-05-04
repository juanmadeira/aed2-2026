from players import Players

print(f"\n=== POVOAMENTO INICIAL ===\n")
players = Players()
for i in range(0, 10): # zero-based
    players.insertPlayer(i, f"Jogador {i + 1}")
    print(f"Inserindo Jogador {i + 1}")

players.printPlayers()
print(f"Head: {players.head}, Tail: {players.tail}, Total: {players.getNumberOfPlayers()}")


print(f"\n\n=== TESTE DE GERAÇÃO DE ESPAÇO ===\n")
for i in range(3):
    print(f"Removendo jogador da posição 0")
    players.removePlayer(0)
    players.printPlayers()
    print(f"Head: {players.head}, Tail: {players.tail}, Total: {players.getNumberOfPlayers()}\n")


print(f"\n\n=== TESTE DE CIRCULARIDADE ===\n")
print("Inserindo Jogador A na última posição...")
players.insertPlayer(players.getNumberOfPlayers(), "Jogador A")
players.printPlayers()
print(f"Head: {players.head}, Tail: {players.tail}, Total: {players.getNumberOfPlayers()}")


print(f"\n\n=== INSERÇÃO NO MEIO ===\n")
print(f"Lista \"quebrada\": Head: {players.head}, Tail: {players.tail}")

node_meio = players.getNumberOfPlayers() // 2 # pega meio da lista

print(f"\nInserindo Jogador X na posição do meio ({node_meio})...")
players.insertPlayer(node_meio, "Jogador X")
players.printPlayers()
print(f"Head: {players.head}, Tail: {players.tail}, Total: {players.getNumberOfPlayers()}\n")