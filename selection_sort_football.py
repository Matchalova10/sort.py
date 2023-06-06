def selection_sort_players(players):
    n = len(players)
    
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if players[j][2] > players[max_idx][2]:
                max_idx = j
        
        players[i], players[max_idx] = players[max_idx], players[i]
    
    return players

players = [
    [1, "Kylian Mbappe", "Paris Saint Germain", 40],
    [2, "Victor Osimhen", "Napoli", 28],
    [3, "Robert Lewandowski", "Barcelona", 33],
    [4, "Erling Haaland", None, 52],
    [5, "Christopher Nkunku", "RB Leipzig", 22]
]

sorted_players = selection_sort_players(players)
print("Daftar pemain setelah diurutkan berdasarkan jumlah gol (descending):")
for player in sorted_players:
    print(f"No. {player[0]} | Nama Pemain: {player[1]} | Klub: {player[2]} | Jumlah Gol: {player[3]}")
