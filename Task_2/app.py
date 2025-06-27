import streamlit as st
from minimax_tictactoe import best_move, check_winner, PLAYER, AI

if "board" not in st.session_state:
    st.session_state.board = [""] * 9
    st.session_state.turn = PLAYER
    st.session_state.winner = None

st.title("Tic Tac Toe")
board = st.session_state.board

cols = st.columns(3)
for i in range(9):
    if board[i] == "":
        if cols[i % 3].button(" ", key=i):
            if st.session_state.turn == PLAYER and not st.session_state.winner:
                board[i] = PLAYER
                winner = check_winner(board)
                if winner:
                    st.session_state.winner = winner
                else:
                    st.session_state.turn = AI
    else:
        cols[i % 3].write(f"**{board[i]}**")

if st.session_state.turn == AI and not st.session_state.winner:
    ai_move = best_move(board)
    if ai_move is not None:
        board[ai_move] = AI
    winner = check_winner(board)
    if winner:
        st.session_state.winner = winner
    st.session_state.turn = PLAYER

if st.session_state.winner:
    st.success(f"Game Over! Winner is: {st.session_state.winner}")
    if st.button("Restart"):
        st.session_state.board = [""] * 9
        st.session_state.turn = PLAYER
        st.session_state.winner = None