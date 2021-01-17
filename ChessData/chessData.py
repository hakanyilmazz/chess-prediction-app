import csv
import chess.pgn

pgn = open("chess-game.pgn")
firstGame = chess.pgn.read_game(pgn)

with open('chess.csv', 'w', encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['ilkHamle', 'ikinciHamle', 'ucuncuHamle', 'dorduncuHamle', 'besinciHamle', 'altinciHamle', 'yedinciHamle', 'sekizinciHamle', 'dokuzuncuHamle',
                     'onuncuHamle', 'sonuc'])

while True:
    try:
        stringGameResultHeader = firstGame.headers["Result"]
    except Exception as e:
        break

    moves = list()
    for i in firstGame.variations:
        moves = str(i).split(' ')

    resultMoves = list()
    for i in range(1, len(moves)):
        if i % 3 != 0:
            resultMoves.append(moves[i])

    print(resultMoves, end="\n\n")

    gameResult = 0

    if stringGameResultHeader.find("1-0") > -1:
        gameResult = 1
    elif stringGameResultHeader.find("0-1") > -1:
        gameResult = -1
    else:
        gameResult = 0

    try:
        with open('chess.csv', mode='a', encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([resultMoves[0], resultMoves[1], resultMoves[2], resultMoves[3], resultMoves[4], resultMoves[5], resultMoves[6],
                             resultMoves[7], resultMoves[8], resultMoves[9], gameResult])
    except Exception as e:
        pass

    firstGame = chess.pgn.read_game(pgn)
