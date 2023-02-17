
class Board:
     def __init__(self):
          # board is a list of cells that are represented 
          # by strings (" ", "O", and "X")
          # initially it is made of empty cells represented 
          # by " " strings
          self.sign = " "
          self.size = 3
          self.board = list(self.sign * self.size**2)
          self.labels = self._get_labels()
          # the winner's sign O or X
          self.winner = ""


     def _get_labels(self):
          labels = []
          n = self.size
          for char in range(65, 65+n):
               for i in range(1, 1+n):
                    labels.append(chr(char) + str(i))
          return labels

     def get_size(self):
          return self.size

     def get_winner(self):
          # return the winner's sign O or X (an instance winner)
          return self.winner

     def get_sign(self, index):
          # return the sign O or X at the index
          return self.board[index]

     def get_index(self, cell):
          if (cell[0] == 'A'):
               if (cell[1] == '1'):
                    index = 0
               elif (cell[1] == '2'):
                    index = 3
               elif (cell[1] == '3'):
                    index = 6
          elif (cell[0] == 'B'):
               if (cell[1] == '1'):
                    index = 1
               elif (cell[1] == '2'):
                    index = 4
               elif (cell[1] == '3'):
                    index = 7
          elif (cell[0] == 'C'):
               if (cell[1] == '1'):
                    index = 2
               elif (cell[1] == '2'):
                    index = 5
               elif (cell[1] == '3'):
                    index = 8
          return index
     
     def returnCell(self, index):
          return chr(ord('A') + index // 3) + str((index % 3) + 1)

     def set(self, cell, sign):
          # mark the cell on the board with the sign X or O
          # if the cell ends with 1, 2, or 3, it is in the first row
          # if the cell ends with 4, 5, or 6, it is in the second row
          # if the cell ends with 7, 8, or 9, it is in the third row
          # if the cell starts with A, it is in the first column
          # if the cell starts with B, it is in the second column
          # if the cell starts with C, it is in the third column
          self.board[self.get_index(cell)] = sign

     def isempty(self, cell):
          # return True if the cell is empty (not marked with X or O)
          # otherwise return False
          if self.board[self.get_index(cell)] == " ":
               return True
          else:
               return False

     def isemptyIndex(self, index):
          if self.board[index] == " ":
               return True
          else:
               return False

     def isdone(self):
          # you need to implement 8 other conditions (1 diagonal, 3 rows, 3 cols, 1 tie) 
          done = False
          self.winner = '' 
          if self.board[0]==self.board[4]==self.board[8]!=' ':
               done = True
               self.winner = self.board[0]
          elif self.board[2]==self.board[4]==self.board[6]!=' ':
               done = True    
               self.winner = self.board[2]
          elif self.board[0]==self.board[1]==self.board[2]!=' ':
               done = True
               self.winner = self.board[0]
          elif self.board[3]==self.board[4]==self.board[5]!=' ':
               done = True
               self.winner = self.board[3]
          elif self.board[6]==self.board[7]==self.board[8]!= ' ':
               done = True
               self.winner = self.board[6]
          elif self.board[0]==self.board[3]==self.board[6]!=' ':
               done = True
               self.winner = self.board[0]
          elif self.board[1]==self.board[4]==self.board[7]!=' ':
               done = True
               self.winner = self.board[1]
          elif self.board[2]==self.board[5]==self.board[8]!=' ':
               done = True
               self.winner = self.board[2]
          elif ' ' not in self.board:
               done = True
               self.winner = 'Tie'
          return done

     def show(self):
          # draw the board
          # need to complete the code
          print('   A   B   C') 
          print(' +---+---+---+')
          print('1| {} | {} | {} |'.format(self.board[0], self.board[1], self.board[2]))
          print(' +---+---+---+')
          print("2| {} | {} | {} |".format(self.board[3], self.board[4], self.board[5]))
          print(" +---+---+---+")
          print("3| {} | {} | {} |".format(self.board[6], self.board[7], self.board[8]))
          print(" +---+---+---+")


if __name__ == '__main__':
     board = Board()
     board.set('C2', 'X')
     print(board.isempty(cell='C2'))
     board.show()
     

               
