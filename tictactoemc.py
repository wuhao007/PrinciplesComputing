"""
Monte Carlo Tic-Tac-Toe Player
"""
 
import random
import poc_ttt_gui
import poc_ttt_provided as provided
 
# Constants for Monte Carlo simulator
# Change as desired
NTRIALS = 20   # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player
    
# Add your functions here.
 
def create_board():
    """
    El inicio dej juego
    """
    dimension_square_board = 3
    primer_jugador = provided.PLAYERX
    
    board = provided.TTTBoard(dimension_square_board)
    
    mc_trial(board, primer_jugador)
 
def mc_trial(board, player):
    """
    Juega aleatoriamente hasta obtener un resultado
    """
    player = player
    juego_en_progreso = None
    
    while board.get_empty_squares():
        square = random.choice(board.get_empty_squares())
        board.move(square[0], square[1], player)
        
        state = board.check_win()
        if state != juego_en_progreso:
            break
        
        player = provided.switch_player(player)
 
def mc_update_scores(scores, board, player):
    """
    Player que gano el partido.
    EMPTY     = 1
    PLAYERX = 2
    PLAYERO = 3
    """
    winner = board.check_win()
    board_dim = board.get_dim()
    
    for row in range(board_dim):
        for col in range(board_dim):
            square = board.square(row, col)
            
            if winner == provided.PLAYERX and player == provided.PLAYERX or winner == provided.PLAYERX and player == provided.PLAYERO:
                if square == provided.EMPTY:
                    scores[row][col] += 0
                elif square == provided.PLAYERX:
                    scores[row][col] += MCMATCH
                elif square == provided.PLAYERO:
                    scores[row][col] -= MCOTHER
            elif winner == provided.PLAYERO and player == provided.PLAYERX or winner == provided.PLAYERO and player == provided.PLAYERO:
                if square == provided.EMPTY:
                    scores[row][col] += 0
                elif square == provided.PLAYERX:
                    scores[row][col] -= MCMATCH
                elif square == provided.PLAYERO:
                    scores[row][col] += MCOTHER
 
def get_best_move(board, scores):
    """
    Aqui va algo
    """
    empty_squares = board.get_empty_squares()
    high_score = get_high_score_for(empty_squares, scores)
    board_dim = board.get_dim()
    lista = []
        
    for row in range(board_dim):
        for col in range(board_dim):
            
            if scores[row][col] == high_score:
                if board.square(row, col) == provided.EMPTY:
                    lista.append((row, col))
    return random.choice(lista)
 
def mc_move(board, player, trials):
    """
    Aqui va algo
    """
    scores = get_scores_grid(board.get_dim())
 
    for dummy_trial in range(trials):
        board_copy = board.clone()
        mc_trial(board_copy, player)
        mc_update_scores(scores, board_copy, player)
    return get_best_move(board, scores)
 
def get_scores_grid(dim):
    """
    Retorna un grid de tamanio n
    """
    return [ [0 for dummy_col in range(dim)] for dummy_row in range(dim)]
 
def get_high_score_for(empty_squares, scores):
    """
    Retorna el maximo score que tiene el grid scores
    """
    max_score = float("-inf")
    
    for tupla in empty_squares:
        if scores[tupla[0]][tupla[1]] >= max_score:
            max_score = scores[tupla[0]][tupla[1]]
    return max_score
 
# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.
 
# provided.play_game(mc_move, NTRIALS, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
# create_board()
 
#mc_update_scores([[0, 0, 0], [0, 0, 0], [0, 0, 0]], provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.EMPTY, provided.PLAYERX, provided.PLAYERO]]), 2)
#get_best_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), [[0, 0], [3, 0]])
#get_best_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.PLAYERX], [provided.EMPTY, provided.PLAYERO]]), [[3, 3], [0, 0]])
#get_best_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.PLAYERO, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), [[3, 2, 5], [8, 2, 8], [4, 0, 2]])
mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO, NTRIALS)
#import user35_nVhUMJnQWlTC6EY as wopr
#wopr.test_mc_trial(mc_trial)
#wopr.test_mc_update_scores(mc_update_scores)
#wopr.test_get_best_move(get_best_move)
#wopr.test_mc_move(mc_move)