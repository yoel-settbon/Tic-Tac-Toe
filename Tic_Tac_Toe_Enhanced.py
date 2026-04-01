"""
Tic-Tac-Toe Enhanced
====================
Features:
  - Pygame graphical window with a drawn grid and animated X/O symbols
  - Menu screen: Player vs Player  or  Player vs AI
  - AI difficulty: Easy (random moves) or Hard (minimax – unbeatable)
  - Highlighted winning line
  - Persistent score counter
  - Play-again / back-to-menu button
"""

import sys
import math
import random
import pygame

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
WIDTH, HEIGHT = 600, 700          # window dimensions
BOARD_SIZE = 600                  # square board area
CELL = BOARD_SIZE // 3            # 200 px per cell

LINE_W = 8                        # grid line thickness
CIRCLE_R = 70                     # O radius
CIRCLE_W = 14                     # O stroke width
CROSS_W = 18                      # X stroke width
CROSS_PAD = 45                    # padding inside cell for X
WIN_LINE_W = 12                   # winning-line thickness

# Colours
C_BG         = (28,  170, 156)
C_GRID       = (18,  130, 120)
C_O          = (239, 231, 200)
C_X          = ( 66,  66,  66)
C_WIN_LINE   = (230,  60,  60)
C_PANEL      = ( 20, 140, 128)
C_TEXT       = (255, 255, 255)
C_BTN        = ( 23, 145, 135)
C_BTN_HOVER  = ( 12,  90,  82)
C_BTN_SHADOW = ( 10,  80,  73)

FPS = 60

# ---------------------------------------------------------------------------
# State
# ---------------------------------------------------------------------------
board        = [" "] * 9
current      = "X"                # X always starts
game_over    = False
winner       = None               # "X", "O", or "draw"
winning_combo = None              # tuple of 3 indices

score        = {"X": 0, "O": 0, "draw": 0}

# game mode / difficulty set from menu
mode       = None   # "pvp" | "ai"
difficulty = None   # "easy" | "hard"

# ---------------------------------------------------------------------------
# Pygame initialisation
# ---------------------------------------------------------------------------
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe Enhanced")
clock = pygame.time.Clock()

_FONT_LIST = ["segoeui", "arial", "helvetica", "dejavusans", None]

def _font(size, bold=False):
    for name in _FONT_LIST:
        try:
            f = pygame.font.SysFont(name, size, bold=bold)
            if f is not None:
                return f
        except Exception:
            continue
    return pygame.font.Font(None, size)

font_lg   = _font(52, bold=True)
font_md   = _font(34, bold=True)
font_sm   = _font(24)
font_tiny = _font(20)


# ===========================================================================
# Helper utilities
# ===========================================================================

def check_winner(b):
    """Return (winner_symbol, winning_indices) or (None, None)."""
    lines = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),   # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),   # cols
        (0, 4, 8), (2, 4, 6),              # diagonals
    ]
    for a, b_, c in lines:
        if b[a] != " " and b[a] == b[b_] == b[c]:
            return b[a], (a, b_, c)
    return None, None


def is_full(b):
    return " " not in b


# ---------------------------------------------------------------------------
# Minimax AI
# ---------------------------------------------------------------------------

def minimax(b, is_maximising):
    w, _ = check_winner(b)
    if w == "O":
        return 1
    if w == "X":
        return -1
    if is_full(b):
        return 0

    if is_maximising:
        best = -math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "O"
                best = max(best, minimax(b, False))
                b[i] = " "
        return best
    else:
        best = math.inf
        for i in range(9):
            if b[i] == " ":
                b[i] = "X"
                best = min(best, minimax(b, True))
                b[i] = " "
        return best


def ai_best_move():
    """Return the index of the best move for 'O' using minimax."""
    best_score = -math.inf
    best_idx   = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            s = minimax(board, False)
            board[i] = " "
            if s > best_score:
                best_score = s
                best_idx   = i
    return best_idx


def ai_random_move():
    """Return a random empty cell index."""
    empties = [i for i, v in enumerate(board) if v == " "]
    return random.choice(empties) if empties else None


# ===========================================================================
# Drawing helpers
# ===========================================================================

def cell_center(idx):
    col = idx % 3
    row = idx // 3
    return (col * CELL + CELL // 2, row * CELL + CELL // 2)


def draw_grid():
    for i in range(1, 3):
        # vertical lines
        pygame.draw.line(screen, C_GRID,
                         (i * CELL, 0), (i * CELL, BOARD_SIZE), LINE_W)
        # horizontal lines
        pygame.draw.line(screen, C_GRID,
                         (0, i * CELL), (BOARD_SIZE, i * CELL), LINE_W)


def draw_symbols():
    for idx, val in enumerate(board):
        cx, cy = cell_center(idx)
        if val == "O":
            pygame.draw.circle(screen, C_O, (cx, cy), CIRCLE_R, CIRCLE_W)
        elif val == "X":
            x0 = cx - CELL // 2 + CROSS_PAD
            y0 = cy - CELL // 2 + CROSS_PAD
            x1 = cx + CELL // 2 - CROSS_PAD
            y1 = cy + CELL // 2 - CROSS_PAD
            pygame.draw.line(screen, C_X, (x0, y0), (x1, y1), CROSS_W)
            pygame.draw.line(screen, C_X, (x1, y0), (x0, y1), CROSS_W)


def draw_winning_line(combo):
    if combo is None:
        return
    a, _, c = combo
    start = cell_center(a)
    end   = cell_center(c)
    pygame.draw.line(screen, C_WIN_LINE, start, end, WIN_LINE_W)


def draw_panel():
    """Draw the bottom panel (score + status)."""
    panel_rect = pygame.Rect(0, BOARD_SIZE, WIDTH, HEIGHT - BOARD_SIZE)
    pygame.draw.rect(screen, C_PANEL, panel_rect)

    # Scores
    score_txt = font_sm.render(
        f"X: {score['X']}   Draws: {score['draw']}   O: {score['O']}", True, C_TEXT)
    screen.blit(score_txt,
                (WIDTH // 2 - score_txt.get_width() // 2, BOARD_SIZE + 8))

    # Status / turn
    if game_over:
        if winner == "draw":
            msg = "It's a draw!"
        else:
            label = "AI" if (mode == "ai" and winner == "O") else f"Player {winner}"
            msg = f"{label} wins!"
        status = font_md.render(msg, True, C_WIN_LINE)
    else:
        if mode == "ai" and current == "O":
            msg = "AI is thinking…"
        else:
            msg = f"Player {current}'s turn"
        status = font_md.render(msg, True, C_TEXT)

    screen.blit(status, (WIDTH // 2 - status.get_width() // 2, BOARD_SIZE + 38))

    # Buttons
    if game_over:
        draw_button(btn_again,  "Play Again",    font_sm)
        draw_button(btn_menu,   "Main Menu",     font_sm)
    else:
        draw_button(btn_menu,   "Main Menu",     font_sm)


# ---------------------------------------------------------------------------
# Button helpers
# ---------------------------------------------------------------------------

btn_again = pygame.Rect(60,  BOARD_SIZE + 75, 210, 44)
btn_menu  = pygame.Rect(330, BOARD_SIZE + 75, 210, 44)
btn_menu_only = pygame.Rect(195, BOARD_SIZE + 75, 210, 44)

_hovered_btn = None   # tracked each frame


def draw_button(rect, label, fnt, colour=C_BTN, hover_colour=C_BTN_HOVER):
    global _hovered_btn
    mx, my = pygame.mouse.get_pos()
    is_hov = rect.collidepoint(mx, my)
    c = hover_colour if is_hov else colour
    # shadow
    shadow = rect.move(3, 3)
    pygame.draw.rect(screen, C_BTN_SHADOW, shadow, border_radius=8)
    pygame.draw.rect(screen, c, rect, border_radius=8)
    txt = fnt.render(label, True, C_TEXT)
    screen.blit(txt, (rect.centerx - txt.get_width() // 2,
                      rect.centery - txt.get_height() // 2))


# ===========================================================================
# Menu screen
# ===========================================================================

def draw_menu():
    screen.fill(C_BG)
    title = font_lg.render("Tic-Tac-Toe", True, C_TEXT)
    screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 60))

    sub = font_sm.render("Choose a game mode:", True, C_TEXT)
    screen.blit(sub, (WIDTH // 2 - sub.get_width() // 2, 160))

    draw_button(btn_pvp, "Player vs Player", font_md)
    draw_button(btn_ai_easy, "vs AI  –  Easy", font_md)
    draw_button(btn_ai_hard, "vs AI  –  Hard", font_md)

    hint = font_tiny.render("Hard mode uses minimax (unbeatable AI)", True, C_TEXT)
    screen.blit(hint, (WIDTH // 2 - hint.get_width() // 2, 520))


btn_pvp     = pygame.Rect(150, 220, 300, 60)
btn_ai_easy = pygame.Rect(150, 310, 300, 60)
btn_ai_hard = pygame.Rect(150, 400, 300, 60)


def handle_menu_click(pos):
    global mode, difficulty
    if btn_pvp.collidepoint(pos):
        mode, difficulty = "pvp", None
        return True
    if btn_ai_easy.collidepoint(pos):
        mode, difficulty = "ai", "easy"
        return True
    if btn_ai_hard.collidepoint(pos):
        mode, difficulty = "ai", "hard"
        return True
    return False


# ===========================================================================
# Game state management
# ===========================================================================

def reset_board():
    global board, current, game_over, winner, winning_combo
    board         = [" "] * 9
    current       = "X"
    game_over     = False
    winner        = None
    winning_combo = None


def apply_move(idx):
    """Place the current player's mark and check end conditions."""
    global current, game_over, winner, winning_combo
    if board[idx] != " " or game_over:
        return
    board[idx] = current
    w, combo = check_winner(board)
    if w:
        winner        = w
        winning_combo = combo
        game_over     = True
        score[w]     += 1
    elif is_full(board):
        winner    = "draw"
        game_over = True
        score["draw"] += 1
    else:
        current = "O" if current == "X" else "X"


def pos_to_cell(pos):
    """Convert a mouse position to board index, or None if outside the board."""
    x, y = pos
    if x < 0 or x >= BOARD_SIZE or y < 0 or y >= BOARD_SIZE:
        return None
    return (y // CELL) * 3 + (x // CELL)


# ===========================================================================
# Main loop
# ===========================================================================

def main():
    global mode, difficulty

    in_menu = True
    reset_board()

    while True:
        clock.tick(FPS)
        mx, my = pygame.mouse.get_pos()

        # ----------------------------------------------------------------
        # Event handling
        # ----------------------------------------------------------------
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if in_menu:
                    if handle_menu_click(event.pos):
                        reset_board()
                        in_menu = False
                else:
                    # "Main Menu" button: btn_menu when game_over (right slot),
                    # btn_menu_only when game is still running (centred slot).
                    menu_btn = btn_menu if game_over else btn_menu_only
                    if menu_btn.collidepoint(event.pos):
                        in_menu = True
                        reset_board()
                        continue

                    # Play Again button
                    if game_over and btn_again.collidepoint(event.pos):
                        reset_board()
                        continue

                    # Board click
                    if not game_over and not (mode == "ai" and current == "O"):
                        idx = pos_to_cell(event.pos)
                        if idx is not None:
                            apply_move(idx)

        # ----------------------------------------------------------------
        # AI move (after human turn)
        # ----------------------------------------------------------------
        if not in_menu and mode == "ai" and current == "O" and not game_over:
            pygame.time.delay(300)   # brief pause so it feels more natural
            idx = ai_best_move() if difficulty == "hard" else ai_random_move()
            if idx is not None:
                apply_move(idx)

        # ----------------------------------------------------------------
        # Drawing
        # ----------------------------------------------------------------
        if in_menu:
            draw_menu()
        else:
            screen.fill(C_BG)
            draw_grid()
            draw_symbols()
            if game_over and winning_combo:
                draw_winning_line(winning_combo)
            draw_panel()

            # Render single "Main Menu" button when game is not over
            if not game_over:
                draw_button(btn_menu_only, "Main Menu", font_sm)

        pygame.display.flip()


if __name__ == "__main__":
    main()
