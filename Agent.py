class Agent:
  def __init__(self, username, color, isBot, model=None):
    self.username = username
    self.color = color
    self.isBot = isBot
    self.model = model