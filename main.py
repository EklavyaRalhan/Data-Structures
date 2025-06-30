theboard = {
    '7':' ', '8':' ', '9':' ',
    '4':' ', '5':' ', '6':' ',
    '1':' ', '2':' ', '3':' '
}

boardkeys = list(theboard.keys())

def printboard(board):
    print(board['7'] + '|' + board['8']+ '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5']+ '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2']+ '|' + board['3'])

def game():
    turn = 'x'
    count = 0


    for _ in range(9):
        printboard(theboard)
        print("Your turn" + turn + "Choose a postion between 1-9")

        move = input("Move: ")

        if theboard.get(move) == ' ':
            theboard[move] = turn
            count+=1

        else:
            print("Spot occupied, try again")
            continue

        if count >= 5:
            wins = [
                ('7','8','9'), ('4','5','6'), ('1','2','3'), ('1','4','7'),
                ('2','5','8'), ('3','6','9'), ('1','5','9'), ('3','5','7')
            ]

            for a,b,c in wins:
             if theboard[a] == theboard[b] == theboard[c] != ' ':
                printboard(theboard)
                print("Game over")
                print(turn, "Wins the game")
                return

        if count == 9:
            printboard(theboard)
            print("Game over")
            print("It's a tie!")
            return
            
        turn = 'O' if turn == 'x' else 'x'
    restart = input("Do you want to play again, y/n")
    if restart.lower() == 'y':
        for k in boardkeys:
            theboard[k] = ' '
        game()


if __name__ == "__main__":
    game()


