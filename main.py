import random

def print_board(b):
    for i in range(3):
        row = [b[3*i + j] or str(3*i + j + 1) for j in range(3)]
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")

def check_win(b, mark):
    wins = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    return any(all(b[i]==mark for i in combo) for combo in wins)

def play():
    board = [None]*9
    players = ["X","O"]
    mode = input("Ikkiga-ikkiga oynash (1) yoki kompyuterga qarshi (2)? [1/2]: ").strip()
    vs_comp = mode == "2"
    turn = 0
    while True:
        print_board(board)
        current = players[turn%2]
        if vs_comp and current=="O":
            move = random.choice([i for i,v in enumerate(board) if v is None])
            print(f"Komp tanladi: {move+1}")
        else:
            try:
                move = int(input(f"O'yinchi {current}, qaysi uyaga qo'yasiz (1-9): ")) - 1
            except ValueError:
                print("1 dan 9 gacha son kiriting.")
                continue
            if not (0 <= move <= 8) or board[move] is not None:
                print("Noto'g'ri yoki band uy. Qaytadan urinib ko'ring.")
                continue

        board[move] = current
        if check_win(board, current):
            print_board(board)
            print(f"O'yinchi {current} g'alaba qozondi! 🎉")
            break
        if all(x is not None for x in board):
            print_board(board)
            print("Durrang!")
            break
        turn += 1

if __name__ == "__main__":
    play()
