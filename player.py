
import random
class Player:
      def __init__(self, name, sign):
            self.name = name  # player's name
            self.sign = sign  # player's sign O or X
      def get_sign(self):
            # return an instance sign
            return self.sign
      def get_name(self):
            # return an instance name
            return self.name

      def choose(self, board):
            # prompt the user to choose a cell
            # if the user enters a valid string and the cell on the board is empty, update the board
            # otherwise print a message that the input is wrong and rewrite the prompt
            # use the methods board.isempty(cell), and board.set(cell, sign)
            valid_choices = board._get_labels()
            while True: 
                  cell = input(f'{self.name}, {self.sign}: Enter a cell [A-C][1-3]:').upper()
                  if cell in valid_choices:
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              break
                        else:
                              print('The cell is not empty. Choose another cell.')
                  else:
                        print('Invalid input. Try again.')




class AI(Player):
      def __init__(self, name, sign, board):
            super().__init__(name, sign)
            self.board = board

      def choose(self, board):
            # choose a cell on the board
            # if the cell is empty, update the board
            # otherwise choose another cell
            # use the methods board.isempty(cell), and board.set(cell, sign)
            random_cell = random.choice(board._get_labels())
            if board.isempty(random_cell):
                  board.set(random_cell, self.sign)
            else:
                  self.choose(board)

class SmartAI(AI):
      #have not finished this class yet
      def __init__(self, name, sign, board):
            super().__init__(name, sign, board)

      def opponentSign(self):
            if self.sign == 'X':
                  return 'O'
            else:
                  return 'X'


      def choose(self, board):
            # choose a cell on the board
            # if the cell is empty, update the board
            # otherwise choose another cell
            # use the methods board.isempty(cell), and board.set(cell, sign)


            for cell in board._get_labels():
                  index = board.get_index(cell)
                  if board.isempty(cell):
                        if(self.check(board, index)):
                              board.set(cell, self.sign)
                              return

            #add cells to the board on the corners
            corners = [0, 2, 6, 8]
            for corner in corners:
                  if board.isemptyIndex(corner):
                        board.set(board.returnCell(corner), self.sign)                        
                        return

            random_cell = random.choice(board._get_labels())
            board.set(random_cell, self.sign)



class MiniMaxAI(AI):
      def __init__(self, name, sign, board):
            super().__init__(name, sign, board)

      def returnOpponentSign(self):
            if self.sign == 'X':
                  return 'O'
            else:
                  return 'X'
      

      def bestMove(self, board, turn):
            bestScore = float('-inf')
            move = ''
            for cell in board._get_labels():
                  if board.isempty(cell):
                        board.set(cell, self.sign)
                        score = self.minimax(turn, board)
                        board.set(cell, ' ')
                        if score > bestScore:
                              bestScore = score
                              move = cell
            return move

      def minimax(self, turn, board):
            if board.isdone():
                  if board.get_winner() == self.sign:
                        return 1
                  elif board.get_winner() == self.returnOpponentSign():
                        return -1
                  else:
                        return 0
            if turn:
                  bestScore = float('-inf')
                  for cell in board._get_labels():
                        if board.isempty(cell):
                              board.set(cell, self.sign)
                              score = self.minimax(False, board)
                              board.set(cell, ' ')
                              if score > bestScore:
                                    bestScore = score
                  return bestScore
            else:
                  bestScore = float('inf')
                  for cell in board._get_labels():
                        if board.isempty(cell):
                              board.set(cell, self.returnOpponentSign())
                              score = self.minimax(True, board)
                              board.set(cell, ' ')
                              if score < bestScore:
                                    bestScore = score
                  return bestScore


      def choose(self, board):
            board.set(self.bestMove(board, False), self.sign)