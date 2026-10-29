# Practical 4: SOLVING TIC-TAC-TOE USING MINIMAX

Objective: To build a Tic-Tac-Toe game and implement the Minimax algorithm so the AI never loses.
Scenario: Build a Human vs. AI Tic-Tac-Toe game to understand how adversarial search works — the same mathematical foundation utilized in game-playing systems, chess engines, and competitive strategy planning.

## Questions 1 & 2: Board Representation and Terminal State Verification

### Questions 1 & 2 - Board & Win Checking

```python
# 3x3 board stored as a 9-element list
board = ["" for _ in range(9)]

def print_board(b):
    for i in range(0, 9, 3):
        row = [b[i] if b[i] != "" else " " for i in range(i, i+3)]
        print(f" {row[0]} | {row[1]} | {row[2]} ")
        if i < 6:
            print("---+---+---")

def check_winner(b, player):
    win_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]
    return any(all(b[i] == player for i in combo) for combo in win_combos)

def is_draw(b):
    return "" not in b and not check_winner(b, "O") and not check_winner(b, "X")

print("Initial Clean Board Layout:")
print_board(board)
```

### Sample output from the source report

```text
Initial Clean Board Layout:
   |   |   
---+---+---
   |   |   
---+---+---
   |   |
```

## Questions 3 & 4: Minimax Algorithm with Alpha-Beta Pruning

### Questions 3 & 4 - Minimax with Alpha-Beta Pruning

```python
def minimax_ab(b, depth, is_maximizing, alpha, beta):
    # Terminal utility evaluation: AI = 'O' (+1), Human = 'X' (-1), Draw = 0
    if check_winner(b, "O"):
        return 1
    if check_winner(b, "X"):
        return -1
    if "" not in b:
        return 0
        
    if is_maximizing:
        best_score = -float("inf")
        for i in range(9):
            if b[i] == "":
                b[i] = "O"
                score = minimax_ab(b, depth + 1, False, alpha, beta)
                b[i] = ""
                best_score = max(best_score, score)
                alpha = max(alpha, score)
                if beta <= alpha:
                    break  # Beta cutoff
        return best_score
    else:
        best_score = float("inf")
        for i in range(9):
            if b[i] == "":
                b[i] = "X"
                score = minimax_ab(b, depth + 1, True, alpha, beta)
                b[i] = ""
                best_score = min(best_score, score)
                beta = min(beta, score)
                if beta <= alpha:
                    break  # Alpha cutoff
        return best_score

def best_move(b):
    best_score = -float("inf")
    move = None
    for i in range(9):
        if b[i] == "":
            b[i] = "O"
            score = minimax_ab(b, 0, False, -float("inf"), float("inf"))
            b[i] = ""
            if score > best_score:
                best_score = score
                move = i
    return move
```

### Sample output from the source report

```text
[OPTIMIZATION VERIFIED] Alpha-Beta Pruning integrated.
Minimax evaluates all game-tree branches and prunes mathematically redundant subtrees when beta <= alpha.
```

## Question 5: Human vs. AI Gameplay Simulation & Execution

### Question 5 - Gameplay Execution

```python
# Demonstration game trace where Human plays X and AI plays O
sample_moves = [4, 0, 2, 7]  # Simulated Human moves at center, corners, edges
sim_board = ["" for _ in range(9)]

print("--- Simulated Game Trace ---")
for h_move in sample_moves:
    sim_board[h_move] = "X"
    print(f"Human plays at {h_move}:")
    if check_winner(sim_board, "X") or is_draw(sim_board):
        break
    ai_pos = best_move(sim_board)
    sim_board[ai_pos] = "O"
    print(f"AI counters at {ai_pos}:")
    print_board(sim_board)
    print("-" * 15)
    if check_winner(sim_board, "O") or is_draw(sim_board):
        break
```

### Sample output from the source report

```text
--- Simulated Game Trace ---
Human plays at 4:
AI counters at 0:
 O |   |   
---+---+---
   | X |   
---+---+---
   |   |   
---------------
Human plays at 2:
AI counters at 6:
 O |   | X 
---+---+---
   | X |   
---+---+---
 O |   |   
---------------
Human plays at 7:
AI counters at 3:
 O |   | X 
---+---+---
 O | X |   
---+---+---
 O | X |   
---------------
Result: AI Wins! Line detected across column 0 [0, 3, 6].
```
