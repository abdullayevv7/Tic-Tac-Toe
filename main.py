import random

def print_board(b):
    for i in range(3):
        row = [b[3*i + j] or str(3*i + j + 1) for j in range(3)]
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")

def check_win(b, mark):
    wins = [(0,1,2),(3,4,5),(6,7,8),
            (0,3,6),(1,4,7),(2,5,8),
            (0,4,8),(2,4,6)]
    return any(all(b[i]==mark for i in combo) for combo in wins)

def get_available_moves(board):
    return [i for i,v in enumerate(board) if v is None]

def minimax(board, is_maximizing):
    if check_win(board, "O"):
        return 1
    if check_win(board, "X"):
        return -1
    if all(x is not None for x in board):
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in get_available_moves(board):
            board[move] = "O"
            score = minimax(board, False)
            board[move] = None
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            board[move] = "X"
            score = minimax(board, True)
            board[move] = None
            best_score = min(score, best_score)
        return best_score

def computer_move(board, level):
    moves = get_available_moves(board)

    if level == "easy":
        return random.choice(moves)

    if level == "normal":
        if random.random() < 0.5:
            return random.choice(moves)

    if level == "hard":
        if random.random() < 0.2:
            return random.choice(moves)

    # hard va extremely hard uchun minimax
    best_score = -float("inf")
    best_move = None
    for move in moves:
        board[move] = "O"
        score = minimax(board, False)
        board[move] = None
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def play_round(player1, player2, vs_comp=False, level="easy"):
    board = [None]*9
    players = ["X","O"]
    turn = 0

    while True:
        print_board(board)
        current_mark = players[turn%2]
        current_name = player1 if current_mark=="X" else player2

        if vs_comp and current_mark=="O":
            move = computer_move(board, level)
            print(f"{player2} tanladi: {move+1}")
        else:
            try:
                move = int(input(f"{current_name}, qaysi uyaga qo'yasiz (1-9): ")) - 1
            except ValueError:
                print("1 dan 9 gacha son kiriting.")
                continue
            if not (0 <= move <= 8) or board[move] is not None:
                print("Noto'g'ri yoki band uy.")
                continue

        board[move] = current_mark

        if check_win(board, current_mark):
            print_board(board)
            print(f"{current_name} g'alaba qozondi! 🎉")
            return current_name

        if all(x is not None for x in board):
            print_board(board)
            print("Durrang!")
            return None

        turn += 1

def play():
    while True:
        mode = input("Ikkita o'yinchi (1) yoki kompyuterga qarshi (2)? [1/2]: ").strip()
        rounds_to_win = int(input("Nechta g'alabagacha o'ynaysiz?: "))

        player1 = input("1-o'yinchi ismini kiriting (X): ")

        if mode == "2":
            player2 = "Kompyuter"
            level = input("Qiyinlik darajasi (easy, normal, hard, extremely hard): ").lower()
            vs_comp = True
        else:
            player2 = input("2-o'yinchi ismini kiriting (O): ")
            level = "easy"
            vs_comp = False

        scores = {player1:0, player2:0}

        while scores[player1] < rounds_to_win and scores[player2] < rounds_to_win:
            winner = play_round(player1, player2, vs_comp, level)
            if winner:
                scores[winner] += 1

            print(f"Hisob: {player1} {scores[player1]} - {player2} {scores[player2]}")
            print("-"*20)

        print("Raund tugadi!")
        if scores[player1] > scores[player2]:
            print(f"Umumiy g'olib: {player1} 🏆")
        else:
            print(f"Umumiy g'olib: {player2} 🏆")

        again = input("Yana o'ynaysizmi? (yes/exit): ").lower()
        if again == "exit":
            print("O'yin yakunlandi.")
            break

if __name__ == "__main__":
    play()