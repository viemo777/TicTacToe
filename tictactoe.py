lst = [None, None, None, None, None, None, None, None, None]

class TicTacToe():
    def __init__(self):
        pass

    def seticon(self, lst):
        print(lst[0:3])
        print(lst[3:6])
        print(lst[6:9])

    def checkstatus(self, lst):

        haswinner = False

        if (lst[0] == lst[1] == lst[2] and lst[2] != None) or (lst[3] == lst[4] == lst[5] and lst[5] != None) or (lst[6] == lst[7] == lst[7] and lst[7] != None) or \
                (lst[0] == lst[3] == lst[6] and lst[6] != None) or (lst[1] == lst[4] == lst[7] and lst[7] != None) or (lst[2] == lst[5] == lst[8] and lst[8] != None) or \
                (lst[0] == lst[4] == lst[8] and lst[8] != None) or (lst[3] == lst[4] == lst[6] and lst[6] != None):
            haswinner = True

        return haswinner

ttt = TicTacToe()

nextcross = True
cur_cell = 0


while int(cur_cell) >=0 and int(cur_cell) <=8 and (None in lst):

    cur_cell = int(input(f'Player {"X" if nextcross else "0"}, indicate number of cell from 0 to 8: '))
    if (lst[cur_cell] != None):
        continue

    lst[cur_cell] = 'X' if nextcross else '0'


    ttt.seticon(lst)

    if ttt.checkstatus(lst):
        print(f'Player {"X" if nextcross else "0"} is winner')
        break

    nextcross = not nextcross

print('Game over')