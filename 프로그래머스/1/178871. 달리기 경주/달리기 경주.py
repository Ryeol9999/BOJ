def solution(players, callings):
    player_map = {name: i for i, name in enumerate(players)}
    
    for who in callings:
        idx = player_map[who]
        
        front_player = players[idx - 1]
        
        players[idx - 1], players[idx] = players[idx], players[idx - 1]
        
        player_map[who] = idx - 1
        player_map[front_player] = idx
        
    return players