import streamlit as st
import copy

PLAYER = "X"
AI = "O"

def check_winner(board):
    wins = [(0,1,2), (3,4,5), (6,7,8),  # rows
            (0,3,6), (1,4,7), (2,5,8),  # columns
            (0,4,8), (2,4,6)]           # diagonals
    for a,b,c in wins:
        if board[a] == board[b] == board[c] != "":
            return board[a]
    if "" not in board:
        return "Draw"
    return None

def minimax(board, is_maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == PLAYER:
        return -1
    elif winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = AI
                score = minimax(board, False)
                board[i] = ""
                best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(9):
            if board[i] == "":
                board[i] = PLAYER
                score = minimax(board, True)
                board[i] = ""
                best_score = min(best_score, score)
        return best_score

def best_move(board):
    best_score = -float('inf')
    move = None
    for i in range(9):
        if board[i] == "":
            board[i] = AI
            score = minimax(board, False)
            board[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move