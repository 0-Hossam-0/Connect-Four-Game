from Agent import Agent
import random

class Game(Agent):

  def __init__(self, name):
    self.name = name
    self.isBoardAvailable = True
    self.isAutoPlay = False
    self.board = (
  (
  {'place': 'A1', 'color':'⬜'},
  {'place': 'A2', 'color':'⬜'},
  {'place': 'A3', 'color':'⬜'},
  {'place': 'A4', 'color':'⬜'},
  {'place': 'A5', 'color':'⬜'},
  {'place': 'A6', 'color':'⬜'},
  {'place': 'A7', 'color':'⬜'},
  ),
  (
  {'place': 'B1', 'color':'⬜'},
  {'place': 'B2', 'color':'⬜'},
  {'place': 'B3', 'color':'⬜'},
  {'place': 'B4', 'color':'⬜'},
  {'place': 'B5', 'color':'⬜'},
  {'place': 'B6', 'color':'⬜'},
  {'place': 'B7', 'color':'⬜'},
  ),
  (
  {'place': 'C1', 'color':'⬜'},
  {'place': 'C2', 'color':'⬜'},
  {'place': 'C3', 'color':'⬜'},
  {'place': 'C4', 'color':'⬜'},
  {'place': 'C5', 'color':'⬜'},
  {'place': 'C6', 'color':'⬜'},
  {'place': 'C7', 'color':'⬜'},
  ),
  (
  {'place': 'D1', 'color':'⬜'},
  {'place': 'D2', 'color':'⬜'},
  {'place': 'D3', 'color':'⬜'},
  {'place': 'D4', 'color':'⬜'},
  {'place': 'D5', 'color':'⬜'},
  {'place': 'D6', 'color':'⬜'},
  {'place': 'D7', 'color':'⬜'},
  ),
  (
  {'place': 'E1', 'color':'⬜'},
  {'place': 'E2', 'color':'⬜'},
  {'place': 'E3', 'color':'⬜'},
  {'place': 'E4', 'color':'⬜'},
  {'place': 'E5', 'color':'⬜'},
  {'place': 'E6', 'color':'⬜'},
  {'place': 'E7', 'color':'⬜'},
  ),
  (
  {'place': 'F1', 'color':'⬜'},
  {'place': 'F2', 'color':'⬜'},
  {'place': 'F3', 'color':'⬜'},
  {'place': 'F4', 'color':'⬜'},
  {'place': 'F5', 'color':'⬜'},
  {'place': 'F6', 'color':'⬜'},
  {'place': 'F7', 'color':'⬜'},
  ),
    )
  def _getSegmentByPlace(self, place : str):
    for row in self.board:
      for segment in row :
        if segment['place'] == place:
          return segment


  def _getLowerIndex(self, place : str):
    index = place[1]
    match index:
      case '2':
        index = '1'
      case '3':
        index = '2'
      case '4':
        index = '3'
      case '5':
        index = '4'
      case '6':
        index = '5'
      case '7':
        index = '6'
      case '1':
        return None
    return index
  def _getHigherIndex(self, place : str):
    index = place[1]
    match index:
      case '1':
        index = '2'
      case '2':
        index = '3'
      case '3':
        index = '4'
      case '4':
        index = '5'
      case '5':
        index = '6'
      case '6':
        index = '7'
      case '7':
        return None
    return index
  def _getHigherLevel(self, place : str):
    level = place[0]
    match level:
      case 'A':
        level = 'B'
      case 'B':
        level = 'C'
      case 'C':
        level = 'D'
      case 'D':
        level = 'E'
      case 'E':
        level = 'F'
      case 'F':
        return None
    return level
  def _getLowerLevel(self, place : str):
    level = place[0]
    match level:
      case 'B':
        level = 'A'
      case 'C':
        level = 'B'
      case 'D':
        level = 'C'
      case 'E':
        level = 'D'
      case 'F':
        level = 'E'
      case 'A':
        return None
    return level
  def _checkHorizontal(self, place: str, color: str):
    winCounter = 3

    currentPlace = place
    while winCounter >= 1:
        higherIndex = self._getHigherIndex(currentPlace)
        if higherIndex is None:
            break
        nextPlace = currentPlace[0] + higherIndex
        nextSegment = self._getSegmentByPlace(nextPlace)
        if nextSegment['color'] == color:
            winCounter -= 1
            currentPlace = nextPlace
        else:
            break
    currentPlace = place
    while winCounter >= 1:
        lowerIndex = self._getLowerIndex(currentPlace)
        if lowerIndex is None:
            break
        nextPlace = currentPlace[0] + lowerIndex
        nextSegment = self._getSegmentByPlace(nextPlace)
        if nextSegment['color'] == color:
            winCounter -= 1
            currentPlace = nextPlace
        else:
            break
    return winCounter <= 0

  def _checkVertical(self, place : str, color : str):
    winCounter = 3
    currentPlace = place
    while winCounter >= 1:
        higherLevel = self._getHigherLevel(currentPlace)
        if higherLevel is None:
            break
        nextPlace = higherLevel + currentPlace[1]
        nextSegment = self._getSegmentByPlace(nextPlace)
        if nextSegment['color'] == color:
            winCounter -= 1
            currentPlace = nextPlace
        else:
            break

    currentPlace = place
    while winCounter >= 1:
        lowerLevel = self._getLowerLevel(currentPlace)
        if lowerLevel is None:
            break
        nextPlace = lowerLevel + currentPlace[1]
        nextSegment = self._getSegmentByPlace(nextPlace)
        if nextSegment['color'] == color:
            winCounter -= 1
            currentPlace = nextPlace
        else:
            break
    return winCounter <= 0

  def _checkRightAngle(self, place : str, color : str):
    winCounter = 4
    currentPlace = place
    while winCounter >= 1:
        lowerLevel = self._getLowerLevel(currentPlace)
        higherIndex = self._getHigherIndex(currentPlace)
        if lowerLevel is None or higherIndex is None:
            break
        nextPlace = lowerLevel + higherIndex
        nextSegment = self._getSegmentByPlace(nextPlace)
        if nextSegment['color'] == color:
            winCounter -= 1
            currentPlace = nextPlace
        else:
            break

    currentPlace = place
    while winCounter >= 1:
        higherLevel = self._getHigherLevel(currentPlace)
        lowerIndex = self._getLowerIndex(currentPlace)
        if higherLevel is None or lowerIndex is None:
            break
        nextPlace = higherLevel + lowerIndex
        nextSegment = self._getSegmentByPlace(nextPlace)
        if nextSegment['color'] == color:
            winCounter -= 1
            currentPlace = nextPlace
        else:
            break
    return winCounter <= 0

  def _checkLeftAngle(self, place : str, color : str):
    winCounter = 4
    currentPlace = place
    while winCounter >= 1:
        lowerLevel = self._getLowerLevel(currentPlace)
        lowerIndex = self._getLowerIndex(currentPlace)
        if lowerLevel is None or lowerIndex is None:
            break
        nextPlace = lowerLevel + lowerIndex
        nextSegment = self._getSegmentByPlace(nextPlace)
        if nextSegment['color'] == color:
            winCounter -= 1
            currentPlace = nextPlace
        else:
            break

    currentPlace = place
    while winCounter >= 1:
        higherLevel = self._getLowerLevel(currentPlace)
        higherIndex = self._getHigherIndex(currentPlace)
        if higherLevel is None or higherIndex is None:
            break
        nextPlace = higherLevel + higherIndex
        nextSegment = self._getSegmentByPlace(nextPlace)
        if nextSegment['color'] == color:
            winCounter -= 1
            currentPlace = nextPlace
        else:
            break
    return winCounter <= 0
  def _isWin(self, agent : Agent, lastMove: {str, str}):
    if self.isBoardAvailable and (self._checkHorizontal(lastMove['place'], agent.color) or self._checkVertical(lastMove['place'], agent.color) or self._checkRightAngle(lastMove['place'], agent.color) or self._checkLeftAngle(lastMove['place'], agent.color)):
       print(agent.username +'!', 'Won the Game')
       self.isBoardAvailable = False
    return
  def _isFullBoard(self):
     isWhiteSegmentAvailable = False
     for row in self.board:
      for segment in row :
        if segment['color'] == '⬜':
          isWhiteSegmentAvailable = True
      if isWhiteSegmentAvailable:
         self.isBoardAvailable = True
      else:
         self.isBoardAvailable = False
  def makeMove(self, agent: Agent, index : int):
    index -= 1
    if not self.isBoardAvailable:
      print('Full Board')
      return False
    for rowIndex in range(5,-1,-1):
      currentSegment = self.board[rowIndex][index]
      if currentSegment['color'] == '⬜':
         currentSegment['color'] = agent.color
         self._isWin(agent, currentSegment)
         return True
    if not self.isAutoPlay: print('Index Overflow!')
    return False

  def displayBoard(self):
    print('______________')
    print('|1|2|3|4|5|6|7')
    for row in self.board:
      print("".join(str(segment['color']) for segment in row))

  def autoPlay(self, agents: list[Agent]):
    agentPlay = int
    self.isAutoPlay = True
    index = 0
    while self.isBoardAvailable:
      self._isFullBoard()
      agentPlay = random.randint(0,6)
      if not self.makeMove(agents[index], agentPlay):
        continue
      if index == len(agents) - 1:
         index = 0
         continue
      index += 1
  def startGameWithBot(self, agents: list[Agent]):
     index = 0
     while self.isBoardAvailable:
        if index == len(agents):
           index = 0
        print(agents[index].username, 'Turn')
        self._isFullBoard()
        if agents[index].isBot:
          agentPlay = random.randint(0,6)
          if not self.makeMove(agents[index], agentPlay):
            continue
          self.displayBoard()
          index += 1
        else:
           try:
              userPlay = int(input('Enter '+ agents[index].username + ' Next Move '))
              if userPlay >= 1 and userPlay <= 7:
                if not self.makeMove(agents[index], userPlay):
                  continue
                self.displayBoard()
                index += 1
              else:
                 print('Wrong Index')
           except ValueError:
              print('Invalid Input, Must Be Between 0 and 6')
              continue
