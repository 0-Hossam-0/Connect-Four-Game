
class SmartAgent:
    def __init__(self, playerColor):
        self.playerColor = playerColor
        self.playerNum = 2
        self.opponentNum = 1

    def minimax(self, numericBoard, depth, alpha, beta, maximizingPlayer):
        validMoves = self._getValidMoves(numericBoard)
        gameOver, winner = self._isTerminal(numericBoard)

        if depth == 0 or gameOver:
            if gameOver:
                if winner == self.playerNum:
                    return (None, 1000000)
                elif winner == self.opponentNum:
                    return (None, -1000000)
                else:
                    return (None, 0)
            else:
                return (None, self._scorePosition(numericBoard, self.playerNum))
        if maximizingPlayer:
            value = -float('inf')
            bestColumn = validMoves[0]
            for col in validMoves:
                row = self._getNextOpenRow(numericBoard, col)
                tempBoard = [row.copy() for row in numericBoard]
                self._dropPiece(tempBoard, row, col, self.playerNum)
                newScore = self.minimax(tempBoard, depth-1, alpha, beta, False)[1]
                if newScore > value:
                    value = newScore
                    bestColumn = col
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return bestColumn, value
        else:
            value = float('inf')
            bestColumn = validMoves[0]
            for col in validMoves:
                row = self._getNextOpenRow(numericBoard, col)
                tempBoard = [row.copy() for row in numericBoard]
                self._dropPiece(tempBoard, row, col, self.opponentNum)
                newScore = self.minimax(tempBoard, depth-1, alpha, beta, True)[1]
                if newScore < value:
                    value = newScore
                    bestColumn = col
                beta = min(beta, value)
                if alpha >= beta:
                    break
            return bestColumn, value

    def _convertBoardToNumeric(self, originalBoard):
        numericBoard = []
        for row in originalBoard:
            newRow = []
            for segment in row:
                if segment['color'] == '⬜':
                    newRow.append(0)
                elif segment['color'] == self.playerColor:
                    newRow.append(2)
                else:
                    newRow.append(1)
            numericBoard.append(newRow)
        return numericBoard

    def _getValidMoves(self, numericBoard):
        return [col for col in range(7) if numericBoard[0][col] == 0]

    def _getNextOpenRow(self, numericBoard, col):
        for r in range(5, -1, -1):
            if numericBoard[r][col] == 0:
                return r
        return -1

    def _dropPiece(self, board, row, col, player):
        board[row][col] = player

    def _isTerminal(self, numericBoard):
        for col in range(7):
            for row in range(6):
                if numericBoard[row][col] != 0:
                    if self._checkWin(numericBoard, row, col):
                        return True, numericBoard[row][col]
        return False, None

    def _checkWin(self, numericBoard, row, col):
        player = numericBoard[row][col]
        if col <= 3:
            if all(numericBoard[row][col+i] == player for i in range(4)):
                return True
        if row <= 2:
            if all(numericBoard[row+i][col] == player for i in range(4)):
                return True
        if row <= 2 and col <= 3:
            if all(numericBoard[row+i][col+i] == player for i in range(4)):
                return True
        if row >= 3 and col <= 3:
            if all(numericBoard[row-i][col+i] == player for i in range(4)):
                return True
        return False

    def _scorePosition(self, numericBoard, player):
      score = 0
      centerArray = [row[3] for row in numericBoard]
      centerCount = centerArray.count(player)
      score += centerCount * 3
      for r in range(6):
          for c in range(7):
              if numericBoard[r][c] == player:
                  if c <= 3:
                      window = numericBoard[r][c:c+4]
                      score += self._evaluateWindow(window, player)
                  if r <= 2:
                      window = [numericBoard[r+i][c] for i in range(4)]
                      score += self._evaluateWindow(window, player)
                  if r <= 2 and c <= 3:
                      window = [numericBoard[r+i][c+i] for i in range(4)]
                      score += self._evaluateWindow(window, player)
                  if r >= 3 and c <= 3:
                      window = [numericBoard[r-i][c+i] for i in range(4)]
                      score += self._evaluateWindow(window, player)
      return score

    def _evaluateWindow(self, window, player):
        score = 0
        opponent = 1 if player == 2 else 2
        if window.count(player) == 4:
            score += 100
        elif window.count(player) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(player) == 2 and window.count(0) == 2:
            score += 2
        if window.count(opponent) == 3 and window.count(0) == 1:
            score -= 4
        return score

    def _scoreWindow(self, window, player, opponent):
        score = 0
        if window.count(player) == 4:
            score += 100
        elif window.count(player) == 3 and window.count(0) == 1:
            score += 5
        elif window.count(player) == 2 and window.count(0) == 2:
            score += 2

        if window.count(opponent) == 3 and window.count(0) == 1:
            score -= 4
        return score
